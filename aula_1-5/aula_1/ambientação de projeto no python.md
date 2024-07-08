## Uso do Venv

**Para que serve?**

O venv é uma forma nativa que o python oferece para criar um ambiente virtual onde vamos conseguir colocar todas as dependencias/bibliotecas utilizadas no nosso projeto. 

podemos ter vários cenários onde criamos um projeto em si e varias pastas cada uma com o seu proprio ambiente virtual contendo suas dependencias.

**Como criar o venv**

- dentro da pasta do projeto que queremos criar a venv, vamos abrir o git bash (terminal) nela e rodar a seguiente linha: 
    - `python -m venv .venv`
- o ".venv" é o nome do ambiente virtual


**Ativando a venv**
- Para ativar a venv, temos que rodar o seguiente código:   
    -  `source .venv/Scripts/activate`

-  ativação serve somente para windows no linux é diferente

**saindo do ambiente virtual**

- `deactivate`


## Uso do PyEnv + Poetry

O Pyenv é uma biblioteca do python que ajuda a gente a versionar o python em várias camadas no nosso projeto. Por exemplo, posso ter o projeto A, utilizando o Python 3.10 e o projeto B utilizando o Python 3.12.

O Poetry é um orquestrador do venv, nele eu consigo criar o venv com mais facilidade, criar melhor um projeto, adicionar e remover pacotes com mais facilidade, por exemplo:

![alt text](image.png)

**Criando novo projeto com poetry**

`poetry new (nome_do_projeto)`

**Pyenv + Poetry**

No primeiro momento, eu baixo o pyenv e utilizando o pyenv faço um `pyenv install` selecionando a versão do python que eu quero usar

Depois faço um `pyenv global` especificando que quero utilizar globalmente uma versão especifica do python.

Entrando no poetry, eu tenho que fazer um `poetry env use (versão do python)` para o poetry entender qual versão eu quero usar no projeto.

E ele entendendo a versão que eu quero usar, ele ja cria automaticamente a venv dentro do projeto.

Para ativar o ambiente do poetry é só rodar um `poetry shell`

Para desativar é só rodar um `poetry exit`

Ou os comandos clássicos de ativaçãod e venv (activate e deactivate)

para adicionar uma biblioteca no projeto usando o poetry é só fazer um `poetry add (biblioteca)` 

