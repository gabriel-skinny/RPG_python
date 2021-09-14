# Escrever o codigo aqui
salaAtual = 1
contadorDeTentativas = 0
perdeu = False

def Escolhercaminho():
  global salaAtual
  global contadorDeTentativas
  global perdeu
  
   if (contadorDeTentativas == 7):
    print("Voce usou mais tentativas do que eram permitidas")
    perdeu = True

    print("Voce esta na sala {}".format(SalaAtual))
    print("Escolha seu caminho:")
    print("[1] - Caminho Vermelho")
    print("[2] - Caminho Preto")
    caminhoEscolhido = int(input())

  contadorDeTentativas += 1

while (salaAtual < 9):
  Escolhercaminho()
else:
  print("Voce conseguiu sair da dungeon com apenas {} tentativas".format(contadorDeTentativas))
