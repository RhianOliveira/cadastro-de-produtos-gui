# 🛒 Projeto de Cadastro e CRUD de Produtos (Python, Tkinter & SQLite)

Este é um projeto simples de aplicação desktop (GUI) para gerenciamento de cadastro de usuários e um CRUD (Create, Read, Update, Delete) de produtos.

O projeto foi desenvolvido em Python, utilizando o ambiente Jupyter Notebook como rascunho inicial, e empacotado para ser executável.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python
* **Interface Gráfica (GUI):** Tkinter (módulo `tkinter` e `tkinter.ttk`)
* **Banco de Dados:** SQLite (`Projeto_Compras.db`)
    * **Conexão DB:** `pyodbc` (é necessário ter o driver ODBC para SQLite instalado no ambiente de execução)
* **Ambiente de Desenvolvimento:** Jupyter Notebook (`Cadastro de Produtos.ipynb`)
* **Empacotamento:** Ferramenta para transformar em executável (ex: PyInstaller)

## ✨ Funcionalidades Principais

O sistema realiza as seguintes operações:

### 1. Sistema de Login/Autenticação
* O aplicativo começa com uma tela de login simples.
* Verifica as credenciais do usuário (`Nome` e `Senha`) na tabela `Usuarios` do banco de dados.
* **Credenciais de Teste (Usuário/Senha):**
    * Jose / 987
    * Aluno / 123
    * Clevison Santos / 555
    * Hilda / 999

### 2. CRUD (Cadastro de Produtos)
Após o login bem-sucedido, o usuário acessa a tela de cadastro e gerenciamento de produtos, que permite:
* **READ (Visualizar):** Lista todos os produtos cadastrados em um `Treeview` (tabela).
* **CREATE (Novo):** Abre uma janela *Toplevel* para adicionar um novo produto (Nome, Descrição e Preço).
* **UPDATE (Editar):** Permite a edição de um registro ao dar um **duplo clique** na linha da tabela.
* **DELETE (Deletar):** Permite a exclusão de um registro selecionado.
* **Filtro/Busca:** Possui campos de entrada que filtram a lista de produtos em tempo real por `NomeProduto` e `Descricao`.

## 📂 Estrutura do Banco de Dados

O arquivo `Projeto_Compras.db` contém as seguintes tabelas e estruturas:

* **Tabela `Usuarios`:** Armazena as credenciais de acesso.
    * Colunas: `ID` (INTEGER, PK), `Nome` (TEXT), `Senha` (TEXT).
* **Tabela `Produtos`:** Armazena os itens para o CRUD.
    * Colunas: `Id` (INTEGER, PK), `NomeProduto` (TEXT), `Descricao` (TEXT), `Preco` (REAL).

## ⚙️ Como Rodar o Projeto

### 1. Pré-requisitos
* Python 3.x instalado.
* Ter o driver **SQLite3 ODBC Driver** instalado no seu sistema.

### 2. Instalação de Dependências
Crie um arquivo `requirements.txt` com as dependências e instale-as:

```bash
pip install pyodbc
# Outras dependências necessárias
