import random
from enum import Enum
from typing import List

#Enum pra guardar informações de escolha , typing para definir saidas e random para números aletórios.

#Definindo as cores da roleta
class CorRoleta(Enum):
     VERMELHO = "Vermelho"
     PRETO = "Preto"
     ZERO = "Zero" #Vitória da casa!


#Criando uma lista de números da roleta com pares!
def criarRoleta() -> List[tuple]:
    roleta = [] #A lista vazia para iterações
    for numero in range(37): #Número de 0 a 36
         if numero == 0:
              roleta.append((numero, CorRoleta.ZERO)) #Vitória da casa
         elif numero % 2 == 0:
              roleta.append((numero, CorRoleta.PRETO)) #Números pares
         else:
              roleta.append((numero, CorRoleta.VERMELHO)) #Números ímpares
    return roleta #Se for preciso usar a classe basta chamar o return 'roleta'
    
def sortear_numero(roleta: List[tuple]) -> tuple: #Função que sorteia os números
     return random.choice(roleta)   

#Função principal - Criando o jogo

def jogar_roleta():
    roleta = criarRoleta()
    
    print("Welcome to the rollet game of Mighty King Dice hahaha >:) ") #Saudação do bot
    print("Make your bet!")
    print("Type '1' for bet a number (0-36)")
    print("type 2 for choose a color (VERMELHO or PRETO)")

    opcao = int(input("Choose a lucky number (or not hahahaha)"))

    if opcao == 1:
        numero_aposta = int(input("Type the bet number! "))
        if numero_aposta < 0 or numero_aposta > 36:
            print("Ops.. try again >:) ")
            return
    elif opcao == 2:
        cor_aposta = input("Select a color").strip().capitalize()
        if cor_aposta not in [cor.value for cor in CorRoleta]:
            print("Wrong color! Choose another. ")
            return
    else:
        print("Type 1 or 2 for play. ")
        return
    
    #Sorteando o numero
    numero_sorteado, cor_sorteada = sortear_numero(roleta)
    print(f"\nNumero Sorteado: {numero_sorteado} ({cor_sorteada})")

    #Win ou lose
    if opcao == 1:
        if numero_aposta == numero_sorteado:
            print("I can believe... you win >:( I'll set your soul free... )")
        else:
            print("Hahahaha, you lose! ")
    elif opcao == 2:
        if cor_aposta == cor_sorteada.value:
            print("I can believe... you win >:( I'll set your soul free... ")
        else:
            print("Hahahaha, you lose!")

if __name__ == "__main__":
    jogar_roleta()