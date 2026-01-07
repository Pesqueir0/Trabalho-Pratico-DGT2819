arquivo = open("texto.txt", "w")
texto = list()
texto.append("Primeira frase.\n")
texto.append("Segunda frase.\n")
texto.append("Terceira frase.\n")

for linha in texto:
    arquivo.write(linha)
arquivo.close()