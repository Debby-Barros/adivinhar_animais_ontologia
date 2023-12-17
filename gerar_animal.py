from owlready2 import *
import random
from os import path

trocar_animal = True
current_animal = None

_script_local = path.dirname(os.path.realpath(__file__))

# Lê ontologia
onto = get_ontology(f"file://{_script_local}/adivinha_animal.owl").load()


def escolher_animal():
    global current_animal, trocar_animal
    
    if not current_animal or trocar_animal:
        current_animal = random.choice(list(onto.Animal.instances()))
        trocar_animal = False
        return current_animal
    else:
        return current_animal


def gerar_descricao(animal):
    # mostrar as características para o usuário
    cor_animal = sorted(set(cor.name for cor in animal.temCor))
    habitat_animal = sorted(set(habitat.name for habitat in animal.viveEm))
    pele_animal = sorted(set(pele.name for pele in animal.temTipoPele))
    alimentacao_animal = sorted(
        set(alimentacao.name for alimentacao in animal.seAlimenta)
    )

    return "Possuo uma cor {}, meu habitat é {}. Tenho a pele {} e minha alimentação consiste de {}. Que animal eu sou? ".format(
        ", ".join(cor_animal),
        ", ".join(habitat_animal),
        ", ".join(pele_animal),
        ", ".join(alimentacao_animal),
    )


def set_trocar_animal(value: bool):
    global trocar_animal
    trocar_animal = value
