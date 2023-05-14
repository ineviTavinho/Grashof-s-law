import numpy as np


elo_1 = int(input('Entre com a dimensão da 1° Barra: '));
elo_2 = int(input('Entre com a dimensão da 2° Barra: '));
elo_3 = int(input('Entre com a dimensão da 3° Barra: '));
elo_4 = int(input('Entre com a dimensão da 4° Barra: '));


mecanismo = [elo_1,elo_2,elo_3,elo_4];

if ((mecanismo[0] + mecanismo[1] or (mecanismo[0] + mecanismo[3]) or (mecanismo[1] + mecanismo[3])) > mecanismo[2])and (mecanismo[0] + mecanismo[2]) < (mecanismo[1] + mecanismo[3]):
  def sort(mecanismo):
    for i in range(len(mecanismo)-1,0,-1):
        for j in range(i):
            if mecanismo[j]>mecanismo[j+1]:
                temp = mecanismo[j]
                mecanismo[j]= mecanismo[j+1]
                mecanismo[j+1]= temp
  sort(mecanismo)
  vet_mec = mecanismo
  print(vet_mec)
  l1 = elo_1;
  l2 = elo_2;
  l3 = elo_3;
  l4 = elo_4;


  S = (min(vet_mec));
  L =(max(vet_mec));
  P= (vet_mec[1]);
  Q = (vet_mec[2]);
  x = S+L;
  y = P+Q;
  if x<=y:
    print('Pertence á condição de Grashof')
    if x==y:
        print('Caso especial de Grashof, Classe III')
        espec = input('O elo menor é Terra, Entrada, Acoplador ou Saída? ')
        if espec == 'Saída':
            print('O mecanismo em questão se trata de um seguidor-seguidor-manivela (Caso especial do seguidor manivela). ')
            Cod = 'CSSM'
            print(Cod)
        if espec == 'Acoplador':
            print(' O mecanismo em questão se trata de um seguidor-manivela-seguidor com ponto de mudança (Caso especial do manivela-seguidor). ')
            Cod = 'CSMS'
            print(Cod)
        if espec == 'Entrada':
            print(' O mecanismo em questão se trata de um manivela-seguidor-seguidor com ponto de mudança(Caso especial do manivela seguidor). ')
            Cod = 'CMSS'
            print(Cod)


        if espec == 'Terra':
            print(' O mecanismo em questão se trata de um manivela-manivela-manivela com ponto de mudança(Caso especial do dupla manivela). ')
            Cod = 'CMMM'
            print(Cod)


        if l1==l2 & l2==l3 & l3==l4:
       
            print(' O mecanismo em questão se trata de um ponto de mudança triplo (Quadrado)')
            Cod = 'C3X'
            print(Cod)
    else:
        print('Caso especial de Grashof, Classe I')
        espec = (input('O elo fixado é adjacente ao menor elo, oposto ao menor elo ou o menor elo? '))
        if espec == 'adjacente':
            print('O mecanismo em questão é um manivela seguidor de Grashof. ') 
             
        if espec == 'oposto':
            print('O mecanismo em questão se trata de um Duplo seguidor de Grashof. ')
            Cod = 'GMMM'

        if espec == 'menor':
            print('O mecanismo em questão se trata de uma Dupla manivela de Grashof. ')
            Cod = 'GSMS'
       
    if x>y:
      print('Não é Grashof, Classe II')
      print('Todas as inversões serão triplos seguidores, sendo assim, nenhuma barra irá conseguir revolucionar completamente.' )
else:
   print(' As dimensões inseridas não podem compor um mecanismo de quatro barras. ')