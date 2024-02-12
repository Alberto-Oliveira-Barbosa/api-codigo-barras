# API para a criação de código de barras.

API para a criação de código de barras, desenvolvido na semana NLW da Rocketseat.   
Foi utilizando Python como linguagem de programação, além das bibliotecas Python-Barcode para a criação dos códigos de barras e Flask como framework de construção da API.   
O servidor recebe uma requisição POST com um json contendo um código de produto (``product_code``) que será usado para a criação de um código de barras e salvo na pasta `tags` do projeto.

## Tecnologias utilizadas:
- `Python` como linguagem de programação.
- `Python-Barcode` como biblioteca de criação dos códigos de barras.
- `Flask` para a criação do servidor da aplicação.
- `Pylint` para a padronização e análise da qualidade do código.
- `Pre-Commit` como biblioteca para validação do código antes de ser feito um commit.
- `Cerberus` para o tratamento de erros
- `Unittest` para a criação de testes unitários.

---

### Instalação do setup do projeto:

- Fazer o clone do repositório
- Navegar até a pasta do projeto.
- Não é obrigatório, mas altamente recomendado trabalhar com ambientes virtuais com python, para criar um novo ambiente virtual usar o comando:
```bash
python -m venv .venv
```
- A ativação do ambiente virtual vai depender do seu sistema operacional:
```bash
# Ambiente Linux - Unix
. .venv/bin/activate
```
```bash
# windows com Powershell
venv/Scripts/activate.ps1
```
```bash
# windows com CMD
venv/Scripts/activate.bat
```
- O arquivo requirements.txt possui as bibliotecas usadas no projeto, para fazer a sua instalação em lote de todas as bibliotecas usar o comando:
```bash
pip install -r requirements.txt
```
---

### Modo de utilização:
- rodar o aquivo `app.py` para a inicialização do servidor 
```python
python app.py
```
- Fazer uma requisição `POST` para a rota `http://localhost:3000/create_tag` passando no corpo da requisição um json com o atributo `product_code`, contendo o valor a ser convertido em código de barras.

- Após o processamento ele será salvo na pasta `tags` do projeto.

