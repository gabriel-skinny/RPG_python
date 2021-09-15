# Escrever o codigo aqui
import random

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
    
    if (salaAtual == 6 and caminhoEscolhido == 1):
        salaAtual = 5
        print("Nao eh possivel sair dessa sala por esse caminho")

    if (caminhoEscolhido == 1):
        salaAtual+= 1
    elif (caminhoEscolhido == 2):
        salaAtual += 2
    else:
        print("Erro nao existe esse caminho")
        
    if (salaAtual == 8):
      print("Voce caiu em um portal portanto voce vai retornar para uma sala aleatoria")
      salaAtual = random.randint(1, 5)
      print("Voce retornou para a sala {}".format(salaAtual))
  
while (salaAtual < 9 and not(perdeu)):
  Escolhercaminho()
else:
  if perdeu: print("\n\nVoce usou mais tentativas do que podiam vc PERDEU! \n \n \n \n")
  else:  print("\n\nVoce conseguiu sair da dungeon com apenas {} tentativas \n \n \n \n".format(contadorDeTentativas)) 
