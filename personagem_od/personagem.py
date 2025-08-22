from atributos import Atributos

class Personagem:
    """Classe principal de um personagem"""

    def __init__(self, nome, raca, classe, metodo_atributos="classico"):
        self.nome = nome
        self.raca = raca
        self.classe = classe
        self.atributos = Atributos()

        if metodo_atributos == "classico":
            self.atributos.distribuir_classico()
        elif metodo_atributos == "heroico":
            self.atributos.distribuir_heroico()
        elif metodo_atributos == "aventureiro":
            self.atributos.distribuir_aventureiro()

    def __str__(self):
        return (f"===== {self.nome} =====\n"
                f"{self.raca}\n\n"
                f"{self.classe}\n\n"
                f"Atributos:\n{self.atributos}\n")
