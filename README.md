Crud Sisqualis Django 1.7 + Python 2.7 ou superior
===================

##Descrição

O projeto tem por objetivo apresentar um CRUD (cadastro, edição, exclusão. busca e visualização) simples no Django. O Projeto cria um cadastro de usuários relacionados a categorias.

##Instalação

Para que o projeto rode perfeitamente é necessário a instalação dos itens abaixo:
```
1) Python 2.7 ou superior
2) Django 1.7
3) Fazer o download do projeto
```

###Instalação do Python 2.7

Em sistemas linux, por default, o python estará instalado. Caso necessite instalar, faça:


```
# cd /usr/local/src
# wget https://www.python.org/ftp/python/3.4.1/Python-3.4.1.tar.xz
```
**Descompacte o pacote: **
```
# tar zxvf Python-3.4.1.tar.xz 
```
**Acesse a pasta: **
```
# cd Python-3.4.1
```
**Agora vamos compilar e instalar: **
```
# ./configure -prefix=/usr
# make
# make install 
```

**Obs.:** *As configurações do tutorial foram realizadas no Ubuntu. Para mais informações de como instalar no windows clique no site ofical [Python.org](https://www.python.org/download/)*

###Instalação do Django 1.7
```
1) Remover versão antigas do Django
2) Instalando o pip
3) Instalando o Django via pip install
```

*[Clique aqui](https://docs.djangoproject.com/en/dev/topics/install/) e vá para o link oficial da instalação*


Caso você esteja atualizando o Django e não esteja utilizando o easy_install ou o pip é necessário remover o Django do sistema.
Caso você tenha instalado o Django utilizando o comando **python setup.py install**, para desinstalar basta apenas apagar a pasta do Django do sistema. Para localizar a pasta do Django entre com o comando:
```
python -c "import sys; sys.path = sys.path[1:]; import django; print(django.__path__)"
```

Instale o pip através do [tutorial oficial](https://pip.pypa.io/en/latest/installing.html#using-the-installer)

Para pegar a versão 1.7 atualmente BETA do Django, utilize o comando abaixo:
```
pip install https://www.djangoproject.com/download/1.7.b4/tarball/
```

