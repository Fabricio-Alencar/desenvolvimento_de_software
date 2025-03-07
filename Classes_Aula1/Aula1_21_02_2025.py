class Boneca:
    def __init__(self, nome: str, preco: float, faixa_etaria_cliente: str, tamanho: str, empresa_distribuidora: str, codigo: int):
        self.nome = nome
        self.preco = preco
        self.faixa_etaria_cliente = faixa_etaria_cliente
        self.tamanho = tamanho
        self.empresa_distribuidora = empresa_distribuidora
        self.__codigo = codigo  

    def __str__(self):
        return (
            f"Informações da boneca:\n"
            f"Nome: {self.nome}\n"
            f"Preço: R$ {self.preco:.2f}\n"
            f"Faixa etária dos clientes: {self.faixa_etaria_cliente}\n"
            f"Tamanho: {self.tamanho}\n"
            f"Empresa Distribuidora: {self.empresa_distribuidora}\n"
            f"Código: {self.__codigo}"
        )

if __name__ == "__main__":
    boneca2 = Boneca("Barbie", 100.00, "7 a 10 anos", "19 cm", "Mattel", 1253123462346513)
    print(boneca2)
    print(boneca2.nome)
    #print(boneca2.__codigo)  <-- Esse código dá erro porque o atributo é privado
