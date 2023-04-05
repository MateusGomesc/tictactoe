from os import system
import modulo as mdl
from pygame import mixer, init

# Apresentação
mdl.cabeçalho()
mdl.regras()
print('\nDigite ENTER para começar: ')
iniciar = ' '

while iniciar != '':
    iniciar = input()

# Começo do jogo
resposta = 'sim'

while resposta == 'sim':
    system('cls')
    jogadas = 1
    vez = 0
    casas = [['', '', ''], ['', '', ''], ['', '', '']]

    # Nome dos jogadores
    mdl.cabeçalho()
    nick1 = str(input('Nome do jogador 1: '))
    nick2 = str(input('Nome do jogador 2: '))

    while jogadas <=9:
        system('cls')
        mdl.tabuleiro(casas)

        if vez % 2 == 0:
            # Entrada das posições jogador 1
            print(f'\nVez de {nick1}:')
            while True:
                linha = mdl.readline('Digite a \033[36mlinha\033[m: ')
                coluna = mdl.readcolumn('Digite a \033[35mcoluna\033[m: ')
            
                # Salva na matriz
                if casas[linha-1][coluna-1] != 'X' and casas[linha-1][coluna-1] != 'O':
                    casas[linha-1][coluna-1] = 'X'
                    break
                else:
                    print('\033[31mPOSIÇÃO OCUPADA, tente novamente\033[m')
            
            # Incrementa jogada e vez
            jogadas += 1
            vez += 1
        else: 
            # Entrada das posições jogador 2
            print(f'\nVez de {nick2}:')
            while True:
                linha = mdl.readline('Digite a \033[36mlinha\033[m: ')
                coluna = mdl.readcolumn('Digite a \033[35mcoluna\033[m: ')
            
                # Salva na matriz
                if casas[linha-1][coluna-1] != 'X' and casas[linha-1][coluna-1] != 'O':
                    casas[linha-1][coluna-1] = 'O'
                    break
                else:
                    print('\033[31mPOSIÇÃO OCUPADA, tente novamente\033[m')
            
            # Incrementa jogada e vez
            jogadas += 1
            vez += 1
        
        # Condições de vitoria jogador 1
        if casas[0][0] == 'X' and casas[0][1] == 'X' and casas[0][2] == 'X':
            jogadas = 11 
        if casas[1][0] == 'X' and casas[1][1] == 'X' and casas[1][2] == 'X':
            jogadas = 11 
        if casas[2][0] == 'X' and casas[2][1] == 'X' and casas[2][2] == 'X':
            jogadas = 11 
        if casas[0][0] == 'X' and casas[1][0] == 'X' and casas[2][0] == 'X':
            jogadas = 11 
        if casas[0][1] == 'X' and casas[1][1] == 'X' and casas[2][1] == 'X':
            jogadas = 11 
        if casas[0][2] == 'X' and casas[1][2] == 'X' and casas[2][2] == 'X':
            jogadas = 11  
        if casas[0][0] == 'X' and casas[1][1] == 'X' and casas[2][2] == 'X':
            jogadas = 11     
        if casas[0][2] == 'X' and casas[1][1] == 'X' and casas[2][0] == 'X':
            jogadas = 11  

        # Condições de vitoria jogador 2 
        if casas[0][0] == 'O' and casas[0][1] == 'O' and casas[0][2] == 'O':
            jogadas = 12
        if casas[1][0] == 'O' and casas[1][1] == 'O' and casas[1][2] == 'O':
            jogadas = 12
        if casas[2][0] == 'O' and casas[2][1] == 'O' and casas[2][2] == 'O':
            jogadas = 12 
        if casas[0][0] == 'O' and casas[1][0] == 'O' and casas[2][0] == 'O':
            jogadas = 12 
        if casas[0][1] == 'O' and casas[1][1] == 'O' and casas[2][1] == 'O':
            jogadas = 12 
        if casas[0][2] == 'O' and casas[1][2] == 'O' and casas[2][2] == 'O':
            jogadas = 12  
        if casas[0][0] == 'O' and casas[1][1] == 'O' and casas[2][2] == 'O':
            jogadas = 12     
        if casas[0][2] == 'O' and casas[1][1] == 'O' and casas[2][0] == 'O':
            jogadas = 12 
    
    system('cls')

    # Resultados
    if jogadas == 10:
        mdl.empate()
        init()
        mixer.music.load('ganhou.mp3')
        mixer.music.play(loops=0,start=0.0) 
    if jogadas == 11:
        mdl.ganhou(nick1)
        init()
        mixer.music.load('ganhou.mp3')
        mixer.music.play(loops=0,start=0.0)    
    if jogadas == 12:
        mdl.ganhou(nick2)
        init()
        mixer.music.load('ganhou.mp3')
        mixer.music.play(loops=0,start=0.0)

    resposta = mdl.readstr('\nVocê quer jogar novamente? [Sim / Não]: ')