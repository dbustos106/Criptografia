import numpy as np

'''
  Esta función imprime un mensaje en bloques de 5
'''
def printMessage(message):
  i = 5
  while i < len(message):
    message = message[0:i] + " " + message[i::]
    i = i + 6
  print(message)


'''
  Esta función realiza la encripción del mensaje
'''
def encrypt(m, k):
  c = "".join(list(map(lambda x: chr(((ord(x)+k-97)%26)+97), m)))
  return c


'''
  Esta función realiza la desencripción del mensaje
'''
def decrypt(c, k):
  m = "".join(list(map(lambda x: chr(((ord(x)-k-97)%26)+97), c)))
  return m


if __name__ == '__main__':

  opcion = input("Ingrese 1 para encriptar y 0 para desencriptar:\n>> ")
  if opcion == "1":

    # Solicitar el mensaje en texto plano al usuario (plaintext)
    m = input("\nIngrese el mensaje que desea encriptar:\n>> ").lower()
    m = m.replace(" ", "")

    # Solicitar el parámetro k
    k = input("\nIngrese el parámetro k:\n>> ").lower()
    k = int(k)

    print("\nEncriptación:\n")

    # Imprimir el plaintext en bloques de tamaño k
    printMessage(m)

    # Encriptar el mensaje
    c = encrypt(m, k)

    # Imprimir el ciphertext en bloques de tamaño k
    printMessage(c)

  else: 

    # Solicitar el mensaje cifrado al usuario (ciphertext)
    c = input("\nIngrese el mensaje que desea desencriptar:\n>> ").lower()
    c = c.replace(" ", "")

    # Solicitar el parámetro k
    k = input("\nIngrese el parámetro k:\n>> ").lower()
    k = int(k)

    print("\nDesencriptación:\n")

    # Imprimir el ciphertext en bloques de tamaño k
    printMessage(c)

    # Desencriptar el mensaje
    m = decrypt(c, k)

    # Imprimir el plaintext en bloques de tamaño k
    printMessage(m)


# Ejemplos:

# RETUR NTORO ME
# uhwxu qwrur ph

# thisi sextr emely insec ureen crypt iondo notus eitto prote ctval uable infor matio n
# WKLVL VHAWU HPHOB LQVHF XUHHQ FUBSW LRQGR QRWXV HLWWR SURWH FWYDO XDEOH LQIRU PDWLR Q

# itisc laime dthee arlie stkno wnref erenc etoth istyp eofci pheri sinth ekama sutra which saysw omens hould learn thear tofse cretw ritil gtoco nceal their liaso ns
# LWLVF ODLPH GWKHH DUOLH VWNQR ZQUHI HUHQF HWRWK LVWBS HRIFL SKHUL VLQWK HNDPD VXWUD ZKLFK VDBVZ RPHQV KRXOG OHDUQ WKHDU WRIVH FUHWZ ULWLO JWRFR QFHDO WKHLU OLDVR QV

# WE WILL ATTACK AT DAWN THROUGH THE LEFT FLANK
# zhzlo odwwd fndwg dzqwk urxjk wkhoh iwiod qn