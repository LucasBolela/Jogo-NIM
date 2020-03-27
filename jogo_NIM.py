def main():
  print("Bem vindo ao Jogo do NIM! Escolha:")
  print("1 - Para jogar uma partida isolada")
  start=int(input("2 - Para jogar um campeonato "))
  if start ==1:
    return partida(1)
  elif start==2:
    return campeonato(3)
def partida(a):
  i=1
  while i<=a:
    print("**** Rodada %d ****" %i)
    n=int(input("Quantas peças? "))
    m=int(input("Limite de peças por jogada? "))
    if n%(m+1)==0 and n>m:
      print("Você começa!")
      while n>0:
        t = usuario_escolhe_jogada(n,m)
        n-=t
        if t==1:
          print("Você tirou uma peça.")
        else:
          print("Você tirou %d peças." %t)
        if n==1:
          print("Agora resta apenas uma peça no tabuleiro.")
        elif n>1:
          print("Agora restam apenas %d peças no tabuleiro." %n)
        else:
          print("Fim do jogo! Você ganhou!")
        if n>0:
          d = computador_escolhe_jogada(n,m)
          n-=d
          if d==1:
            print("O computador tirou uma peça.")
          else:
            print("O computador tirou %d peças" %d)
          if n==1:
            print("Agora resta apenas uma peça no tabuleiro.")
          elif n>1:
            print("Agora restam apenas %d peças no tabuleiro." %n)
          else:
            print("Fim do jogo! O computador ganhou!")
    elif n<m:
      partida(a)
    else:
      print("Computador começa!")
      while n>0:
        d = computador_escolhe_jogada(n,m)
        n-=d
        if d==1:
          print("O computador tirou uma peça.")
        else:
          print("O computador tirou %d peças" %d)
        if n==1:
          print("Agora resta apenas uma peça no tabuleiro.")
        elif n>1:
          print("Agora restam apenas %d peças no tabuleiro." %n)
        else:
          print("Fim do jogo! O computador ganhou!")
        if n>0:       
          t = usuario_escolhe_jogada(n,m)
          n-=t
          if t==1:
            print("Você tirou uma peça.")
          else:
            print("Você tirou %d peças." %t)
          if n==1:
            print("Agora resta apenas uma peça no tabuleiro.")
          elif n>1:
            print("Agora restam apenas %d peças no tabuleiro." %n)
          else:
            print("Fim do jogo! Você ganhou!")
    i+=1
def campeonato(a):
  partida(a)
  print("**** Final do campeonato! ****")
  print("Placar: Você 0 X 3 Computador")
def usuario_escolhe_jogada(n,m):
  t=int(input("Quantas peças você vai tirar? "))
  if t>m or t<=0:
    print("Oops! Jogada inválida! Tente de novo.")
    return usuario_escolhe_jogada(n,m)
  else:
    n-=t
    return t
def computador_escolhe_jogada(n,m):
  if n<=m:
    return n
  else:
    a=n
    while a%(m+1)!=0:
      a-=1
    d=n-a
    return d
main()