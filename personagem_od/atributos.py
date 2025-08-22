import random

class Atributos:
    """Representa os atributos principais de um personagem"""

    NOMES = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]

    def __init__(self):
        self.valores = {nome: 0 for nome in self.NOMES}

    def distribuir_classico(self):
        """Rolagem clássica: 3d6 para cada atributo"""
        for nome in self.NOMES:
            self.valores[nome] = sum(random.randint(1, 6) for _ in range(3))

    def distribuir_heroico(self):
        """Rolagem heróica: 4d6 descartando o menor"""
        for nome in self.NOMES:
            rolagens = [random.randint(1, 6) for _ in range(4)]
            rolagens.remove(min(rolagens))
            self.valores[nome] = sum(rolagens)

    def distribuir_aventureiro(self):
        """Rolagem aventureiro: 12, 13, 14, 15, 16, 17 distribuídos manualmente"""
        valores_fixos = [12, 13, 14, 15, 16, 17]
        random.shuffle(valores_fixos)
        for i, nome in enumerate(self.NOMES):
            self.valores[nome] = valores_fixos[i]

    def __str__(self):
        return "\n".join([f"{nome}: {valor}" for nome, valor in self.valores.items()])
