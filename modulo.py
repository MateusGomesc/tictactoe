from os import system
import emoji

def cabeçalho():
    """
        função sem parâmetro
        return: sem retorno
    """

    print('*'*34)
    print('*  \033[33mJOGO DA VELHA\033[m         V.1.0  *')
    print('*'*34)
    print('\n')

def tabuleiro(casas):
    """
        função do tabuleiro do jogo
        param casas: recebe matriz 3x3
        return: sem retorno
    """
    print('     \033[35m1   2   3\033[m')
    print(f' \033[36m1\033[m   {casas[0][0]}  |  {casas[0][1]}  |  {casas[0][2]}  ')
    print('     -', end='') 
    print('-'*10)
    print(f' \033[36m2\033[m   {casas[1][0]}  |  {casas[1][1]}  |  {casas[1][2]}  ')
    print('     -', end='')
    print('-'*10)
    print(f' \033[36m3\033[m   {casas[2][0]}  |  {casas[2][1]}  |  {casas[2][2]}  ')

def readstr(msg):
    """
        Função para ler string
        param msg: recebe mensagem para input
        return: retorna a string sem erros
    """

    while True: 
        try:
            resposta = str(input(msg)).strip().lower()
        except:
            system('cls')
            cabeçalho()
            print('\033[31mDIGITO INVALIDO, tente novamente!\033[m')
            continue
        else:
            if resposta.isalpha() == False or resposta == '':
                system('cls')
                cabeçalho()
                print('\033[31mDIGITO INVALIDO, tente novamente!\033[m')
                continue
            elif resposta != 'sim' and resposta != 'não' and resposta != 'nao':
                system('cls')
                cabeçalho()
                print('\033[31mRESPOSTA INVALIDA, tente novamente!\033[m')
                continue                
            else:
                return resposta

def readline(msg):
    """
        função para verficar escolha das casas
        param msg: recebe mensagem para input
        return: posição da casa sem erros
    """

    while True:
        try:
            linha = int(input(msg))
        except: 
            print('\033[31mDIGITO INVALIDO, tente novamente!\033[m')
            continue
        else:
            if linha < 1 or linha > 3:
                print('\033[31mNUMERO FORA DO INTERVALO, tente novamente!\033[m')   
                continue
            else:
                return linha    

def readcolumn(msg):
    """
        função para verficar escolha das casas
        param msg: recebe mensagem para input
        return: posição da casa sem erros
    """

    while True:
        try:
            coluna = int(input(msg))
        except: 
            print('\033[31mDIGITO INVALIDO, tente novamente!\033[m')
            continue
        else:
            if coluna < 1 or coluna > 3:
                print('\033[31mNUMERO FORA DO INTERVALO, tente novamente!\033[m')   
                continue
            else:
                return coluna

def ganhou(nome):
    print('\n\033[33m*\033[m    -------  \033[33m*\033[m  ')
    print('   \033[33m*\033[m |     |    \033[33m*\033[m')
    print(' \033[33m*\033[m   \     / \033[33m*\033[m   ')
    print('  \033[33m*\033[m   |   |   \033[33m*\033[m ')
    print(' \033[33m*\033[m    |   |  \033[33m*\033[m  ')
    print('   \033[33m*\033[m /     \    \033[33m*\033[m ')
    print('     -------     ')    
    print(emoji.emojize(f'{nome} GANHOU!:sunglasses:', language = 'alias'))

def empate():
    print('\033[33m *         *     \033[m')
    print('\033[33m      *       *  \033[m')
    print(emoji.emojize('  \033[33m*\033[m  EMPATOU:+1:   \033[33m*', language = 'alias'))
    print('\033[33m *          *    \033[m')
    print('\033[33m     *       *   \033[m') 

def regras():
    print(emoji.emojize('Olá \033[32mjogadores\033[m:smile:, este é o famoso jogo da velha, onde o objeto é cruzar os três simbolos iguais.', language = 'alias'))
    print('Aqui neste jogo você irá nos informar a \033[36mlinha\033[m e a \033[35mcoluna\033[m da posição desejada.')
    print(emoji.emojize('\033[32mVAMOS JOGAR!:muscle:\033[m', language = 'alias'))      