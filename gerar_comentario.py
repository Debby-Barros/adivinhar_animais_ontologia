from gerar_animal import escolher_animal
import streamlit as st

def comentario():
    if escolher_animal().name.lower() == 'leão':
        st.write('''
                    O leão conhecido como o rei da selva e o segundo maior felino do 
                    mundo, habita a Ásia, África e Europa. Vivem em grupos liderados 
                    por um macho alfa e compostos principalmente por fêmeas. Sua 
                    comunicação é feita por rugidos audíveis a até 9 km, usados para 
                    alerta e demarcação de território. Possuem excelente visão noturna 
                    e podem viver até 20 anos e consomem até 30 kg de carne em uma 
                    refeição.
                ''')
        
    elif escolher_animal().name.lower() == 'tubarão tigre':
        st.write('''
                    O tubarão tigre, assim chamado pelas manchas escuras que desaparecem 
                    na fase adulta, tem ampla distribuição no Atlântico Ocidental, 
                    Sudoeste Atlântico e costa de países como Marrocos e Angola. Essa 
                    espécie é conhecida por seu hábito solitário, vivendo nas zonas 
                    pelágicas e caçando sozinha. Surpreendentemente, os tubarões-tigre 
                    podem se alimentar até mesmo de seus próprios filhotes. As orcas 
                    são os únicos animais que representam uma ameaça para eles.
                ''')
        
    elif escolher_animal().name.lower() == 'sapo cururu':
        st.write('''
                    O sapo cururu, nativo das Américas do Sul e Central, é o maior 
                    sapo do planeta. Conhecido por sua toxicidade, seu veneno era 
                    historicamente utilizado pelos índios Choco, no oeste da 
                    Colômbia, para banhar pontas de flechas e dardos de zarabatana. 
                    Quando ameaçados, esses sapos secretam substâncias químicas, 
                    incluindo O-metil-bufotenina, que pode ter efeitos alucinógenos. 
                    Esses sapos têm hábitos terrestres e são noturnos.
                ''')
    
    elif escolher_animal().name.lower() == 'sucuri':
        st.write('''
                    A sucuri, conhecida como "anaconda", é encontrada nas regiões 
                    tropicais da América do Sul, com relatos de avistamentos também 
                    na Flórida. Apesar de não ser venenosa, é perigosa e capaz de 
                    matar suas presas por constrição geralmente caçando próximo à 
                    água. Ao encontrar uma presa, a sucuri envolve seu grande corpo 
                    ao redor dela, aplicando pressão até causar a morte da vítima.
                ''')
        
    elif escolher_animal().name.lower() == 'arara azul':
        st.write('''
                    As araras-azuis são aves sociais que vivem em pares ou em bandos, 
                    encontradas em vastas áreas do Brasil, Bolívia e no Paraguai. 
                    Essas aves se alimentam em grupo, com um indivíduo designado para 
                    vigiar e alertar sobre perigos. São animais monogâmicos, e os 
                    casais compartilham responsabilidades como a reforma do ninho e os 
                    cuidados com os filhotes.
                ''')
        