class ClassePersonagem:
    """Classe base para classes de personagem"""

    def __init__(self, nome, dado_vida, habilidades):
        self.nome = nome
        self.dado_vida = dado_vida
        self.habilidades = habilidades

    def __str__(self):
        return (f"Classe: {self.nome}\n"
                f"Dado de Vida: d{self.dado_vida}\n"
                f"Habilidades: {', '.join(self.habilidades)}")


class Guerreiro(ClassePersonagem):
    def __init__(self):
        super().__init__("Guerreiro", dado_vida=10, habilidades=[
            "Especialização em armas", "Ataque extra conforme nível"
        ])


class Mago(ClassePersonagem):
    def __init__(self):
        super().__init__("Mago", dado_vida=4, habilidades=[
            "Uso de magia arcana", "Pouca proficiência em armas"
        ])


class Clerigo(ClassePersonagem):
    def __init__(self):
        super().__init__("Clérigo", dado_vida=8, habilidades=[
            "Magias divinas", "Expulsar mortos-vivos"
        ])
