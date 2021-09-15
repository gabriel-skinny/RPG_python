# Escrever o codigo aqui
import random

salaAtual = 1
contadorDeTentativas = 0
perdeu = False
jogo = True
personagem = 0

def PegarInputs(tipo):
  if (tipo == "personagem"):
    print("Escolha o seu personagem")
    print("[1] - Guerreiro")
    print("[2] - Arqueiro ")
    print("[3] - Ladingo")
    print("[4] - Mago \n ")

    return int(input())

  elif (tipo == "caminho"):
    print("\nVoce esta na sala {}".format(salaAtual))
    print("Escolha seu caminho:")
    print("[1] - Caminho Vermelho")
    print("[2] - Caminho Preto\n")

    return int(input())

  else:
    print("ERROR!!")

def EscolherPersonagem():
  global personagem
  global jogo
  global perdeu
  
  personagem = PegarInputs("personagem")

  if (personagem > 4 or personagem < 1):
    print("\n\n\nERROR NAO EXISTE ESSE PERSONAGEM QUE FOI DIGITADO!!\n")
    jogo = False
    perdeu = True
    return

def Escolhercaminho():
  global salaAtual
  global contadorDeTentativas
  global perdeu
  global jogo

  caminhoEscolhido = PegarInputs("caminho")

  contadorDeTentativas += 1

  if (contadorDeTentativas == 7):
    perdeu = True
    
  if (salaAtual == 6 and caminhoEscolhido == 1):
    print("\nNAO EH POSSIVEL SAIR DA SALA POR ESSE CAMINHO!!!!")
    return

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


while(jogo):
  EscolherPersonagem()

  while (salaAtual < 9 and not(perdeu) and jogo):
    Escolhercaminho()
  else:
    if perdeu: print("\n\n\nO limite de tentativas eram 7 vc usou um total de {} tentativa. VOCE PERDEU! \n \n \n \n".format(contadorDeTentativas))
    else:  print("\n\nVoce conseguiu sair da dungeon com apenas {} tentativas \n \n \n \n".format(contadorDeTentativas)) 
else: 
  print("O JOGO ACABOU!!\n")