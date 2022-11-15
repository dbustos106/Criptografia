import json
import hashlib
import datetime
import requests

from flask import Flask, jsonify, request
from uuid import uuid4
from urllib.parse import urlparse


'''
class BlockChain
'''
class BlockChain:

    def __init__(self):
        self.chain = []
        self.nodes = set()
        self.transactions = []
        self.difficulty = 3
        
        initialBlock = self.createBlock(previousHash='0')
        initialHash = self.calculateHash(initialBlock)
        self.addBlock(initialBlock, initialHash)
        

    def getPreviousBlock(self):
        return self.chain[-1]


    def calculateHash(self, block):
        encodedBlock = json.dumps(str(block['index']) + block['previousHash'] + str(block['transactions']) + str(block['nonce']), sort_keys=True).encode()
        return hashlib.sha256(encodedBlock).hexdigest()


    def createBlock(self, previousHash):
        newBlock = {'index': len(self.chain) + 1,
                    'timestamp': str(datetime.datetime.now()),
                    'nonce': 0,
                    'transactions': self.transactions.copy(),
                    'previousHash': previousHash,
                    'hash': None}
        return newBlock


    def addTransaction(self, amount, receiver, sender):
        newTransaction = {"amount": amount, "receiver": receiver, "sender": sender}
        self.transactions.append(newTransaction)
        return self.getPreviousBlock()['index'] + 1


    def addNode(self, address):
        parseUrl = urlparse(address)
        self.nodes.add(parseUrl.netloc)


    def addBlock(self, block, hash):
        block['hash'] = hash
        self.chain.append(block)
        return block


    def replaceChain(self):
        network = self.nodes
        longestChain = None
        maxLength = len(self.chain)

        for node in network:
            response = requests.get(f'http://{node}/getChain')
            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']
                
                if length > maxLength and self.isChainValid(chain):
                    maxLength = length
                    longestChain = chain

        if longestChain:
            self.chain = longestChain
            return True
        return False
                

    def proofOfWork(self, block):
        hash = self.calculateHash(block)
        while not hash.startswith('0' * self.difficulty):
            block['nonce'] += 1
            hash = self.calculateHash(block)
        return hash


    def isChainValid(self, chain):
        previousBlock = chain[0]
        blockIndex = 1
        while blockIndex < len(chain):
            block = chain[blockIndex]
            if (block['previousHash'] != self.calculateHash(previousBlock)):
                return False
            computedHash = self.calculateHash(block)
            if (not computedHash.startswith('0' * self.difficulty)):
                return False

            previousBlock = block
            blockIndex += 1

        return True



app = Flask(__name__)
nodeAddress = str(uuid4()).replace('-', '')
blockChain = BlockChain()


@app.route("/mineBlock", methods=['GET'])
def mineBlock():
    blockChain.addTransaction(amount=1, sender=nodeAddress, receiver="Pulga")
    
    previousBlock = blockChain.getPreviousBlock()
    newBlock = blockChain.createBlock(previousBlock['hash'])
    hash = blockChain.proofOfWork(newBlock)

    blockChain.addBlock(newBlock, hash)
    blockChain.transactions = []
    
    response = {"message": "Has minado un bloque",
                "index": newBlock['index'],
                "nonce": newBlock['nonce'],
                "hash": newBlock['hash'],
                "transactions": newBlock['transactions']}

    return jsonify(response), 200


@app.route('/getChain', methods=['GET'])
def getChain():
    response = {
        'chain': blockChain.chain,
        'length': len(blockChain.chain)
    }
    return jsonify(response), 200


@app.route('/isValid', methods=['GET'])
def isValid():
    if blockChain.isChainValid(blockChain.chain):
        response = 'Cadena valida'
    else:
        response = 'Cadena no es valida'
    return jsonify(response), 200


@app.route('/addTransaction', methods=['POST'])
def addTransaction():
    json = request.get_json()
    transactionKeys = ['amount', 'receiver', 'sender']
    if not all (key in json for key in transactionKeys):
        return 'Falta algún elemento de la transacción', 400

    index = blockChain.addTransaction(json['amount'], json['receiver'], json['sender'])
    response = {'message':f'La transacción será añadida al bloque {index}'}

    return jsonify(response), 201


@app.route('/connectNode', methods=['POST'])
def connectNode():
    json = request.get_json()
    nodes = json.get('nodes')
    if nodes is None:
        return "No none", 401

    for node in nodes:
        blockChain.addNode(node)
    response = {'message':'La lista de nodos es:',
                'total_nodos': list(blockChain.nodes)}

    return jsonify(response), 201


@app.route('/replaceChain', methods=['GET'])
def replaceChain():
    isChainReplace = blockChain.replaceChain()

    if isChainReplace:
        response = {'message': 'Los nodos tenían diferentes nodos, estos fueron reemplazados por la más larga',
                    'newChain': blockChain.chain}
    else:
        response = {'message': 'Todo bien, la cadena es la más larga',
                    'newChain': blockChain.chain}
    return jsonify(response), 200


app.run(host='0.0.0.0', port='5003')