#defina a funçao
def matematica():
    print('------------------------------------------------------')
    print('                     Matematica'                       )
    print('------------------------------------------------------')
    #Dicionario
    perguntas = {
        'Pergunta 1': {
            'pergunta': 'Quanto é 2+ 2? ',
            'respostas': {'a': '1', 'b': '4', 'c': '5','d': '9' },
            'resposta_certa': 'b'
        },
        'Pergunta 2': {
            'pergunta': 'Quanto é 15 + 13? ',
            'respostas': {'a': '4', 'b': '10', 'c': '28','d': '33' },
            'resposta_certa': 'c'
        },
        'Pergunta 3': {
            'pergunta': 'Quanto é 4 * 2? ',
            'respostas': {'a': '4', 'b': '8', 'c': '6','d': '20' },
            'resposta_certa': 'b'
        },
        'Pergunta 4': {
            'pergunta': 'Quanto é 3 * 3? ',
            'respostas': {'a': '4', 'b': '10', 'c': '9','d':'12' },
            'resposta_certa': 'c'
        },
        'Pergunta 5': {
            'pergunta': 'Quanto é 15 - 2? ',
            'respostas': {'a': '4', 'b': '10', 'c': '6','d':'13' },
            'resposta_certa': 'd'
        },
        'Pergunta 6': {
            'pergunta': 'Quanto é 12 / 2? ',
            'respostas': {'a': '24', 'b': '15', 'c': '6','d':'8' },
            'resposta_certa': 'c'
        },
    }
#Laço de repeticao
    respostas_certas = 0
    #retorna as perguntas
    for p, pc in perguntas.items():
        print(f'{p} : {pc["pergunta"]}')
#Mostra para o usuario responder
        print('Escolha as opçoes abaixo : ')
#retorna as respostas
        for r, rc in pc['respostas'].items():
            print(f'[{r}]: {rc}')
            print()
#Emite a resposta certa
        respostas_usuario = input('Sua resposta: ')
        #Define se a pessoa digitar maiuscula e torna minuscula
        respostas_usuario = respostas_usuario.lower()
     #retorna a resposta certa
        if respostas_usuario == pc['resposta_certa']:
            print('Resposta Certa')
            respostas_certas += 1
        else:
            print('Resposta Errada')

        print()
#Retorna todas as perguntas
    qtd_perguntas = len(perguntas)
    #Porcentagem do acerto
    porcentagem_acerto = respostas_certas / qtd_perguntas * 100

    print(f'Voce acertou {respostas_certas} respostas de Matematica.')
    print(f'Sua porcentagem de acerto foi de {round(porcentagem_acerto,1)} %')
