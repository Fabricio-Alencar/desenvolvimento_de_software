import tkinter as tk

# Classe que gerencia o sistema de gestão
class SistemaGestaoGenerico:
    def __init__(self, master):  # Método construtor que inicializa a interface gráfica.
        self.root = master  # Armazena a referência da janela principal.
        self.root.title("Twice")  # Define o título da janela principal.
        self.root.geometry('600x600')  # Define o tamanho da janela principal.

        # Lista de integrantes do Twice em ordem de idade (do mais velho para o mais novo)
        integrantes = [
            ("Im Nayeon", "#5BC2E7"),  # Cor personalizada para o primeiro botão
            ("Yoo Jeongyeon", "#C5D97A"),
            ("Hirai Momo", "#FF8DA1"),
            ("Minatozaki Sana", "#9B7DD4"),
            ("Park Jihyo", "#FFC56E"),
            ("Myoui Mina", "#6DCDB8"),
            ("Kim Dahyun", "#FFFFFF"),
            ("Son Chaeyoung", "#EE2737"),
            ("Chou Tzuyu", "#005EB8")
        ]
        # Criando 9 botões em um layout 3x3
        for i, (nome, cor) in enumerate(integrantes):
            row = i // 3  # Determina a linha (divisão inteira por 3)
            col = i % 3   # Determina a coluna (resto da divisão por 3)
            button = tk.Button(self.root, text=nome, width=20, height=5, bg=cor)  # Criando o botão com a cor e o nome
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")  # Colocando o botão no grid

        # Ajustando a expansão das linhas e colunas para preencher o espaço disponível
        for i in range(3):
            self.root.grid_rowconfigure(i, weight=1)  # Faz com que as linhas se expandam igualmente
            self.root.grid_columnconfigure(i, weight=1)  # Faz com que as colunas se expandam igualmente

# Criando a janela principal
root = tk.Tk()
app = SistemaGestaoGenerico(root)
root.mainloop()
