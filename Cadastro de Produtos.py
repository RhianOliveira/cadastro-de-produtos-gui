#!/usr/bin/env python
# coding: utf-8

# In[2]:


#importa o modulo pyodbc para conexao com o bd
import pyodbc

#importa o modulo tkinter para construcao de interfaces graficas
from tkinter import *

#importa a classe ttk do modulo tkinter
from tkinter import ttk

#funcao que verifica se credenciais do usuario estao corretas
def verifica_credenciais():
    
    #Driver - drive
    #Server - servidor
    #Database - Nome do BD
    conexao =pyodbc.connect("Driver={SQLite3 ODBC Driver};Server=localhost;Database=Projeto_Compras.db")
    
    #Cursor - ferramenta para executar os comandos sql
    cursor = conexao.cursor()

    #executando uma query que seleciona os usuarios que possuem o nome de usuario e senha inseridos pelo usuario
    cursor.execute("SELECT * FROM Usuarios WHERE Nome = ? AND Senha = ?", (nome_usuario_entry.get(), senha_usuario_entry.get()))

    #recebendo os resultados
    usuario = cursor.fetchone()

    if usuario:

        #destruindo/fechando a janela de login
        janela_principal.destroy()
        
        #Driver - drive
        #Server - servidor
        #Database - Nome do BD
        dadosConexao = ("Driver={SQLite3 ODBC Driver};Server=localhost;Database=Projeto_Compras.db")
        
        #UID - Login
        #PWD - Senha
        #Criando a conexao
        conexao = pyodbc.connect(dadosConexao)
        cursor = conexao.cursor()
        
        conexao.execute("Select * From Produtos")
        print("Conectado com sucesso")
        
        def listar_dados():
        
            #limpa os valores da treeview
            for i in treeview.get_children():
                treeview.delete(i)
                
            cursor.execute("Select * From Produtos")
        
            valores = cursor.fetchall()
        
            for valor in valores:
        
                treeview.insert("", "end", values=(valor[0], valor[1], valor[2], valor[3]))
        
        #Criado uma janela tkinter com o titulo "Cadastro de Produtos"
        janela =Tk()
        janela.title("Cadastro de Produtos")
        
        #definindo a cor de fundo da janela
        janela.configure(bg="#F5F5F5")
        
        #deixando janela em tela cheia
        janela.attributes("-fullscreen", True)
        
        Label(janela, text="Nome do Produto: ", font="Arial 16", bg="#F5F5F5").grid(row=0, column=2, padx=10, pady=10)
        nome_produto = Entry(janela, font="Arial 16")
        nome_produto.grid(row=0, column=3, padx=10, pady=10)
        
        Label(janela, text="Descricao do Produto: ", font="Arial 16", bg="#F5F5F5").grid(row=0, column=5, padx=10, pady=10)
        descricao_produto = Entry(janela, font="Arial 16")
        descricao_produto.grid(row=0, column=6, padx=10, pady=10)
        
        Label(janela, text="Produtos: ", font="Arial 16", fg="blue", bg="#F5F5F5").grid(row=2, column=0, columnspan=10, padx=10, pady=10)
        
        def cadastrar():
        
            janela_cadastrar = Toplevel(janela)
            janela_cadastrar.title("Cadastrar Produto")
            
            #bg - background(cor do fundo)
            #definindo a cor de fundo da janela
            janela_cadastrar.configure(bg="#FFFFFF")
            
            #define a largura e altura da janela
            largura_janela = 450
            altura_janela = 250
            
            #obtem largura e altura da tela
            largura_tela = janela_cadastrar.winfo_screenwidth()
            altura_tela = janela_cadastrar.winfo_screenheight()
            
            #calcula a posicao da janela para centraliza-la na tela
            pos_x = (largura_tela // 2) - (largura_janela // 2)
            pos_y = (altura_tela // 2) - (altura_janela // 2)
            
            #define a posição da janela
            janela_cadastrar.geometry('{}x{}+{}+{}'.format(largura_janela, altura_janela, pos_x, pos_y))
        
            for i in range(5):
                janela_cadastrar.grid_rowconfigure(i, weight=1)
            for i in range(2):
                janela_cadastrar.grid_columnconfigure(i, weight=1)
        
            #adiciona bordas para cada campo de entrada
            estilo_borda = {"borderwidth": 2, "relief": "groove"}
        
            Label(janela_cadastrar, text="Nome do Produto:", font=("Arial", 12), bg="#FFFFFF").grid(row=0, column=0, padx=10, pady=10, stick="W")
            nome_produto_cadastrar = Entry(janela_cadastrar, font=("Arial", 12), **estilo_borda)
            nome_produto_cadastrar.grid(row=0, column=1, padx=10, pady=10)
        
            Label(janela_cadastrar, text="Descricao do Produto:", font=("Arial", 12), bg="#FFFFFF").grid(row=1, column=0, padx=10, pady=10, stick="W")
            descricao_produto_cadastrar = Entry(janela_cadastrar, font=("Arial", 12), **estilo_borda)
            descricao_produto_cadastrar.grid(row=1, column=1, padx=10, pady=10)
        
            Label(janela_cadastrar, text="Preco do Produto:", font=("Arial", 12), bg="#FFFFFF").grid(row=2, column=0, padx=10, pady=10, stick="W")
            preco_produto_cadastrar = Entry(janela_cadastrar, font=("Arial", 12), **estilo_borda)
            preco_produto_cadastrar.grid(row=2, column=1, padx=10, pady=10)
        
            def salvar_dados():
        
                #cria uma tupla com os valores dos campos de texto
                novo_produto_cadastrar = (nome_produto_cadastrar.get(), descricao_produto_cadastrar.get(), preco_produto_cadastrar.get())
        
                #inserindo informações no bd
                dados_usuario = ("Jose", "987")
                cursor.execute("INSERT INTO Produtos (NomeProduto, Descricao, Preco) Values (?, ?, ?)", novo_produto_cadastrar)
                conexao.commit() #gravando no bd
                
                print("Dados cadastrados com sucesso")
                
                janela_cadastrar.destroy()
                listar_dados()
                
            botao_salvar_dados = Button(janela_cadastrar, text="Salvar", font=("Arial", 12), command=salvar_dados)
            botao_salvar_dados.grid(row=3, column=0, columnspan=2, padx=10, pady=10, stick="NSEW")
        
            botao_cancelar = Button(janela_cadastrar, text="Cancelar", font=("Arial", 12), command=janela_cadastrar.destroy)
            botao_cancelar.grid(row=4, column=0, columnspan=2, padx=10, pady=10, stick="NSEW")
        
        
        botao_gravar = Button(janela, text="Novo", command=cadastrar, font="Arial 26")
        botao_gravar.grid(row=4, column=0, columnspan=4, stick="NSEW", padx=20, pady=5)
        
        #define o estile da treeview
        style = ttk.Style(janela)
        
        #criando a treeview
        treeview = ttk.Treeview(janela, style="mystyle.Treeview")
        
        #define estilo
        style.theme_use("default")
        #configurando
        style.configure("mystyle.Treeview", font=("Arial", 14))
        
        treeview = ttk.Treeview(janela, style="mystyle.Treeview", columns=("ID", "NomeProduto", "Descricao", "Preco"), show="headings", height=20)
        
        treeview.heading("ID", text="ID")
        treeview.heading("NomeProduto", text="Nome do Produto")
        treeview.heading("Descricao", text="Descricao do Produto")
        treeview.heading("Preco", text="Preco do Produto")
        
        treeview.column("#0", width=0, stretch=NO)
        treeview.column("ID", width=100)
        treeview.column("NomeProduto", width=300)
        treeview.column("Descricao", width=500)
        treeview.column("Preco", width=200)
        
        treeview.grid(row=3, column=0, columnspan=10, stick="NSEW")
        
        listar_dados()
        def editar_dados(event):
            #obtem o item selcionado no treeview
            item_selecionado = treeview.selection()[0]
        
            #obtem os valores do item slecionado
            valores_selecionados = treeview.item(item_selecionado)['values']
        
            janela_edicao = Toplevel(janela)
            janela_edicao.title("Editar Produto")
            
            #bg - background(cor do fundo)
            #definindo a cor de fundo da janela
            janela_edicao.configure(bg="#FFFFFF")
            
            #define a largura e altura da janela
            largura_janela = 500
            altura_janela = 200
            
            #obtem largura e altura da tela
            largura_tela = janela_edicao.winfo_screenwidth()
            altura_tela = janela_edicao.winfo_screenheight()
            
            #calcula a posicao da janela para centraliza-la na tela
            pos_x = (largura_tela // 2) - (largura_janela // 2)
            pos_y = (altura_tela // 2) - (altura_janela // 2)
            
            #define a posição da janela
            janela_edicao.geometry('{}x{}+{}+{}'.format(largura_janela, altura_janela, pos_x, pos_y))
        
            for i in range(5):
                janela_edicao.grid_rowconfigure(i, weight=1)
            for i in range(2):
                janela_edicao.grid_columnconfigure(i, weight=1)
        
            #adiciona bordas para cada campo de entrada
            estilo_borda = {"borderwidth": 2, "relief": "groove"}
        
            Label(janela_edicao, text="Nome do Produto:", font=("Arial", 16), bg="#FFFFFF").grid(row=0, column=0, padx=10, pady=10, stick="W")
            nome_produto_edicao = Entry(janela_edicao, font=("Arial", 16), **estilo_borda,  bg="#FFFFFF", textvariable=StringVar(value=valores_selecionados[1]))
            nome_produto_edicao.grid(row=0, column=1, padx=10, pady=10)
        
            Label(janela_edicao, text="Descricao do Produto:", font=("Arial", 16), bg="#FFFFFF").grid(row=1, column=0, padx=10, pady=10, stick="W")
            descricao_produto_edicao = Entry(janela_edicao, font=("Arial", 16), **estilo_borda,  bg="#FFFFFF", textvariable=StringVar(value=valores_selecionados[2]))
            descricao_produto_edicao.grid(row=1, column=1, padx=10, pady=10)
        
            Label(janela_edicao, text="Preco do Produto:", font=("Arial", 16), bg="#FFFFFF").grid(row=2, column=0, padx=10, pady=10, stick="W")
            preco_produto_edicao = Entry(janela_edicao, font=("Arial", 16), **estilo_borda,  bg="#FFFFFF", textvariable=StringVar(value=valores_selecionados[3]))
            preco_produto_edicao.grid(row=2, column=1, padx=10, pady=10)
        
            def salvar_edicao():
        
                #obtem novos valores do item selecionado no teeview
                nome_produto = nome_produto_edicao.get()
                nova_descricao = descricao_produto_edicao.get()
                novo_preco = preco_produto_edicao.get()
        
                #atualiza os valores do item selecionado
                treeview.item(item_selecionado, values=(valores_selecionados[0], nome_produto, nova_descricao, novo_preco))
        
                #inserindo informações no bd
                dados_usuario = ("Jose", "987")
                cursor.execute("UPDATE Produtos SET NomeProduto = ?, Descricao = ?, Preco = ? WHERE ID  = ?",
                   (nome_produto, nova_descricao, novo_preco, valores_selecionados[0]))
                conexao.commit() #gravando no bd
                
                print("Dados alterados com sucesso")
                
                janela_edicao.destroy()
                #listar_dados()
                
            botao_salvar_edicao = Button(janela_edicao, text="Alterar", font=("Arial", 16), bg="#008000", fg="#FFFFFF", command=salvar_edicao)
            botao_salvar_edicao.grid(row=4, column=0, padx=20, pady=20)
        
            def deletar_registro():
                
                selected_item = treeview.selection()[0]
                id = treeview.item(selected_item)['values'][0]
                
                cursor.execute("DELETE FROM Produtos WHERE id = ?", (id))
        
                conexao.commit()
        
                janela_edicao.destroy()
                listar_dados()
            
            botao_deletar_edicao = Button(janela_edicao, text="Deletar", font=("Arial", 16), bg="#FF0000", fg="#FFFFFF", command=deletar_registro)
            botao_deletar_edicao.grid(row=4, column=1, padx=20, pady=20)
        
        #adicina evento de duplo click para editar dados
        treeview.bind("<Double-1>", editar_dados)
        
        #configura a janela para utilizar a barra de menus criada
        menu_barra = Menu(janela)
        janela.configure(menu=menu_barra)
        
        #cria o menu chamado arquivo
        menu_arquivo = Menu(menu_barra, tearoff=0)
        menu_barra.add_cascade(label="Arquivo", menu=menu_arquivo)
        
        #cria uma opcao menu 'Arquivo" chamada "Cadastrar"
        menu_arquivo.add_command(label="Cadastrar", command=cadastrar)
        
        #cria uma opcao menu 'Arquivo" chamada "Sair"
        menu_arquivo.add_command(label="Sair", command=janela.destroy)
        
        #limpa dados da treeview
        def limparDados():
        
            #limpando valores da treeview
            for i in treeview.get_children():
                treeview.delete(i)
        
        
        
        def filtrar_dados(nome_produto, descricao_produto):
        
            #verifica se os campos estao vazios
            if not nome_produto.get() and not descricao_produto.get():
                listar_dados()
                return
            sql = "SELECT * FROM Produtos"
        
            params = []
        
            if nome_produto.get():
                sql += " WHERE NomeProduto LIKE ?"
                params.append('%' + nome_produto.get() + '%')
                
            if descricao_produto.get():
                if nome_produto.get():
                    sql += " AND"
                else:
                    sql += " WHERE"
                sql += " Descricao LIKE ?"
                params.append('%' + descricao_produto.get() + '%')
        
            cursor.execute(sql, tuple(params))
            produtos = cursor.fetchall()
            limparDados()
        
            #preenche treeview com dados filtrados
            for dado in produtos:
                treeview.insert('', 'end', values=(dado[0], dado[1], dado[2], dado[3]))
        
        nome_produto.bind('<KeyRelease>', lambda e: filtrar_dados(nome_produto, descricao_produto))
        descricao_produto.bind('<KeyRelease>', lambda e: filtrar_dados(nome_produto, descricao_produto))
        
        
        def deletar():
                
                selected_item = treeview.selection()[0]
                id = treeview.item(selected_item)['values'][0]
                
                cursor.execute("DELETE FROM Produtos WHERE id = ?", (id))
        
                conexao.commit()
                listar_dados()
        
        botao_deletar = Button(janela, text="Deletar", command=deletar, font="Arial 26")
        botao_deletar.grid(row=4, column=4, columnspan=4, stick="NSEW", padx=20, pady=5)
        
        #inicia a janela Tkinter
        janela.mainloop()
        
        cursor.close()
        conexao.close()
        
    else:

        mensagem_lbl = Label(janela_principal, text="Nome de usuario ou senha incorretos", fg="red")
        mensagem_lbl.grid(row=3, column=0, columnspan=2)

#criando a janela principal para a tela de login
janela_principal = Tk()
janela_principal.title("Tela de Login")

#bg - background(cor do fundo)
#definindo a cor de fundo da janela
janela_principal.configure(bg="#F5F5F5")

#define a largura e altura da janela
largura_janela = 450
altura_janela = 300

#obtem largura e altura da tela
largura_tela = janela_principal.winfo_screenwidth()
altura_tela = janela_principal.winfo_screenheight()

#calcula a posicao da janela para centraliza-la na tela
pos_x = (largura_tela // 2) - (largura_janela // 2)
pos_y = (altura_tela // 2) - (altura_janela // 2)

#define a posição da janela
janela_principal.geometry('{}x{}+{}+{}'.format(largura_janela, altura_janela, pos_x, pos_y))


#fg - foreground(cor da letra)
titulo_lbl = Label(janela_principal, text="Tela de Login", font="Arial 20", fg="blue", bg="#F5F5F5")
titulo_lbl.grid(row=0, column=0, columnspan=2, pady=20) #row - linha; column - coluna; columnspan - quantas colunas vai ocupar no grid; pady - espaço

#Campo Label
nome_usuario_lbl = Label(janela_principal, text="Nome de Usuario", font="Arial 14 bold", bg="#F5F5F5")
nome_usuario_lbl.grid(row=1, column=0, stick="e") #NSEW

#Campo Label
senha_usuario_lbl = Label(janela_principal, text="Senha", font="Arial 14 bold", bg="#F5F5F5")
senha_usuario_lbl.grid(row=2, column=0, stick="e") #NSEW

#Criadno entry para campo nome de usuario
nome_usuario_entry = Entry(janela_principal, font="Arial 14")
nome_usuario_entry.grid(row=1, column=1, pady=10)

#Criadno entry para campo senha
senha_usuario_entry = Entry(janela_principal, show="*", font="Arial 14")
senha_usuario_entry.grid(row=2, column=1, pady=10)

entrar_btn = Button(janela_principal, text="Entrar", font="Arial 14", command=verifica_credenciais)
entrar_btn.grid(row=4, column=0, columnspan=2, padx=20, pady=10, stick="NSEW") #stick - preenche laterais

sair_btn = Button(janela_principal, text="Sair", font="Arial 14", command=janela_principal.destroy)
sair_btn.grid(row=5, column=0, columnspan=2, padx=20, pady=10, stick="NSEW")

for i in range(5):
    janela_principal.grid_rowconfigure(i, weight=1)
for i in range(2):
    janela_principal.grid_columnconfigure(i, weight=1)

#inicia a janela Tkinter
janela_principal.mainloop()


# In[ ]:




