#Tainan Diogo Chitolina

print("JOGO DA VELHA")
pontosdojogador1 = 0
pontosdojogador2 = 0
empate = 0
print ()

#Tabuleiro
def jogodavelha():
    tabuleiro = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    fim = False
    vitoria = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)) 

    def desenha(): 
        print(tabuleiro[0],'|',tabuleiro[1],'|',tabuleiro[2])
        print('---------')
        print(tabuleiro[3],'|',tabuleiro[4],'|',tabuleiro[5])
        print('---------')
        print(tabuleiro[6],'|',tabuleiro[7],'|',tabuleiro[8])
        print()

#Jogador 1
    def jogador1(): 
        n = escolha_numero()
        if tabuleiro[n] == 'X' or tabuleiro[n] == 'O':
            print('\nEsta casa já está ocupada. Tente novamente.')
            jogador1()
        else:
            tabuleiro[n] = 'X'

#Jogador 2
    def jogador2(): 
        n = escolha_numero()
        if tabuleiro[n] == 'X' or tabuleiro[n] == 'O':
            print('\nEsta casa já está ocupada. Tente novamente.')
            jogador2()
        else:
            tabuleiro[n] = 'O'

#Escolha da Jogada
    def escolha_numero(): 
        while True:
            while True:
                a = input()
                try:
                    a  = int(a)
                    a -= 1
                    if a in range(0, 9):
                        return a
                    else:
                        print('\nOpção inválida. Tente novamente.')
                        continue
                except ValueError:
                   print('\nOpção inválida. Tente novamente')
                   continue

#Conferindo a vitoria
    def conferindovitoria(): 
        global pontosdojogador1, pontosdojogador2, empate
        count = 0
        for a in vitoria:
            if tabuleiro[a[0]] == tabuleiro[a[1]] == tabuleiro[a[2]] == 'X':
                print(' Parabéns, o jogador1 foi o vencedor\n')
                return True

            if tabuleiro[a[0]] == tabuleiro[a[1]] == tabuleiro[a[2]] == 'O':
                print(' Parabéns, o jogador2 foi o vencedor\n')
                return True

        for a in range(9):
            if tabuleiro[a] == 'X' or tabuleiro[a] == 'O':
                count += 1
            if count == 9:
                print('Empatou.\n')
                empate += 1
                return True

    while not fim:
        desenha()
        fim = conferindovitoria()
        if fim == True:
            break
        print('jogador1 está na sua vez de jogar, escolha uma casa:')
        jogador1()
        print()
        desenha()
        fim = conferindovitoria()
        if fim == True:
            break
        print('jogador2 está na sua vez de jogar, escolha uma casa:')
        jogador2()
        print()


    if input('Você deseja jogar novamente? (s/n)\n') == 's':
        print()
        jogodavelha()
    else:
        print ('Obrigado por jogar')


jogodavelha()