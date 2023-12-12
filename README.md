# Automatic Presence

#### Preencha a lista de presença automaticamente usando reconhecimento facial

## Sobre
Durante os dias na faculdade, percebi problemas recorrentes na assinatura dos alunos na lista de presença. Sendo um desses problemas a desorganização e falta de atenção, fazendo com que alguns alunos não assinassem a lista mesmo estando presentes durante a aula.

Visto isso, faz-se necessário encontrar uma maneira de solucionar esse problema por meio do uso de tecnologias acessíveis e fáceis de manipular. Portanto, desenvolvi o projeto "Automatic Presence" que visa utilizar reconhecimento facial para preencher a lista de presença automaticamente quando os alunos entrarem na sala.

Esse projeto foi desenvolvido utilizando a linguagem de programação Python e algumas bibliotecas como a OpenCV e Face Recognition.

## Como Utilizar?

Para executar o projeto em seu dispositivo é necessário fazer o download de alguns requisitos essenciais.

Siga abaixo os

###### 1. Git;
https://git-scm.com/downloads

###### 2. Python 3.1X;
https://www.python.org/downloads/

###### 3. Visual Studio Code
https://code.visualstudio.com 

###### 4. Webcam

#### 1. Clonar repositório

Abra um terminal em algum diretório de sua preferencia e execute o comando:

> git clone https://github.com/JonathasSC/automatic_presence.git

#### 2. Abra com Visual Studio Code

Clique com o botão direito encima do diretório criado e abra um novo terminal/bash e execute o comando:

> code .

Automaticamente a pasta será aberta dentro do seu visual studio code.

#### 3. Criando Ambiente Virtual

Abra um terminal dentro do Visual Studio Code clicando em "Terminal" na barra superior

Digite e execute os comandos na seguinte ordem:

> python -m venv venv

> .\venv\Scripts\activate

#### 4. Download das bibliotecas necessárias

Ainda no terminal atual, execute o comando abaixo para fazer o download automático de todos os recursos necessários

> pip install -r requirements.txt

Esse procedimento demora um pouco a depender da velocidade de sua internet.

#### Inserindo rostos e nomes

Para que haja precisão, coloque imagens das pessoas a serem identificadas no diretório src/persons

Nomeei cada imagem com o nome e sobrenome separado por sublinhado(underscore), assim como no exemplo já presente de Robert Downey Jr.

#### Inserindo nomes na planilha

Abra o arquivo spreadsheet.xlsx em algum aplicativo adequado no seu dispositivo e logo abaixo de "Robert Downey Jr" coloque o nome completo em maiúsculo das pessoas que deseja marcar a presença

#### Executando código

Clicar sobre o arquivo "main.py" e no botão superior direito de "run"
No terminal será questionado o nome do professor, responda com o nome do professor responsável ou com o seu próprio nome.

Após isso será aberto uma janela identificando presentes e verificando se estão na planilha e se estão já marcados como presente, caso não, será marcado a presença com um "x" ao lado do nome.

