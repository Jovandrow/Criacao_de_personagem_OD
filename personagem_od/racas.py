class Raca:
    """Classe base para Raças"""

    def __init__(self, nome, movimento, infravisao, alinhamento):
        self.nome = nome
        self.movimento = movimento
        self.infravisao = infravisao
        self.alinhamento = alinhamento
        self.habilidades = []

    def __str__(self):
        return (f"Raça: {self.nome}\n"
                f"Movimento: {self.movimento}\n"
                f"Infravisão: {self.infravisao}\n"
                f"Alinhamento: {self.alinhamento}\n"
                f"Habilidades: {', '.join(self.habilidades)}")


class Humano(Raca):
    def __init__(self):
        super().__init__("Humano", movimento=9, infravisao="Não possui", alinhamento="Qualquer")
        self.habilidades = ["Versatilidade: recebe 1 talento extra"]


class Anao(Raca):
    def __init__(self):
        super().__init__("Anão", movimento=6, infravisao="18m", alinhamento="Leal ou Neutro")
        self.habilidades = ["Resistência a venenos", "Infravisão aprimorada"]


class Elfo(Raca):
    def __init__(self):
        super().__init__("Elfo", movimento=12, infravisao="9m", alinhamento="Neutro ou Caótico")
        self.habilidades = ["Sentidos aguçados", "Afinidade com magia"]
