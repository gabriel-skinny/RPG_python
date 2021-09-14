# Escrever o codigo aqui
salaAtual = 1
contadorDeTentativas = 0
perdeu = False

def Escolhercaminho():
  global salaAtual
  global contadorDeTentativas
  global perdeu

  print("Voce esta na sala {}".format(salaAtual))
  print("Escolha seu caminho:")
  print("[1] - Caminho Vermelho")
  print("[2] - Caminho Preto")
  caminhoEscolhido = int(input())

  contadorDeTentativas += 1

  if (contadorDeTentativas == 7):
    perdeu = True

  

while (salaAtual < 9 and not(perdeu)):
  Escolhercaminho()
else:
  if perdeu: print("\n\nVoce usou mais tentativas do que podiam vc PERDEU! \n \n \n \n")
  else:  print("\n\nVoce conseguiu sair da dungeon com apenas {} tentativas \n \n \n \n".format(contadorDeTentativas)) 
