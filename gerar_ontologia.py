from owlready2 import *
from os import path

_script_local = path.dirname(os.path.realpath(__file__))

# Criar ontologia
onto = get_ontology(f"file://{_script_local}/adivinha_animal.owl")


# Definir classes
class Animal(Thing):
    namespace = onto


class Peixe(Animal):
    namespace = onto


class Anfibio(Animal):
    namespace = onto


class Reptil(Animal):
    namespace = onto


class Mamifero(Animal):
    namespace = onto


class Ave(Animal):
    namespace = onto


class caracFisica(Thing):
    namespace = onto


class Cor(caracFisica):
    namespace = onto


class Habitat(caracFisica):
    namespace = onto


class Pele(caracFisica):
    namespace = onto


class Alimento(caracFisica):
    namespace = onto


# Definir propriedades
class temCor(ObjectProperty):
    namespace = onto
    domain = [Animal]
    range = [Cor]


class viveEm(ObjectProperty):
    namespace = onto
    domain = [Animal]
    range = [Habitat]


class temTipoPele(ObjectProperty):
    namespace = onto
    domain = [Animal]
    range = [Pele]


class seAlimenta(ObjectProperty):
    namespace = onto
    domain = [Animal]
    range = [Alimento]


# adicionar instâncias
animal1 = Mamifero("Leão")
animal1_carac1 = Cor("amarela")
animal1_carac2 = Habitat("selva")
animal1_carac3 = Pele("lisa")
animal1_carac4 = Alimento("roedores, zebras, gnus e carcaças de vários outros animais")

animal2 = Peixe("Tubarão tigre")
animal2_carac1 = Cor("cinza com manchas escuras verticais")
animal2_carac2 = Habitat("oceano")
animal2_carac3 = Pele("áspera recoberta por escamas placoides")
animal2_carac4 = Alimento("lulas, tartarugas, focas e peixes")

animal3 = Anfibio("Sapo cururu")
animal3_carac1 = Cor("marrom em fêmeas, e amarelo-pardo em machos")
animal3_carac2 = Habitat("florestas, lagos, jardins e rios")
animal3_carac3 = Pele("grossa, rugosa e úmida")
animal3_carac4 = Alimento("insetos, camundongos, cobras e caracóis")

animal4 = Reptil("Sucuri")
animal4_carac1 = Cor("verde-oliva com manchas dorsais marrom com bordas pretas")
animal4_carac2 = Habitat("rios, lagos, pântanos e brejos")
animal4_carac3 = Pele("seca e com escamas")
animal4_carac4 = Alimento(
    "tartarugas, jacarés, aves, peixes, capivaras, animais domésticos e até mesmo onças"
)

animal5 = Ave("Arara azul")
animal5_carac1 = Cor(
    "azul cobalto com um anel de cor amarela ao redor dos olhos e na boca"
)
animal5_carac2 = Habitat("florestas úmidas, em árvores como palmeiras e buritizais")
animal5_carac3 = Pele("recoberto de penas")
animal5_carac4 = Alimento(" frutos como: buriti, licuri e macaúba")


# atribuir propriedades
animal1.temCor.append(animal1_carac1)
animal1.viveEm.append(animal1_carac2)
animal1.temTipoPele.append(animal1_carac3)
animal1.seAlimenta.append(animal1_carac4)

animal2.temCor.append(animal2_carac1)
animal2.viveEm.append(animal2_carac2)
animal2.temTipoPele.append(animal2_carac3)
animal2.seAlimenta.append(animal2_carac4)

animal3.temCor.append(animal3_carac1)
animal3.viveEm.append(animal3_carac2)
animal3.temTipoPele.append(animal3_carac3)
animal3.seAlimenta.append(animal3_carac4)

animal4.temCor.append(animal4_carac1)
animal4.viveEm.append(animal4_carac2)
animal4.temTipoPele.append(animal4_carac3)
animal4.seAlimenta.append(animal4_carac4)

animal5.temCor.append(animal5_carac1)
animal5.viveEm.append(animal5_carac2)
animal5.temTipoPele.append(animal5_carac3)
animal5.seAlimenta.append(animal5_carac4)

# salvar a ontologia em um arquivo OWL
onto.save(file=f"{_script_local}/adivinha_animal.owl", format="rdfxml")
