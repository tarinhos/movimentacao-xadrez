```python
def dentro_tabuleiro(l, c):
 return 0 <= l < 8 and 0 <= c < 8


def movimentos_rei(l, c):
 movimentos = []
 for dl in [-1, 0, 1]:
     for dc in [-1, 0, 1]:
         if dl != 0 or dc != 0:
             nl, nc = l + dl, c + dc
             if dentro_tabuleiro(nl, nc):
                 movimentos.append((nl, nc))
 return movimentos


def movimentos_torre(l, c):
 movimentos = []
 for i in range(8):
     if i != l:
         movimentos.append((i, c))
     if i != c:
         movimentos.append((l, i))
 return movimentos


def movimentos_bispo(l, c):
 movimentos = []
 for i in range(1, 8):
     if dentro_tabuleiro(l+i, c+i):
         movimentos.append((l+i, c+i))
     if dentro_tabuleiro(l-i, c-i):
         movimentos.append((l-i, c-i))
     if dentro_tabuleiro(l+i, c-i):
         movimentos.append((l+i, c-i))
     if dentro_tabuleiro(l-i, c+i):
         movimentos.append((l-i, c+i))
 return movimentos


def movimentos_cavalo(l, c):
 passos = [
     (2, 1), (2, -1), (-2, 1), (-2, -1),
     (1, 2), (1, -2), (-1, 2), (-1, -2)
 ]
 movimentos = []
 for dl, dc in passos:
     nl, nc = l + dl, c + dc
     if dentro_tabuleiro(nl, nc):
         movimentos.append((nl, nc))
 return movimentos


def movimentos_rainha(l, c):
 return movimentos_torre(l, c) + movimentos_bispo(l, c)


# PROGRAMA PRINCIPAL
peca = input("Peça (rei, torre, bispo, cavalo, rainha): ").lower()
linha = int(input("Linha (0 a 7): "))
coluna = int(input("Coluna (0 a 7): "))

if peca == "rei":
 print(movimentos_rei(linha, coluna))
elif peca == "torre":
 print(movimentos_torre(linha, coluna))
elif peca == "bispo":
 print(movimentos_bispo(linha, coluna))
elif peca == "cavalo":
 print(movimentos_cavalo(linha, coluna))
elif peca == "rainha":
 print(movimentos_rainha(linha, coluna))
else:
 print("Peça inválida")
