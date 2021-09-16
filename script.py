# Escrever o codigo aqui
import random

salaAtual = 1
contadorDeTentativas = 0
perdeu = False
jogo = True
personagem = 0

def EscolherPersonagem():
  global personagem
  global jogo
  global perdeu
  
  print("\033[1;34mEscolha o seu personagem\n")
  print("[1] - Guerreiro")
  print("[2] - Arqueiro ")
  print("[3] - Ladingo")
  print("[4] - Mago \n ")
  personagem = int(input())

  print("\033[1;33m\n\nVOCE ENTROU NA DUNGEON\n")

  if (personagem > 4 or personagem < 1):
    print("\n\n\nERROR NAO EXISTE ESSE PERSONAGEM QUE FOI DIGITADO!!\n")
    jogo = False
    perdeu = True
    return

def personagemDica(salaAtual, personagem):
  if (salaAtual == 5 and personagem == 1):
      print("\033[1;33m\n\nVoce encontrou uma pedra que somente o seu personagem consegue ler e nela esta escrita uma dica")
      print("\nDica: o caminho vermelho leva a sala 7")

  if (salaAtual == 2 and personagem == 2):
      print("\033[1;33m\n\nVoce encontrou uma pedra que somente o seu personagem consegue ler e nela esta escrita uma dica")
      print("\nDica: o caminho preto leva a sala 4")

  if (salaAtual == 4 and personagem == 3):
      print("\033[1;33m\n\nVoce encontrou uma pedra que somente o seu personagem consegue ler e nela esta escrita uma dica")
      print("\nDica: o caminho preto leva a sala 6")

  if (salaAtual == 6  and personagem == 4):
      print("\033[1;33m\n\nVoce encontrou uma pedra que somente o seu personagem consegue ler e nela esta escrita uma dica")
      print("\nDica: nesta sala eh apenas possivel usar o caminho preto")

def Escolhercaminho():
  global salaAtual
  global contadorDeTentativas
  global perdeu
  global jogo
  global personagem

  print("\033[1;34m\nVoce esta na sala {}".format(salaAtual))
  print("Escolha seu caminho:\n")
  print("[1] - Caminho Vermelho")
  print("[2] - Caminho Preto\n")

  caminhoEscolhido = int(input())
  
  if (salaAtual == 6 and caminhoEscolhido == 1):
    salaAtual-=caminhoEscolhido
    print("\033[1;31m\nNAO EH POSSIVEL SAIR DA SALA POR ESSE CAMINHO!!!!")
    return

  salaAtual+= caminhoEscolhido

  personagemDica(salaAtual, personagem)

  contadorDeTentativas += 1

  if (contadorDeTentativas == 7):
    perdeu = True
    jogo = False
        
  if (salaAtual == 10):
    print("\033[1;33m\nVoce caiu em um portal portanto voce vai retornar para uma sala aleatoria")
    salaAtual = random.randint(1, 5)
    print("Voce retornou para a sala {}".format(salaAtual))

while(jogo):
  EscolherPersonagem()

  while (salaAtual < 9 and not(perdeu) and jogo):
    Escolhercaminho()
  else:
    jogo = False

    if perdeu: print("\033[1;31m\n\n\nO limite de tentativas eram 7. VOCE PERDEU! \n \n \n \n".format(contadorDeTentativas))
    else:  print("\033[1;32m\n\nVoce conseguiu sair da dungeon com apenas {} tentativas \n \n \n \n".format(contadorDeTentativas)) 
else: 
  print("\033[1;33mO JOGO ACABOU!!\n")
