import tkinter as tk

r = tk.Tk()
r.title('Counting Seconds')
r.geometry("400x300")  # Define o tamanho da janela (Largura x Altura)

w = tk.Label(r, text='GeeksForGeeks.org!') # Cria uma "etiqueta", Label indica que vai ser um texto
w.pack(pady=20)  # Adiciona a etiqueta e um espaçamento vertical de 20 pixels


button = tk.Button(r, text='Professor', width=20, height=2, command=r.destroy,
                   relief="flat",  # Remove a borda padrão
                   fg="white",  # Cor do texto
                   bg="#4CAF50",  # Cor de fundo do botão
                   font=("Arial", 14, "bold"))
button.pack(pady=20)

button = tk.Button(r, text='Professor', width=20, command=r.destroy)
button.pack(pady=20)

button = tk.Button(r, text='Professor', width=20, command=r.destroy)
button.pack(pady=20)


r.mainloop()
