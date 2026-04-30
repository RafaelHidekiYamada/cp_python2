def exibir_tabuleiro(tabuleiro):
    print("\nTabuleiro:")
    for i in range(3):
        print(f" {tabuleiro[i][0]} | {tabuleiro[i][1]} | {tabuleiro[i][2]} ")
        if i < 2:
            print("---+---+---")
    print()


def verificar_vencedor(tabuleiro, simbolo):
    # Verifica linhas
    for linha in tabuleiro:
        if linha[0] == simbolo and linha[1] == simbolo and linha[2] == simbolo:
            return True

    # Verifica colunas
    for coluna in range(3):
        if (
            tabuleiro[0][coluna] == simbolo
            and tabuleiro[1][coluna] == simbolo
            and tabuleiro[2][coluna] == simbolo
        ):
            return True

    
    if tabuleiro[0][0] == simbolo and tabuleiro[1][1] == simbolo and tabuleiro[2][2] == simbolo:
        return True

    
    if tabuleiro[0][2] == simbolo and tabuleiro[1][1] == simbolo and tabuleiro[2][0] == simbolo:
        return True

    return False


def verificar_empate(tabuleiro):
    for linha in tabuleiro:
        for celula in linha:
            if celula == " ":
                return False
    return True


def jogada_valida(tabuleiro, linha, coluna):
    # Verifica se a linha ou a coluna estão fora do limite do tabuleiro.
    if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
        return False

    # Verifica se a posição escolhida já está ocupada.
    if tabuleiro[linha][coluna] != " ":
        return False

    return True


def escolher_simbolo():
    while True:
        jogador1 = input("Jogador 1, escolha X ou O: ").upper()

        if jogador1 == "X":
            jogador2 = "O"
            return jogador1, jogador2
        elif jogador1 == "O":
            jogador2 = "X"
            return jogador1, jogador2
        else:
            print("Opção inválida. Digite apenas X ou O.")