from ast import Num
import numpy as np

'''
  Esta función crea la matriz de encriptación
'''
def makeMatrix():
  matriz = [np.arange(26)]
  for i in range(26):
    fila = list(map(lambda x:(x+1)%26 , matriz[-1][:]))
    matriz = np.concatenate([matriz, [fila]], axis=0)

  return matriz


'''
  Esta función imprime un mensaje en bloques de 5
'''
def printMessage(message, t):
  i = t
  while i < len(message):
    message = message[0:i] + " " + message[i::]
    i = i + t + 1
  print(message)


'''
  Está función replica la keyword hasta alcanzar el tamaño del mensaje
'''
def replicateKey(keyword, tam_message):

  aux_keyword = keyword
  tam_keyword = len(keyword)

  for i in range(tam_message - tam_keyword):
    keyword = keyword + aux_keyword[i % tam_keyword]
  return keyword


'''
  Esta función realiza la encripción del mensaje
'''
def encrypt(m, keyword, imatrix):
  c = ""
  for i in range(len(m)):
    num = imatrix[ord(keyword[i]) - 97][ord(m[i]) - 97]
    c = c + chr(num + 97)
  return c


'''
  Esta función realiza la desencripción del mensaje
'''
def decrypt(c, keyword, imatrix):
  m = ""
  for i in range(len(c)):
    pos = np.where(imatrix[ord(keyword[i]) - 97] == ord(c[i]) - 97)
    m = m + chr(imatrix[0, np.array(pos[0][0])] + 97)
  return m


if __name__ == '__main__':

  opcion = input("Ingrese 1 para encriptar y 0 para desencriptar:\n>> ")
  if opcion == "1":

    # Solicitar el mensaje en texto plano al usuario (plaintext)
    m = input("\nIngrese el mensaje que desea encriptar:\n>> ").lower()
    m = m.replace(" ", "")

    # Solicitar la llave de encriptación (keyword)
    keyword = input("\nIngrese la clave de encriptación:\n>> ").lower()
    keyword = keyword.replace(" ", "")

    # Solicitar al usuario el parametro t
    t = input("\nIngrese el parametro t:\n>> ")
    t = int(t)

    print("\nEncriptación:\n")

    # Construir la matriz de encriptación
    imatrix = makeMatrix()

    # Replicar la keyword por cada posición del mensaje 
    keyword = replicateKey(keyword, len(m))

    # Imprimir la keyword en bloques de 5
    print("keyword      : ", end="")
    printMessage(keyword, t)

    # Imprimir el plaintext en bloques de 5
    print("plaintext    : ", end="")
    printMessage(m, t)

    # Encriptar el mensaje
    c = encrypt(m, keyword, imatrix)

    # Imprimir el ciphertext en bloques de 5
    print("chiphertext  : ", end="")
    printMessage(c, t)

  else: 

    # Solicitar el mensaje cifrado al usuario (ciphertext)
    c = input("\nIngrese el mensaje que desea desencriptar:\n>> ").lower()
    c = c.replace(" ", "")

    # Solicitar la llave de encriptación (keyword)
    keyword = input("\nIngrese la clave de encriptación:\n>> ").lower()
    keyword = keyword.replace(" ", "")

    # Solicitar al usuario el parametro t
    t = input("\nIngrese el parametro t:\n>> ")
    t = int(t)

    print("\nDesencriptación:\n")

    # Construir la matriz de encriptación
    imatrix = makeMatrix()

    # Replicar la keyword por cada posición del mensaje 
    keyword = replicateKey(keyword, len(c))

    # Imprimir la keyword en bloques de 5
    print("keyword     : ", end="")
    printMessage(keyword, t)

    # Imprimir el ciphertext en bloques de 5
    print("ciphertext  : ", end="")
    printMessage(c, t)

    # Desencriptar el mensaje
    m = decrypt(c, keyword, imatrix)

    # Imprimir el plaintext en bloques de 5
    print("plaintext   : ", end="")
    printMessage(m, t)


# Ejemplos:

# TO BE OR NOT TO BE THAT IS THE QUESTION
# ksmeh zbblk smemp ogajx sejcs flzsy

# THERE IS A SECRET PASSAGE BEHIND THE PICTURE FRAME
# vyc gxw urq tvf gkn plg cxc qxv keb ias rza inf gwp pfs