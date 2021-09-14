# Escrever o codigo aqui
SalaAtual = 1
contadorDeTentativas = 0
perdeu = False

def Escolhercaminho():
  global SalaAtual
  global contadorDeTentativas
  global perdeu


  contadorDeTentativas += 1

while (SalaAtual < 9):
  Escolhercaminho()
else:
  print("Voce conseguiu sair da dungeon com apenas {} tentativas".format(contadorDeTentativas))
