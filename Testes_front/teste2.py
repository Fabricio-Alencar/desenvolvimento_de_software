import tkinter as tk

def show_page2():
    page1.pack_forget()  # Esconde a primeira página
    page2.pack(fill="both", expand=True)  # Exibe a segunda página

def show_page1():
    page2.pack_forget()  # Esconde a segunda página
    page1.pack(fill="both", expand=True)  # Exibe a primeira página

# Criando a janela principal
root = tk.Tk()
root.title('Navegação entre Páginas')
root.geometry('400x300')

# Página 1
page1 = tk.Frame(root)  # Primeira página (frame)
label1 = tk.Label(page1, text="Esta é a Página 1", font=("Arial", 16))
label1.pack(pady=20)
button1 = tk.Button(page1, text="Ir para Página 2", command=show_page2, width=20)
button1.pack(pady=10)

# Página 2
page2 = tk.Frame(root)  # Segunda página (frame)
label2 = tk.Label(page2, text="Esta é a Página 2", font=("Arial", 16))
label2.pack(pady=20)
button2 = tk.Button(page2, text="Voltar para Página 1", command=show_page1, width=20)
button2.pack(pady=10)

# Exibindo a página inicial
page1.pack(fill="both", expand=True)  # Exibe a primeira página

root.mainloop()
