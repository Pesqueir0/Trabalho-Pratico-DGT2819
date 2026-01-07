# Persistência de Dados com Python (DGT2819)

Este repositório contém o desenvolvimento do Trabalho Prático da disciplina **DGT2819 - Persistência de Dados com Python**. O projeto aborda conceitos fundamentais de manipulação de arrays, algoritmos de ordenação e persistência em arquivos externos.

---

## 📋 Sobre o Projeto
O objetivo central foi atuar como um **Analista de Dados** para criar um MVP (*Minimum Viable Product*) de um glossário de termos. O fluxo de trabalho consistiu em:
* Ler documentos em formato `.txt`.
* Processar o conteúdo para extrair palavras individuais.
* Ordenar os dados de forma eficiente para geração do glossário final.

### Objetivos Principais
* **Ordenação Manual:** Implementação dos algoritmos *Bubble Sort* e *Selection Sort*.
* **Ordenação Nativa:** Utilização do método `sort()` do Python.
* **Persistência:** Manipulação de arquivos externos para leitura e escrita de dados.
* **Performance:** Análise comparativa entre diferentes abordagens de ordenação.

---

## 📂 Estrutura do Repositório
O projeto está organizado entre as microatividades de suporte e o script final de integração (KDD).

| Pasta / Arquivo | Descrição |
| :--- | :--- |
| `microatividades/array.sort.py` | Ordenação de arrays (inteiros e strings) usando métodos nativos. |
| `microatividades/bubble.sort.py` | Implementação manual do algoritmo Bubble Sort. |
| `microatividades/selection.sort.py` | Implementação manual do algoritmo Selection Sort. |
| `microatividades/ler.txt.py` | Técnicas de leitura de arquivos e uso da instrução `with`. |
| `microatividades/escrever.txt.py` | Escrita de listas de strings em arquivos externos. |
| `microatividades/loremipsum.txt` | Arquivo base utilizado para os testes de leitura. |
| `trabalho_pratico/kdd.py` | Script final (MVP) que integra leitura, ordenação otimizada e escrita. |

---

## 🛠️ Tecnologias Utilizadas
* **Python 3.x**: Linguagem base para o desenvolvimento.
* **VS Code**: IDE utilizada para codificação e depuração.
* **Biblioteca Time**: Utilizada para a medição precisa de performance dos algoritmos.

---

## 📈 Análise de Performance e Conclusões
Durante o desenvolvimento do script `kdd.py`, foram comparados três métodos de ordenação para definir a melhor abordagem para o MVP:

> **Bubble Sort:** Eficaz para listas pequenas, mas apresenta performance reduzida em volumes maiores de dados.
>
> **Selection Sort:** Lógica simples baseada na busca pelo menor elemento, mantendo complexidade similar ao Bubble Sort.
>
> **Método Nativo (.sort):** Escolhido para a versão final do projeto por apresentar a melhor performance e otimização interna (Timsort).

---

## 📝 Nota Técnica
Este projeto foi desenvolvido seguindo os princípios da **Programação Estruturada** e manipulação eficiente de fluxos de dados em Python.

**Criado por:** Samuel Davidson


Resultados:
PS C:\Users\leuma\Downloads\projeto_persistência> & "C:/Program Files/Python311/python.exe" c:/Users/leuma/Downloads/projeto_persistência/microatividades/array.sort.py
[3, 11, 13, 13, 19, 26, 28, 35, 41, 86, 86, 87, 87, 88, 98]
[98, 88, 87, 87, 86, 86, 41, 35, 28, 26, 19, 13, 13, 11, 3]
['cpf', 'dataNascimento', 'nome', 'rg']
['rg', 'nome', 'dataNascimento', 'cpf']
PS C:\Users\leuma\Downloads\projeto_persistência> & "C:/Program Files/Python311/python.exe" c:/Users/leuma/Downloads/projeto_persistência/microatividades/bubble.sort.py

[4, 5, 7, 10, 11, 12, 18, 21, 23, 33, 45, 56, 67, 89, 90]
PS C:\Users\leuma\Downloads\projeto_persistência> & "C:/Program Files/Python311/python.exe" c:/Users/leuma/Downloads/projeto_persistência/microatividades/ler.txt.py
--- Todo o conteúdo ---
Lorem ipsum dolor sit amet, consectetur
adipiscing elit,

sed do eiusmod tempor incididunt ut labore
et dolore magna aliqua.

Ut enim ad minim veniam, quis nostrud
exercitation ullamco laboris nisi

ut aliquip ex ea commodo consequat. Duis
aute irure dolor in

reprehenderit in voluptate velit esse cillum
dolore eu fugiat nulla pariatur.

Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia

deserunt mollit anim id est laborum.



--- Primeira linha ---
Lorem ipsum dolor sit amet, consectetur


--- 3 primeiros caracteres ---
Lor

--- Usando instrução WITH ---
Lorem ipsum dolor sit amet, consectetur
adipiscing elit,

sed do eiusmod tempor incididunt ut labore
et dolore magna aliqua.

Ut enim ad minim veniam, quis nostrud
exercitation ullamco laboris nisi

ut aliquip ex ea commodo consequat. Duis
aute irure dolor in

reprehenderit in voluptate velit esse cillum
dolore eu fugiat nulla pariatur.

Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia

deserunt mollit anim id est laborum.


PS C:\Users\leuma\Downloads\projeto_persistência> & "C:/Program Files/Python311/python.exe" c:/Users/leuma/Downloads/projeto_persistência/microatividades/selection.sort.py
[1, 2, 3, 5, 7, 9, 10, 11, 13, 14, 22, 29, 37, 44, 50]
PS C:\Users\leuma\Downloads\projeto_persistência> & "C:/Program Files/Python311/python.exe" c:/Users/leuma/Downloads/projeto_persistência/trabalho_pratico/kdd.py
MVP Concluído: Glossário jurídico básico gerado com sucesso.

