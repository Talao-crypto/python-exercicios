import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

from lib.dados import carregar_produtos
from lib.produtos import (
    cadastrar_produto,
    status_estoque,
    repor_produto,
    excluir_produto
)

# ===================== TELA DE CADASTRO =====================
def abrir_tela_cadastro():
    cadastro = tk.Toplevel()
    cadastro.title("Cadastro de Produto")
    cadastro.geometry("350x300")

    tk.Label(cadastro, text="Cadastrar Produto", font=("Arial", 14, "bold")).pack(pady=10)

    tk.Label(cadastro, text="Nome").pack()
    entry_nome = tk.Entry(cadastro, width=30)
    entry_nome.pack()

    tk.Label(cadastro, text="Categoria").pack()
    entry_categoria = tk.Entry(cadastro, width=30)
    entry_categoria.pack()

    tk.Label(cadastro, text="Quantidade").pack()
    entry_quantidade = tk.Entry(cadastro, width=30)
    entry_quantidade.pack()

    tk.Label(cadastro, text="Preço").pack()
    entry_preco = tk.Entry(cadastro, width=30)
    entry_preco.pack()

    def salvar():
        try:
            nome = entry_nome.get().strip()
            categoria = entry_categoria.get().strip()
            quantidade = int(entry_quantidade.get())
            preco = float(entry_preco.get())

            if not nome or not categoria:
                raise ValueError

            cadastrar_produto(nome, categoria, quantidade, preco)
            messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
            cadastro.destroy()

        except ValueError:
            messagebox.showerror("Erro", "Preencha os dados corretamente")

    tk.Button(
        cadastro,
        text="Salvar Produto",
        width=20,
        command=salvar
    ).pack(pady=15)


# ===================== TELA DE LISTAGEM =====================
def abrir_tela_listagem():
    lista = tk.Toplevel()
    lista.title("Produtos em Estoque")
    lista.geometry("720x380")

    tk.Label(
        lista,
        text="ESTOQUE DE PRODUTOS",
        font=("Arial", 14, "bold")
    ).pack(pady=10)

    colunas = ('id', 'nome', 'categoria', 'quantidade', 'preco', 'status')

    tabela = ttk.Treeview(lista, columns=colunas, show='headings')
    tabela.pack(fill='both', expand=True, padx=10)

    # Cabeçalhos
    tabela.heading('id', text='ID')
    tabela.heading('nome', text='Nome')
    tabela.heading('categoria', text='Categoria')
    tabela.heading('quantidade', text='Quantidade')
    tabela.heading('preco', text='Preço')
    tabela.heading('status', text='Status')

    # Tamanhos
    tabela.column('id', width=50, anchor='center')
    tabela.column('nome', width=160)
    tabela.column('categoria', width=130)
    tabela.column('quantidade', width=100, anchor='center')
    tabela.column('preco', width=100, anchor='center')
    tabela.column('status', width=120, anchor='center')

    # Cores por status
    tabela.tag_configure('OK', background='#d4f4dd')
    tabela.tag_configure('ACABANDO', background='#fff3cd')
    tabela.tag_configure('ACABOU', background='#f8d7da')

    # Scroll
    scroll = ttk.Scrollbar(lista, orient='vertical', command=tabela.yview)
    tabela.configure(yscrollcommand=scroll.set)
    scroll.pack(side='right', fill='y')

    # Carregar produtos
    produtos = carregar_produtos()
    for p in produtos:
        status = status_estoque(p['quantidade'])
        tabela.insert(
            '',
            'end',
            values=(
                p['id'],
                p['nome'],
                p['categoria'],
                p['quantidade'],
                f"R$ {p['preco']:.2f}",
                status
            ),
            tags=(status,)
        )

    # ===================== REPOR ESTOQUE =====================
    def repor():
        selecionado = tabela.focus()
        if not selecionado:
            messagebox.showwarning("Atenção", "Selecione um produto")
            return

        valores = tabela.item(selecionado, 'values')
        id_produto = int(valores[0])

        qtd = simpledialog.askinteger(
            "Repor Estoque",
            "Quantidade a adicionar:",
            minvalue=1
        )

        if qtd:
            repor_produto(id_produto, qtd)
            messagebox.showinfo("Sucesso", "Estoque atualizado")
            lista.destroy()
            abrir_tela_listagem()

    # ===================== EXCLUIR PRODUTO =====================
    def excluir():
        selecionado = tabela.focus()
        if not selecionado:
            messagebox.showwarning("Atenção", "Selecione um produto")
            return

        valores = tabela.item(selecionado, 'values')
        id_produto = int(valores[0])
        nome_produto = valores[1]

        confirmar = messagebox.askyesno(
            "Confirmar Exclusão",
            f"Deseja realmente excluir o produto:\n\n{nome_produto}?"
        )

        if confirmar:
            excluir_produto(id_produto)
            messagebox.showinfo("Sucesso", "Produto excluído com sucesso")
            lista.destroy()
            abrir_tela_listagem()

    # Botões
    tk.Button(lista, text="Repor Estoque", width=22, command=repor).pack(pady=5)
    tk.Button(lista, text="Excluir Produto", width=22, command=excluir).pack(pady=5)


# ===================== TELA PRINCIPAL =====================
janela = tk.Tk()
janela.title("Controle de Estoque")
janela.geometry("420x320")

tk.Label(
    janela,
    text="CONTROLE DE ESTOQUE",
    font=("Arial", 16, "bold")
).pack(pady=25)

tk.Button(
    janela,
    text="Cadastrar Produto",
    width=28,
    command=abrir_tela_cadastro
).pack(pady=6)

tk.Button(
    janela,
    text="Listar Produtos",
    width=28,
    command=abrir_tela_listagem
).pack(pady=6)

tk.Button(
    janela,
    text="Sair",
    width=28,
    command=janela.destroy
).pack(pady=12)

janela.mainloop()
