import tkinter as tk


dados = []




def mostrar_cadastro_administrativo():
    pagina1.pack_forget()  # Esconde a primeira página
    pagina2.pack(fill="both", expand=True)  # Exibe a segunda página

def mostrar_cadastro_professsor():
    pagina1.pack_forget()  # Esconde a primeira página
    pagina3.pack(fill="both", expand=True)  # Exibe a segunda página

def mostrar_cadastro_tecnico():
    pagina1.pack_forget()  # Esconde a primeira página
    pagina4.pack(fill="both", expand=True)  # Exibe a segunda página

def voltar_pagina1():
    for pagina in [pagina2, pagina3, pagina4]: # Esconde todas as outras páginas
        pagina.pack_forget()
    pagina1.pack(fill="both", expand=True)  # Exibe a primeira página



def Cadastrar_Administrativo():
    nome = nomeADM.get()  # Pega o valor da entrada "Nome"
    cpf = cpfADM.get()  # Pega o valor da entrada "Idade"
    
    # Aqui você pode armazenar os dados em uma lista ou base de dados, por exemplo:
    dados.append((nome, cpf))  # Armazenando os dados em uma lista
    
    # Exibindo uma mensagem ou algum feedback
    print(f"Cadastro realizado: {nome}, {cpf}")
    
    voltar_pagina1()  # Depois de cadastrar, volta para a página 1


# Criando a janela principal
root = tk.Tk()
root.title('Cadastro de Funcionários')
root.geometry('400x400') # Horizontal x Vertical



# Página 1
pagina1 = tk.Frame(root)  # Primeira página (frame)

etiqueta = tk.Label(pagina1, text="Selecione qual tipo de funionário\n você deseja cadastrar:", font=("Arial", 16)) 
# Cria uma "etiqueta", Label indica que vai ser um texto
etiqueta.pack(pady=20)  # Adiciona a etiqueta e um espaçamento vertical de 20 pixels


button = tk.Button(pagina1, text='Administrativo', width=20, command=mostrar_cadastro_administrativo)
button.pack(pady=20)

button = tk.Button(pagina1, text='Professor', width=20, command=mostrar_cadastro_professsor)
button.pack(pady=20)

button = tk.Button(pagina1, text='Técnico', width=20, command=mostrar_cadastro_tecnico)
button.pack(pady=20)

button = tk.Button(pagina1, text='Sair', width=20, command=root.destroy)
button.pack(pady=20)










# Página 2
pagina2 = tk.Frame(root)  # Segunda página (frame)

# Label
label2 = tk.Label(pagina2, text="Esta é a Página 2", font=("Arial", 16))
label2.pack(pady=20)  # Usando pack para o label com espaçamento

# Labels e campos de entrada
tk.Label(pagina2, text='Nome').pack()  # Label para "Nome"
nomeADM = tk.Entry(pagina2)  # Primeira entrada
nomeADM.pack(pady=5)  # Entrada 1 com espaçamento

tk.Label(pagina2, text='CPF').pack()  # Label vazio para espaçamento
cpfADM = tk.Entry(pagina2)  # Segunda entrada
cpfADM.pack(pady=5)  # Entrada 2 com espaçamento



button_cadastrar = tk.Button(pagina2, text="Cadastrar", command=Cadastrar_Administrativo)
button_cadastrar.pack(pady=20)


button2 = tk.Button(pagina2, text="Voltar para Página 1", command=voltar_pagina1, width=20)
button2.pack(pady=20)
















# Página 3
pagina3 = tk.Frame(root)  # Segunda página (frame)

label3 = tk.Label(pagina3, text="Esta é a Página 3", font=("Arial", 16))
label3.pack(pady=20)

button3 = tk.Button(pagina3, text="Voltar para Página 1", command=voltar_pagina1, width=20)
button3.pack(pady=10)



# Página 4
pagina4 = tk.Frame(root)  # Segunda página (frame)

label4 = tk.Label(pagina4, text="Esta é a Página 4", font=("Arial", 16))
label4.pack(pady=20)

button4 = tk.Button(pagina4, text="Voltar para Página 1", command=voltar_pagina1, width=20)
button4.pack(pady=10)



# Exibindo a página inicial
pagina1.pack(fill="both", expand=True)  # Exibe a primeira página

root.mainloop()
