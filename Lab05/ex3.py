texto = "X-DSPAM-Confidence:0.8475"
inicio = texto.find(":") +1
final = len(texto)
numero = float(texto[inicio:final])
#print(inicio, final)
#print(texto[inicio:fin])
#print(typetexto[inicio:fin]))
print(type(numero))