from owlready2 import *
import streamlit as st
from PIL import Image

from gerar_animal import escolher_animal, gerar_descricao, set_trocar_animal


animal_aleatorio = escolher_animal()


def adivinhe():
    global animal_aleatorio
    # Front com Streamlit
    st.title("Adivinhe o animal!")

    st.write(gerar_descricao(animal_aleatorio))

    if st.button("Alterar animal"):
        set_trocar_animal(True)

    # input do usuário
    resp_usuario = st.text_input("Qual é o animal?")

    if st.button("Verificar"):
        if resp_usuario.strip():
            if resp_usuario.lower() == animal_aleatorio.name.lower():
                st.success("Parabéns!! Você acertou!")

                # Adicionar ft do animal
                tamanho_redimensionado = (300, 300)
                imagem = Image.open(f"img/{animal_aleatorio.name.lower()}.jpg")
                img_redim = imagem.resize(tamanho_redimensionado)
                st.image(img_redim, caption=animal_aleatorio.name)

            else:
                st.error(f"Uepa! tá errado amigão, tente novamente!!")

        else:
            st.warning("Por favor, insira uma resposta antes de verificar.")

    if st.button("Desistir"):
        st.error(f"A resposta correta era: {animal_aleatorio.name}")


# Função principal do aplicativo Streamlit
def main():
    adivinhe()


if __name__ == "__main__":
    main()
