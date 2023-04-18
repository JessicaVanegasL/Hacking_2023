import string
import re

abc=string.ascii_letters

encriptado = open('ciphertext', 'r').read()
encriptado = re.findall('\{(.*?)\}',encriptado)[0]


rot = 56
salida = ''
for car in encriptado:
	salida += abc[ (abc.find(car) + rot) %57 ]

print(salida)
