palavras_lista = list()

with open("microatividades/loremipsum.txt", "r") as f: # [cite: 162]
    for linha in f:
        palavras = linha.split()
        for p in palavras:
            palavras_lista.append(p.lower().strip(",."))

palavras_lista.sort()


with open("trabalho_pratico/palavras_ordenadas.txt", "w") as f_out:
    for p in palavras_lista:
        f_out.write(p + "\n")

print("MVP Concluído: Glossário jurídico básico gerado com sucesso.")