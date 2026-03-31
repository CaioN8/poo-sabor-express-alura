from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.sobremesa import Sobremesa


restaurante_praca = Restaurante("Praça", "Gourmet")
restaurante_pizza = Restaurante("Pizza Express", "Italiana")
restaurante_praca.alternar_estado()

bebida_suco = Bebida("Suco de laranja", 5.00, "grande")
bebida_suco.aplicar_desconto()
prato_macarronada = Prato("Macarronada", 20.00, "Experimente a melhor massa italiana da região.")
prato_macarronada.aplicar_desconto()
sobremesa_pudim = Sobremesa("Pudim", 15.00, "doce", "grande", "Eu gosto de pudim!")
sobremesa_pudim.aplicar_desconto()

restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_macarronada)
restaurante_praca.adicionar_no_cardapio(sobremesa_pudim)

def main():
    restaurante_praca.exibir_cardapio


if __name__ == "__main__":
    main()