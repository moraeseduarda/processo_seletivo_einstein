# Processo Seletivo - Einstein Floripa (T.I.) 🧠

### Case escolhido: número 3 - Programação Dados

### Objetivo (Instruções)

A aplicação deve fazer a correção de um simulado, recebendo como input uma lista com respostas 
de alunos fictícios e seus respectivos gabaritos (planilhas excel).

Seu output deve conter os seguintes dados:

1. Média de acertos geral (em % e valor absoluto).
2. Média de acertos de cada aluno (em % e valor absoluto)
3. Total de acertos de cada aluno

### Funcionamento

- Esse código tem como entrada (input) duas planilhas do excel (Gabarito e Respostas) presentes na 
pasta input desse repositório. 
- Utilizei da biblioteca pandas para criar dataframes e realizar operações
básicas com os dados presentes nas planilhas.
- As operações estão explicadas em comentários no próprio código.

RESULTADOS
- O código retorna dois dataframes com os dados esperados e duas novas planilhas excel na pasta output do diretório.

### O que aprendi

Relembrei conceitos básicos sobre a utilização de Python para análise de dados usando bibliotecas. 
Possuo conhecimentos básicos em análise de dados, e estavam um pouco enferrujados, foi preciso um pouco de pesquisa e 
esforço, mas foi um ótimo exercício de conceitos.

### Como executar
Para executar deve-se clonar esse repositório do Github, de uma das duas formas:

1. Manualmente no botão Code e depois em download zip, isso resultará em um arquivo zip que será necessário descomprimir.
2. Ou por meio do terminal do git (que deve ser instalado anteriormente na máquina). Digita-se *git clone* e cola-se a URL
do repositório que também se encontra no botão Code.


Após, deve-se utilizar uma IDE para abrir o reposítório e rodar o código Python, assim será possível visualizar os 
outputs via console. 

Também disponibilizei um arquivo .ipynb com o mesmo código, mas com uma melhor visualização dos dataframes que
criei, usei Google Colab.


### Tecnologias utilizadas
- Linguagem python
- Pycharm e Google Colab: inicialmente escrevi tudo na IDE Pycharm, mas depois considerei que
seria interessante também disponibilizar o código em um arquivo .ipynb para melhor visualização dos resultados
- Bibliotecas pandas
- Github