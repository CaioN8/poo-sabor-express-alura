from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio


class Restaurante:
    """Representa um restaurante e suas características"""

    restaurantes = []

    def __init__(self, nome, categoria):
        """
        Inicialização de uma instância de Restaurante

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.
        """

        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._avaliacao = []
        self._cardapio = []
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        """Representação em string das informações da instância do restaurante"""
        return f"{self.nome} | {self.categoria}"
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def categoria(self):
        return self._categoria
        
    @classmethod
    def listar_restaurantes(cls):
        """Exibe uma lista formatada de todos os restaurantes cadastrados"""
        print(f"{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} | {"Status".ljust(25)}")
        for restaurante in cls.restaurantes:
            print(f"{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo.ljust(25)}")

    @property
    def ativo(self):
        """Retorna um símbolo apresentando o estado de atividade do restaurante"""
        return "▣" if self._ativo else "▢"
    
    def alternar_estado(self):
        """Alterna o estado de atividade do restaurante"""
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        """
        Registra as avaliações para o restaurante.

        Parâmetros:
        - cliente (str): O nome do cliente que está avaliando.
        - nota (float): A nota dada pelo cliente (entre 1 e 5)
        """
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        """Calcula e retorna a média de avaliações do restaurante"""
        if not self._avaliacao:
            return "Nenhuma avaliação"
        soma_avaliacoes = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = round(soma_avaliacoes / quantidade_notas, 1)
        return media
    
    
    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f"Cardápio do Restaurante {self._nome}\n")
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, "descricao"):
                mensagem_prato = f"{i}. {item._nome} | Preço: R$ {item._preco} | Descrição: {item._descricao}"
                print(mensagem_prato)
            else:
                mensagem_bebida = f"{i}. {item._nome} | Preço: R$ {item._preco} | Tamanho: {item._tamanho}"
                print(mensagem_bebida)
        