# Sistema de Gestão de Estoque (SGE)

Bem-vindo ao Sistema de Gestão de Estoque (SGE), um projeto desenvolvido em Django e Bootstrap 5 para facilitar o gerenciamento de estoque. Este README fornece informações essenciais sobre como configurar e executar o projeto em seu ambiente local.

## Requisitos

Certifique-se de que você tenha os seguintes requisitos instalados em seu sistema:

- Python (versão recomendada: 3.7 ou superior)
- Django (instalado automaticamente ao seguir as instruções abaixo)
- Outras dependências listadas no arquivo `requirements.txt`


## Instalação das Dependências

Instalar o ambiente virtual:
```bash
python3 -m venv venv
```

Ativar o ambiente virtual (Mac):
```bash
source venv/bin/activate
```

Ativar o ambiente virtual (Mac):
```bash
source venv/Scripts/activate
```

Com o ambiente virtual ativado, instale as dependências do projeto usando o comando:
```bash
pip install -r requirements.txt
```


## Rodar o projeto

Após instalar as dependências, aplique as migrations no banco de dados com o comando:
```bash
python manage.py migrate
```

Criar um super usuário para o sistema:
```bash
python manage.py createsuperuser
```

Agora o projeto jã pode ser inicializado com o comando:
```bash
python manage.py runserver
```

Após isso, o sistema estará pronto para ser acessado em:
[http://localhost:8000/admin/](http://localhost:8000/admin/)
