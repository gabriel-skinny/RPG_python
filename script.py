# Escrever o codigo aqui
salaAtual = 1
contadorDeTentativas = 0
perdeu = False

def Escolhercaminho():
  global salaAtual
  global contadorDeTentativas
  global perdeu


  contadorDeTentativas += 1

while (salaAtual < 9):
  Escolhercaminho()
else:
  print("Voce conseguiu sair da dungeon com apenas {} tentativas".format(contadorDeTentativas))
