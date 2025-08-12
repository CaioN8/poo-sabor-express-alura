from modelos.restaurante import Restaurante

restaurante_praca = Restaurante("Praça", "Gourmet")
restaurante_pizza = Restaurante("Pizza Express", "Italiana")
restaurante_praca.alternar_estado()
restaurante_praca.receber_avaliacao("Robert", 4)
restaurante_praca.receber_avaliacao("Steve", 4.5)
restaurante_praca.receber_avaliacao("Natasha", 2.5)


def main():
    Restaurante.listar_restaurantes()


if __name__ == "__main__":
    main()