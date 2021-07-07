
#importações das materias, listas e sorteio

from materias.listaMatematica              import matematica
from materias.listaPortugues               import portugues
from materias.listaCiencias                import ciencias
from materias.listaIngles                  import ingles    
from materias.listaGeografia               import geografia 
from materias.listaHistoria                import historia
from materias.listaConhecimentos_gerais    import conhecimentos_gerais
import random

#Menu do Jogo
print("-----------------------------------------------------------------------------------------------")
print("QuizReforço chega para agregar valores para seus estudos do ensino fundamental, Bons Estudos!! ")
print("-----------------------------------------------------------------------------------------------")
print("Digite 1 para Matematica")
print("Digite 2 para Portugues")
print("Digite 3 para Ciencias")
print("Digite 4 para Ingles")
print("Digite 5 para Historia ")
print("Digite 6 para Geografia ")
print("Digite 7 para Conhecimentos Gerais ")
print("Digite 8 para Todas as Materias ")
print("Digite 9 para Sorteiar a Materia")
opcao = int(input('Digite uma opção: '))


#Pegas as funcoes que foi definidas das materias
if opcao == 1:
    matematica()    
elif opcao == 2:
    portugues()
elif opcao == 3:
    ciencias()
elif opcao == 4:
    ingles()
elif opcao == 5:
    historia()
elif opcao == 6:
    geografia()
elif opcao == 7:
    conhecimentos_gerais()
elif opcao == 8:
    portugues()
    matematica()
    ciencias()
    ingles()
    geografia()
    historia()
    conhecimentos_gerais()
elif opcao == 9:
    materias = [portugues,matematica,ciencias,ingles,geografia,historia,conhecimentos_gerais]
    random.choice(materias)()
else:
    print('Digite uma opção do Menu' )
