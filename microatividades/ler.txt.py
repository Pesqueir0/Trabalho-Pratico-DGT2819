import os

caminho_arquivo = "microatividades/loremipsum.txt"

if not os.path.exists(caminho_arquivo):
    caminho_arquivo = "loremipsum.txt"

arquivo = open(caminho_arquivo, "r")
print("--- Todo o conteúdo ---")
print(arquivo.read())
arquivo.close()

arquivo = open(caminho_arquivo, "r")
print("\n--- Primeira linha ---")
print(arquivo.readline())
arquivo.close()

arquivo = open(caminho_arquivo, "r")
print("\n--- 3 primeiros caracteres ---")
print(arquivo.read(3))
arquivo.close()

print("\n--- Usando instrução WITH ---")
with open(caminho_arquivo, "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)