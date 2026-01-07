Persistência de Dados com Python (DGT2819)Este repositório contém o desenvolvimento do Trabalho Prático da disciplina DGT2819 - Persistência de Dados com Python1. O projeto aborda conceitos fundamentais de manipulação de arrays, algoritmos de ordenação e persistência em arquivos externos2.+1📋 Sobre o ProjetoO objetivo central foi atuar como um Analista de Dados para criar um MVP (Minimum Viable Product) de um glossário de termos3333. O trabalho consistiu em ler documentos em formato .txt, processar o conteúdo para extrair palavras individuais e ordená-las de forma eficiente4.+2Objetivos Principais:Implementação de algoritmos de ordenação manual (Bubble Sort e Selection Sort)5.Utilização de métodos nativos de ordenação do Python (sort)6.Manipulação de arquivos externos (Leitura e Escrita de dados)7.Análise de performance entre diferentes abordagens de ordenação888.+1📂 Estrutura do RepositórioO projeto está dividido entre as microatividades de suporte e o script final de integração9999.+1Pasta / ArquivoDescriçãomicroatividades/array.sort.pyOrdenação de arrays de inteiros e strings usando métodos nativos10101010.+1microatividades/bubble.sort.pyImplementação manual do algoritmo Bubble Sort11111111.+1microatividades/selection.sort.pyImplementação manual do algoritmo Selection Sort12121212.+1microatividades/ler.txt.pyTécnicas de leitura de arquivos e uso da instrução with13131313.+1microatividades/escrever.txt.pyEscrita de listas de strings em arquivos externos14141414.+1microatividades/loremipsum.txtArquivo base utilizado para os testes de leitura15.trabalho_pratico/kdd.pyScript final (MVP) que integra leitura, ordenação otimizada e escrita161616.+1🛠️ Tecnologias UtilizadasPython 3.x 17VS Code como IDE principal 18Biblioteca Time para medição de performance 19📈 Conclusões da Análise de PerformanceDurante o desenvolvimento do script kdd.py, foram comparados três métodos de ordenação21:Bubble Sort: Eficaz para listas pequenas, mas com performance reduzida em volumes maiores22.Selection Sort: Lógica simples de busca pelo menor elemento, mantendo complexidade similar ao Bubble Sort23.Método Nativo (.sort): Escolhido para a versão final do MVP por apresentar a melhor performance e otimização24.Nota: Este projeto foi desenvolvido seguindo as orientações de Programação Estruturada e manipulação de fluxos de dados em Python25.Criado por: Samuel Davidson


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

