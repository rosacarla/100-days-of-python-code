#Exemplo de função que retorna uma string diferente para cada nº informado
#uso do RETURN

import random
def darResposta(respostaNro):
    if respostaNro == 1:
        return "É certo"
    elif respostaNro == 2:
        return "É decididamente"
    elif respostaNro == 3:
        return "Sim"
    elif respostaNro == 4:
        return "Repita, tente de novo"
    elif respostaNro == 5:
        return "Pergunte de novo mais tarde"
    elif respostaNro == 6:
        return "Concentre-se e pergunte de novo"
    elif respostaNro == 7:
        return "Minha resposta é não"
    elif respostaNro == 8:
        return "Visão não tão boa"
    elif respostaNro == 9:
        return "Muito duvidoso"

r = random.randint(1, 9)
fortuna = darResposta(r)
print(fortuna)

    
    
