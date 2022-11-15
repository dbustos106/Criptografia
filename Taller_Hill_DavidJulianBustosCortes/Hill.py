import numpy as np
import math
import sys


'''
  Esta función implementa el algoritmo extendido de euclides
'''
def extEuclides(a, b):
  if b == 0:
    return a, 1, 0
  else:
    aux_d, aux_x, aux_y = extEuclides(b, a % b)
    d, x, y = aux_d, aux_y, aux_x - math.floor(a/b)*aux_y
    return d, x, y


'''
  Esta función calcula el inverso multiplicatico de a mod m
'''
def inverse_mul(det, mod):
  gcd, x, y = extEuclides(det, mod)
  if gcd != 1:
    print("\ngcd(" + str(det) + ", " + str(mod) +  ") es diferente de 1, luego, la matriz no tiene inverso multiplicativo modulo", mod)
    sys.exit(1)

  return x


'''
  Esta función calcula el determinante de A
'''
def determinante(A):
  if len(A) == 1:
    return A[0, 0]

  elif len(A) == 2:
    return A[0,0]*A[1,1] - A[0,1]*A[1,0]

  else:

    pivote = A[0, 0]
    fila_pivote = A[0, :]
    columna_pivote = A[:, 0]

    B = A[1:, 1:]
    B = B.astype(float)

    for i in range(len(B)):
      for j in range(len(B)):
        B[i, j] = B[i, j] - fila_pivote[0, j+1]*columna_pivote[i+1, 0]/pivote

    return pivote*determinante(B)
    

'''
  Esta función calcula la matriz adjunta de A
'''
def adjunta(A):
  cof = np.zeros(A.shape)
  for i in range(len(A)):
    for j in range(len(A)):

      B = np.delete(A, i, axis=0)
      B = np.delete(B, j, axis=1)
      B = B.astype(float)

      cof[i, j] = pow(-1, i+j)*round(determinante(B), 3)

  adj = cof.T
  return adj


'''
  Esta función calcula la inversa modular de una matriz A mod m
'''
def inversa(A, mod):
  adj = adjunta(A)
  det = round(determinante(A), 3)

  if det == 0:
    print("\nEl determinante de la matriz es cero, luego, la matriz no tiene inverso multiplicativo modulo", mod)
    sys.exit(1)
  else:
    det_inv = inverse_mul(det, mod)
    inv = det_inv*adj
    inv = inv % mod
    return inv


'''
  Está función rompe en grupos de tamaño n al texto
'''
def breakIntoBlocks(m, n):
  while len(m) % n != 0:
    m = m + 'x'

  arr_m = list(map(lambda x: ord(x)-97, m))
  arr_m = np.matrix(arr_m).reshape(-1, n)
  return arr_m


'''
  Esta función encripta mediante el algoritmo de Hill
'''
def encrypt_hill(arr_m, K, m):
  for block in arr_m:
    ci = (block*K) % m
    printMessage(ci)


'''
  Esta función desencripta mediante el algoritmo de Hill
'''
def decrypt_hill(arr_c, inv_k, m):
  for block in arr_c:
    mi = (block*inv_k) % m
    printMessage(mi)


'''
  Esta función imprime un arreglo de bloques
'''
def printMessage(arr_m):
  for i in range(arr_m.shape[0]):
    for j in range(arr_m.shape[1]):
      block = chr(int(arr_m[i, j]) + 97)
      print(block, end="")


if __name__ == '__main__':
  
  opcion = input("Ingrese 1 para encriptar y 0 para desencriptar:\n>> ")
  if opcion == "1":

    # Solicitar el mensaje en texto plano al usuario (plaintext)
    m = input("\nIngrese el mensaje que desea encriptar:\n>> ").lower()
    m = m.replace(" ", "")

    # Solicitar la matriz de encriptación (key)
    k = input("\nIngrese la clave de encriptación:\n>> ")
    k = np.matrix(k)

    # Solicitar la base modular
    mod = input("\nIngrese la base modular:\n>> ")
    mod = int(mod)

    # Se calcula la inversa modular de k
    inv_k = inversa(k, mod)
    print("\nMatriz inversa:\n", inv_k)

    # Romper en grupos de tamaño dos al mensaje m
    arr_m = breakIntoBlocks(m, len(k))

    # Imprimir el plaintext en grupos de dos
    print("\nplaintext:", end="")
    printMessage(arr_m)

    # Encriptar el mensaje
    print("\nciphertext:", end="")
    encrypt_hill(arr_m, k, mod) 

  else: 

    # Solicitar el mensaje cifrado al usuario (ciphertext)
    c = input("\nIngrese el mensaje que desea desencriptar:\n>> ").lower()
    c = c.replace(" ", "")

    # Solicitar la matriz de encriptación (key)
    k = input("\nIngrese la clave de encriptación:\n>> ")
    k = np.matrix(k)

    # Solicitar la base modular
    mod = input("\nIngrese la base modular:\n>> ")
    mod = int(mod)

    # Se calcula la inversa modular de k
    inv_k = inversa(k, mod)
    print("\nMatriz inversa:\n", inv_k)

    # Romper en grupos de tamaño dos al mensaje c
    arr_c = breakIntoBlocks(c, len(k))

    # Imprimir el ciphertext en grupos de dos
    print("\nciphertext:", end="")
    printMessage(arr_c)

    # Desencriptar el mensaje
    print("\nplaintext:", end="")
    decrypt_hill(arr_c, inv_k, mod)

# Ejemplos