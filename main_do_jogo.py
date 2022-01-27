import os

#função de criação do novo player
#essa função cria um arquivo .txt com o nome selecionado que armazena sua pontuação de vitórias e derrotas
def create_new_player():
    nome = input("Digite o nome do novo player: ")
    #verificando se o arquivo já foi criado
    if os.path.isfile("{}.txt".format(nome)):
        print("Player já registrado.")
        print("")
    else:
        print("Registrando novo player {}\n" .format(nome))
        archive = open("{}.txt" .format(nome), "w")
        archive.write("0\n")
        #pontuação de vitórias
        archive.write("0")
        #pontuação das derrotas
        archive.close()   

#função de excluir um player
#essa função apaga um arquivo .txt contendo a pontuação de algum player
def erase_existing_player():
    nome = input("Digite o nome do player que deseja apagar: ")
    #verificando a existência do arquivo
    if os.path.isfile("{}.txt" .format(nome)):
        print("Excluindo player {}\n" .format(nome))
        print("")
        os.remove("{}.txt" .format(nome))
    else:
        print("Player não existente")
        print("")

#função de ler a pontuação
def read_score():
    nome = input("Digite o nome do player: ")
    if os.path.isfile("{}.txt" .format(nome)):
        p = open("{}.txt" .format(nome), "r")
        print("Pontuação de {}: " .format(nome))
        h = p.readlines()
        #pegando as linhas para leitura
        w = h[0]
        l = h[1]
        print("Vitórias: {}\nDerrotas : {}" .format(w,l))
        print("")
    else:
        print("Player não existente")
        print("")

#iniciando o jogo
def funcao_do_game():
    #desenhando a matriz
    matrix = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ']
        ]
    
    #imprimindo o tabuleiro
    def imprimindo_o_game():
        tabuleiro = """
         {} | {} | {} | {} | {}   
        ---+---+---+---+---
         {} | {} | {} | {} | {} 
        ---+---+---+---+---
         {} | {} | {} | {} | {} 
        ---+---+---+---+---
         {} | {} | {} | {} | {} 
        ---+---+---+---+---
         {} | {} | {} | {} | {}         
        """.format(matrix[0][0], matrix[0][1], matrix[0][2], matrix[0][3], matrix[0][4], 
                    matrix[1][0], matrix[1][1], matrix[1][2], matrix[1][3], matrix[1][4],
                    matrix[2][0], matrix[2][1], matrix[2][2], matrix[2][3], matrix[2][4],
                    matrix[3][0], matrix[3][1], matrix[3][2], matrix[3][3], matrix[3][4],
                    matrix[4][0], matrix[4][1], matrix[4][2], matrix[4][3], matrix[4][4])
        print(tabuleiro)

    #função da vitória do player 1, X
    #essa função é executada caso a a condição da vitória seja verdadeira, e adiciona a vitória e a derrota nos respectivos players
    def victory_player1():
        a = open("{}.txt" .format(p1), "r")
        h = a.readlines()
        a.close()
        w = int(h[0]) + 1
        l = int(h[1]) + 0
        a = open("{}.txt" .format(p1), "w")
        a.write("{}\n{}".format(w,l))
        a.close()
        #derrota do p2
        b = open("{}.txt" .format(p2), "r")
        h = b.readlines()
        a.close()
        w = int(h[0]) + 0
        l = int(h[1]) + 1
        b = open("{}.txt" .format(p2), "w")
        b.write("{}\n{}".format(w,l))
        b.close()                    
        print("Player 1, {} ganhou!" .format(p1))
        print("Acesse seu placar no menu para ver sua pontuação")

    #função da vitória player 2, O
    #essa função é executada caso a a condição da vitória seja verdadeira, e adiciona a vitória e a derrota nos respectivos players
    def victory_player2():
        a = open("{}.txt" .format(p2), "r")
        h = a.readlines()
        a.close()
        w = int(h[0]) + 1
        l = int(h[1]) + 0
        a = open("{}.txt" .format(p2), "w")
        a.write("{}\n{}".format(w,l))
        a.close()
        #derrota do p1
        b = open("{}.txt" .format(p1), "r")
        h = b.readlines()
        a.close()
        w = int(h[0]) + 0
        l = int(h[1]) + 1
        b = open("{}.txt" .format(p1), "w")
        b.write("{}\n{}".format(w,l))
        b.close()                    
        print("Player 2, {} ganhou!" .format(p2))
        print("Acesse seu placar no menu para ver sua pontuação")

    def victory_detection():
        #estabelecendo as condições da vitória 
        #as condições vão ser testadas toda vez que o player fizer uma jogada, caso seja verdadeira, vitória
        #condições horizontais de "X"
        if matrix[0][0]=="X" and matrix[0][1]=="X" and matrix[0][2]=="X" and matrix[0][3]=="X":
            return True
        elif matrix[0][1]=="X" and matrix[0][2]=="X" and matrix[0][3]=="X" and matrix[0][4]=="X":
            return True
        elif matrix[1][0]=="X" and matrix[1][1]=="X" and matrix[1][2]=="X" and matrix[1][3]=="X":
            return True
        elif matrix[1][1]=="X" and matrix[1][2]=="X" and matrix[1][3]=="X" and matrix[1][4]=="X":
            return True
        elif matrix[2][0]=="X" and matrix[2][1]=="X" and matrix[2][2]=="X" and matrix[2][3]=="X":
            return True
        elif matrix[2][1]=="X" and matrix[2][2]=="X" and matrix[2][3]=="X" and matrix[2][4]=="X":
            return True
        elif matrix[3][0]=="X" and matrix[3][1]=="X" and matrix[3][2]=="X" and matrix[3][3]=="X":
            return True
        elif matrix[3][1]=="X" and matrix[3][2]=="X" and matrix[3][3]=="X" and matrix[3][4]=="X":
            return True
        elif matrix[4][0]=="X" and matrix[4][1]=="X" and matrix[4][2]=="X" and matrix[4][3]=="X":
            return True
        elif matrix[4][1]=="X" and matrix[4][2]=="X" and matrix[4][3]=="X" and matrix[4][4]=="X":
            return True

        #verificando horizontalmente para O
        elif matrix[0][0]=="O" and matrix[0][1]=="O" and matrix[0][2]=="O" and matrix[0][3]=="O":
            return True
        elif matrix[0][1]=="O" and matrix[0][2]=="O" and matrix[0][3]=="O" and matrix[0][4]=="O":
            return True
        elif matrix[1][0]=="O" and matrix[1][1]=="O" and matrix[1][2]=="O" and matrix[1][3]=="O":
            return True
        elif matrix[1][1]=="O" and matrix[1][2]=="O" and matrix[1][3]=="O" and matrix[1][4]=="O":
            return True
        elif matrix[2][0]=="O" and matrix[2][1]=="O" and matrix[2][2]=="O" and matrix[2][3]=="O":
            return True
        elif matrix[2][1]=="O" and matrix[2][2]=="O" and matrix[2][3]=="O" and matrix[2][4]=="O":
            return True
        elif matrix[3][0]=="O" and matrix[3][1]=="O" and matrix[3][2]=="O" and matrix[3][3]=="O":
            return True
        elif matrix[3][1]=="O" and matrix[3][2]=="O" and matrix[3][3]=="O" and matrix[3][4]=="O":
            return True
        elif matrix[4][0]=="O" and matrix[4][1]=="O" and matrix[4][2]=="O" and matrix[4][3]=="O":
            return True
        elif matrix[4][1]=="O" and matrix[4][2]=="O" and matrix[4][3]=="O" and matrix[4][4]=="O":
            return True

        #checando verticalmente para X
        elif matrix[0][0]=="X" and matrix[1][0]=="X" and matrix[2][0]=="X" and matrix[3][0]=="X":
            return True
        elif matrix[0][1]=="X" and matrix[1][1]=="X" and matrix[2][1]=="X" and matrix[3][1]=="X":
            return True
        elif matrix[1][1]=="X" and matrix[2][1]=="X" and matrix[3][1]=="X" and matrix[4][1]=="X":
            return True
        elif matrix[0][2]=="X" and matrix[1][2]=="X" and matrix[2][2]=="X" and matrix[3][2]=="X":
            return True
        elif matrix[1][2]=="X" and matrix[2][2]=="X" and matrix[3][2]=="X" and matrix[4][2]=="X":
            return True
        elif matrix[0][3]=="X" and matrix[1][3]=="X" and matrix[2][3]=="X" and matrix[3][3]=="X":
            return True
        elif matrix[1][3]=="X" and matrix[2][3]=="X" and matrix[3][3]=="X" and matrix[4][3]=="X":
            return True
        elif matrix[0][4]=="X" and matrix[1][4]=="X" and matrix[2][4]=="X" and matrix[3][4]=="X":
            return True
        elif matrix[1][4]=="X" and matrix[2][4]=="X" and matrix[3][4]=="X" and matrix[4][4]=="X":
            return True

        #verificando verticalmente para O
        elif matrix[0][0]=="O" and matrix[1][0]=="O" and matrix[2][0]=="O" and matrix[3][0]=="O":
            return True
        elif matrix[0][1]=="O" and matrix[1][1]=="O" and matrix[2][1]=="O" and matrix[3][1]=="O":
            return True
        elif matrix[1][1]=="O" and matrix[2][1]=="O" and matrix[3][1]=="O" and matrix[4][1]=="O":
            return True
        elif matrix[0][2]=="O" and matrix[1][2]=="O" and matrix[2][2]=="O" and matrix[3][2]=="O":
            return True
        elif matrix[1][2]=="O" and matrix[2][2]=="O" and matrix[3][2]=="O" and matrix[4][2]=="O":
            return True
        elif matrix[0][3]=="O" and matrix[1][3]=="O" and matrix[2][3]=="O" and matrix[3][3]=="O":
            return True
        elif matrix[1][3]=="O" and matrix[2][3]=="O" and matrix[3][3]=="O" and matrix[4][3]=="O":
            return True
        elif matrix[0][4]=="O" and matrix[1][4]=="O" and matrix[2][4]=="O" and matrix[3][4]=="O":
            return True
        elif matrix[1][4]=="O" and matrix[2][4]=="O" and matrix[3][4]=="O" and matrix[4][4]=="O":
            return True

        #verificando diagonais para X
        elif matrix[0][0]=="X" and matrix[1][1]=="X" and matrix[2][2]=="X" and matrix[3][3]=="X":
            return True
        elif matrix[1][1]=="X" and matrix[2][2]=="X" and matrix[3][3]=="X" and matrix[4][4]=="X":
            return True
        elif matrix[0][1]=="X" and matrix[1][2]=="X" and matrix[2][3]=="X" and matrix[3][4]=="X":
            return True
        elif matrix[0][4]=="X" and matrix[1][3]=="X" and matrix[2][2]=="X" and matrix[3][1]=="X":
            return True
        elif matrix[1][0]=="X" and matrix[2][1]=="X" and matrix[3][2]=="X" and matrix[4][3]=="X":
            return True
        elif matrix[1][3]=="X" and matrix[2][2]=="X" and matrix[3][1]=="X" and matrix[4][0]=="X":
            return True
        elif matrix[0][3]=="X" and matrix[1][2]=="X" and matrix[2][1]=="X" and matrix[3][0]=="X":
            return True
        elif matrix[1][4]=="X" and matrix[2][3]=="X" and matrix[3][2]=="X" and matrix[4][1]=="X":
            return True

        #verificando diagonais para O
        elif matrix[0][0]=="O" and matrix[1][1]=="O" and matrix[2][2]=="O" and matrix[3][3]=="O":
            return True
        elif matrix[1][1]=="O" and matrix[2][2]=="O" and matrix[3][3]=="O" and matrix[4][4]=="O":
            return True
        elif matrix[0][1]=="O" and matrix[1][2]=="O" and matrix[2][3]=="O" and matrix[3][4]=="O":
            return True
        elif matrix[0][4]=="O" and matrix[1][3]=="O" and matrix[2][2]=="O" and matrix[3][1]=="O":
            return True
        elif matrix[1][0]=="O" and matrix[2][1]=="O" and matrix[3][2]=="O" and matrix[4][3]=="O":
            return True
        elif matrix[1][3]=="O" and matrix[2][2]=="O" and matrix[3][1]=="O" and matrix[4][0]=="O":
            return True
        elif matrix[0][3]=="O" and matrix[1][2]=="O" and matrix[2][1]=="O" and matrix[3][0]=="O":
            return True
        elif matrix[1][4]=="O" and matrix[2][3]=="O" and matrix[3][2]=="O" and matrix[4][1]=="O":
            return True

        else:
            return False

    p1 = input("Digite o nome do player 1: ") 
    p2 = input("Digite o nome do player 2: ")   

    print("Player 1 {} será os X e player 2 {} será o O" .format(p1, p2))
    print("Os X começaram agora")
    imprimindo_o_game()

    jogadas = 0
    counter = 0
    #fazendo a função do jogo
    while jogadas <= 24:
        l = " "
        c = " "
        #um booleano para verificar a vitória
        
        #caso o "dê velha" no jogo-da-velha, o jogo empata e recomeça e os jogadores não sua pontuação alterada
        if jogadas >= 24:
            print("Impate ninguém ganhou")
            break

        #alternando entre player 1 e player 2
        if counter == 0:
            l = int(input("Player 1, digite a linha: "))
            c = int(input("Player 1, digite a coluna: "))
            if matrix[l][c] == " ":
                matrix[l][c] = "X"
                counter = counter + 1
                jogadas = jogadas + 1
                imprimindo_o_game()
                victory_detection()
                if victory_detection() == True:
                    victory_player1()
                    break
            else:
                print("Escolha outro lugar, este já está ocupado")
                jogadas = jogadas - 1
                pass
                
        if counter != 0:
            l = int(input("Player 2, digite a linha: "))
            c = int(input("Player 2, digite a coluna: "))        
            if matrix[l][c] == " ":
                matrix[l][c] = "O"
                counter = counter - 1
                jogadas = jogadas + 1
                imprimindo_o_game() 
                victory_detection()
                if victory_detection() == True:
                    victory_player2()
                    break   
            else:
                print("Escolha outro lugar, este já está ocupado")
                jogadas = jogadas - 1
                pass   
    

#criando a função principal
def main():
    while True:
        print("-------Menu-------")
        print("1-Criar novo Player")
        print("2-Iniciar o Jogo")
        print("3-Mostrar pontuação")
        print("4-Excluir Player")
        print("------------------")
        a = int(input("Digite a função que desejar: "))
        if a == 1:
            create_new_player() #função da criação de jogador
        elif a == 2:
            funcao_do_game() #função de iniciar o jogo
        elif a == 3:
            read_score() #função de leitura de pontuação 
        elif a == 4:
            erase_existing_player() #função de apagar pontuação 
        else:
            print("Digite uma função válida")    

main()       
