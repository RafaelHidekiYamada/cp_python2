from funcoes import (
    exibir_tabuleiro,
    verificar_vencedor,
    verificar_empate,
    jogada_valida,
    escolher_simbolo
)


def jogar():
    tabuleiro = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    jogador1, jogador2 = escolher_simbolo()
    jogador_atual = jogador1
    nome_jogador = "Jogador 1"

    print(f"\nJogador 1 = {jogador1}")
    print(f"Jogador 2 = {jogador2}")

    while True:
        exibir_tabuleiro(tabuleiro)

        try:
            linha = int(input(f"{nome_jogador} ({jogador_atual}), digite a linha (1, 2 ou 3): ")) - 1
            coluna = int(input(f"{nome_jogador} ({jogador_atual}), digite a coluna (1, 2 ou 3): ")) - 1
        except ValueError:
            print("Entrada inválida. Digite apenas números entre 1 e 3.")
            continue

        if not jogada_valida(tabuleiro, linha, coluna):
            print("Jogada inválida. Escolha uma posição vazia dentro do tabuleiro.")
            continue

        tabuleiro[linha][coluna] = jogador_atual

        if verificar_vencedor(tabuleiro, jogador_atual):
            exibir_tabuleiro(tabuleiro)
            print(f"{nome_jogador} venceu!")
            break

        if verificar_empate(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print("O jogo terminou em empate!")
            break

        if jogador_atual == jogador1:
            jogador_atual = jogador2
            nome_jogador = "Jogador 2"
        else:
            jogador_atual = jogador1
            nome_jogador = "Jogador 1"


jogar()