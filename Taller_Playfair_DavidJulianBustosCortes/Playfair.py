import numpy as np


'''
  Esta función crea la matriz cuadrada 5x5
'''
def matrixSquare(keyword):

  # Contruir la matriz 5x5 con las letras del alfabeto
  A = np.arange(1, 10)
  B = np.arange(11, 27)
  imatrix = np.concatenate((A, B), axis=0) 
  cmatrix = list(map(lambda x: chr(x+96), imatrix))

  # Recorrer de manera inversa la keyword
  for i, e in enumerate(keyword[::-1]):
    cmatrix.remove(e)
    cmatrix.insert(0, e)

  cmatrix = np.array(cmatrix).reshape((5, 5))
  return cmatrix


'''
  Esta función rompe en grupos de tamaño dos al mensaje m
'''
def breakIntoPairs(m):
  
  # Resolver pares repetidos
  i = 0
  while i+1 <= len(m)-1:
    if m[i] == m[i+1]:
      m = m[0:i+1] + 'x' + m[i+1::]

    i = i + 2

  # Convertir el mensaje en una matriz de dos columnas
  if len(m) % 2 != 0:
    m = m + "x"
  arr_m = np.array(list(m)).reshape((-1, 2))

  return arr_m


'''
  Esta función imprime un mensaje en pares de caracteres
'''
def printMessage(message, flag=True):

  for par in message:

    if flag:
      if par[0] == 'i':
        par[0] = 'i,j'
      if par[1] == 'i':
        par[1] = 'i,j'

    print(f'{par[0] + par[1]:5}', end=" ")
  print(end="\n")


'''
  Esta función realiza la encriptación del mensaje
'''
def encrypt(arr_m, cmatrix):

  arr_c = []

  # Traducir las tuplas
  for par in arr_m:

    if par[0] == 'j':
      par[0] = 'i'
    if par[1] == 'j':
      par[1] = 'i'

    # Ubicar el primer elemento en cmatrix
    index1 = np.where(cmatrix[:, :] == par[0])
    index1 = list(map(int, index1))

    # Ubicar el segundo elemento en cmatrix
    index2 = np.where(cmatrix[:, :] == par[1])
    index2 = list(map(int, index2))

    # Hacer traducciòn
    if index1[1] == index2[1]:
      index1[0] = (index1[0] + 1) % 5
      index2[0] = (index2[0] + 1) % 5
    elif index1[0] == index2[0]:
      index1[1] = (index1[1] + 1) % 5
      index2[1] = (index2[1] + 1) % 5
    else:
      index_aux = index1[1]
      index1[1] = index2[1]
      index2[1] = index_aux

    # Concatenar la traducciòn
    arr_c.append([cmatrix[index1[0], index1[1]], cmatrix[index2[0], index2[1]]])
  
  return arr_c


'''
  Esta función realiza la desencripción del mensaje
'''
def decrypt(arr_c, cmatrix):

  arr_m = []

  # Traducir las tuplas
  for par in arr_c:

    if par[0] == 'j':
      par[0] = 'i'
    if par[1] == 'j':
      par[1] = 'i'

    # Ubicar el primer elemento en cmatrix
    index1 = np.where(cmatrix[:, :] == par[0])
    index1 = list(map(int, index1))

    # Ubicar el segundo elemento en cmatrix
    index2 = np.where(cmatrix[:, :] == par[1])
    index2 = list(map(int, index2))

    # Hacer traducciòn
    if index1[1] == index2[1]:
      index1[0] = (index1[0] - 1) % 5
      index2[0] = (index2[0] - 1) % 5
    elif index1[0] == index2[0]:
      index1[1] = (index1[1] - 1) % 5
      index2[1] = (index2[1] - 1) % 5
    else:
      index_aux = index1[1]
      index1[1] = index2[1]
      index2[1] = index_aux

    # Concatenar la traducciòn
    arr_m.append([cmatrix[index1[0], index1[1]], cmatrix[index2[0], index2[1]]])
  
  return arr_m

if __name__ == '__main__':

  opcion = input("Ingrese 1 para encriptar y 0 para desencriptar:\n>> ")
  if opcion == "1":

    # Solicitar el mensaje en texto plano al usuario (plaintext)
    m = input("\nIngrese el mensaje que desea encriptar:\n>> ").lower()
    m = m.replace(" ", "")

    # Solicitar la llave de encriptación (keyword)
    keyword = input("\nIngrese la clave de encriptación:\n>> ").lower()
    keyword = keyword.replace(" ", "")

    # Crear la matriz cuadrada 5x5
    cmatrix = matrixSquare(keyword)
    print("\nMatriz cuadrada 5x5 utilizada para cifrar:\n", cmatrix)

    print("\nEncriptación:\n")

    # Romper en grupos de tamaño dos al mensaje m
    arr_m = breakIntoPairs(m)

    # Imprimir el plaintext en grupos de dos
    printMessage(arr_m.tolist(), False)

    # Encriptar el mensaje
    arr_c = encrypt(arr_m, cmatrix)  

    # Imprimir el ciphertext en grupos de dos
    printMessage(arr_c, True)

  else: 

    # Solicitar el mensaje cifrado al usuario (ciphertext)
    c = input("\nIngrese el mensaje que desea desencriptar:\n>> ").lower()
    c = c.replace(" ", "")

    # Solicitar la llave de encriptación (keyword)
    keyword = input("\nIngrese la clave de encriptación:\n>> ").lower()
    keyword = keyword.replace(" ", "")

    # Crear la matriz cuadrada 5x5
    cmatrix = matrixSquare(keyword)
    print("\nMatriz cuadrada 5x5 utilizada para decifrar:\n", cmatrix)

    print("\nDesencriptación:\n")

    # Romper en grupos de tamaño dos al mensaje c
    arr_c = breakIntoPairs(c)

    # Imprimir el ciphertext en grupos de dos
    printMessage(arr_c.tolist(), False)

    # Desencriptar el mensaje
    arr_m = decrypt(arr_c, cmatrix)

    # Imprimir el plaintext en grupos de dos
    printMessage(arr_m, True)


# Ejemplos:

# this secret message is encrypted
# we dl lk hw ly lf xp qp hf dl hy hw oy yl kp

# our friend from paris examined his empty glass with surprise as if evaporation had taken place while he wasnt look ingipoured some more wine and he settled back in his chair face tilted uptowards the sun
# ZO MH LC HY ZK MN SO NQ DL KT OQ CY KI EC LK SO YI EQ PQ RX EY KR WM NS DL GY LD GF AB YA QN YE AP GN IX PG HY YS NB HT EC TL KF VN RP YT PU PF CY EB YA WM KI MP LF UZ LH TC YH NP CK KL LY YT KI GB DH CY EC RD GN CL GO IH YE TY KI XO UY VN SC LX KF MX PW