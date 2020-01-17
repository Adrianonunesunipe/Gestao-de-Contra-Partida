TITULODOPROJETO
=================
_DESCRIÇÃODOPROJETO_

## [](#considera%C3%A7%C3%B5es-iniciais)Considerações Iniciais

Essas instruções serão necessárias para configuração e execução do projeto em sua maquina local para desenvolvimento e possíveis casos de testes. Antes de tudo, visualize o arquivo abaixo sobre como você realizará a configuração do projeto para execução oficial.

### [](#pr%C3%A9-requisitos)Pré-requisitos

_EXEMPLO DE REQUERIMENTOS BÁSICOS PARA UMA APLICAÇÃO, É INTERESSANTE QUE AO LADO DA TECNOLOGIA, INFORME A SUA VERSÃO._

```
- Python 3.6.3
- Django 2.0.4
- MySQLClient 1.3.12
```

### [](#instalando)Instalando

É necessário ter instalado em sua máquina o Python 3.6.3 ou superior que é disponibilizado no site oficial do Python ([https://www.python.org/downloads/](https://www.python.org/downloads/)). Antes de finalizar confira em suas Variações de Ambiente do Windows e verifique que o Python encontra-se configurado em sua "path". Posteriormente, tem-se necessário criar e configurar a sua própria máquina virtual de desenvolvimento para que as ferramentas de projeto não se instalem em suas respectivas máquinas permanentemente.

```
	Criar a virtual enviroment:
		--> python -m venv (nomeDaEnviroment)
	Ativar a enviroment criada:
		--> (nomeDaEnviroment)/Scripts/activate
	Instalar o requirements.txt:
	    --> pip install -r requirements.txt
	Atualizar as migrações do banco de dados:
	    --> python manage.py makemigrations
	Construir o banco de dados da aplicação:
	    --> python manage.py migrate
```

## [](#executando-os-testes)Executando os testes

Para executar os testes. Será necessário alguns passos a mais, seguem abaixo a sequência dos mesmos:

```
	Acessar a pasta do projetos:
		--> cd PASTADOPROJETO
	Executar o arquivo manage.py:
		--> python manage.py runserver
	Abrir o navegador e acessar o link de localhost:
		--> localhost:8000
```

## [](#constru%C3%ADdo-com)Construído com

-   [Comic Sans](http://fonts.googleapis.com/css?family=Source+Sans+Pro:200,300,400,600,700,900) - Fonte utilizada no sistema.
-   [JQuery](http://code.jquery.com/ui/1.11.0/themes/smoothness/jquery-ui.css) - Dependencias do sistema
-   [Bootstrap](https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css) - Design do sistema
-   [Popper](https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.0/umd/popper.min.js) - Runs like AJAX (Pop-up's)


## [](#ComoBaixarDoGit)GitLabPull

Comandos para baixar os arquivos no repositório local:

------> 1: git init (criando o repositório local)

------> 2: git remote add origin (+ link do projeto)

------> 3: git pull origin (+ nome da branch para poder
puxar o projeto para 
o repositório local).


## [](#ComoUparNoGit)GitLabPush

Comandos para dar um Push nos arquivos do seu repositório local no GitLab:

-------> 1: git add . (para adicionar tudo que foi modificado no projeto no
repositório do git)

-------> 2: git status (para checar o status dos arquivos)

-------> 3: git commit -m "(entre as aspas você vai comentar algo sobre as
atualizações que você fez no projeto)"

-------> 4: git push origin (+ o nome da branch)

OBS: Sempre checar as credenciais para ter a certeza de que não está
usando as credenciais de outra pessoa. Se estiver usando as credenciais de 
outra pessoa basta apenas remover as credenciais dessa pessoa.

OBS: Caso remova as Credenciais que não seja a sua, logo após o commit do 
git irá aparecer os campos para poder entrar no git, assim, suas credenciais
serão registradas automaticamente.

OBS: Caso não esteja utilizando o seu computador, nunca esqueça de remover as
suas credenciais da máquina utilizada depois que finalizar as atualizações
diárias.


## [](#autores)Autores
 **Daniel Gomes** - _Desenvolvedor Back-End_ - [@dannyelgjl](https://github.com/dannyelgjl)
 
 
## [](#licen%C3%A7a)Licença

Este projeto tem licença administrada pela Fábrica de Software do Centro Universitário de João Pessoa.
