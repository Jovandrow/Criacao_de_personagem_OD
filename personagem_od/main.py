from racas import Humano, Anao, Elfo
from classes_personagem import Guerreiro, Mago, Clerigo
from personagem import Personagem

def main():
    # Criando personagens de exemplo
    p1 = Personagem("Thorin", Anao(), Guerreiro(), metodo_atributos="classico")
    p2 = Personagem("Elandor", Elfo(), Mago(), metodo_atributos="heroico")
    p3 = Personagem("Marcus", Humano(), Clerigo(), metodo_atributos="aventureiro")

    print(p1)
    print(p2)
    print(p3)

if __name__ == "__main__":
    main()
