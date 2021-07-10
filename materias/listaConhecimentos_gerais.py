def conhecimentos_gerais():
    print('------------------------------------------------------')
    print('                Conhecimentos Gerais                  ')
    print('------------------------------------------------------')
    perguntas = {
                    'Pergunta 1': {
                        'pergunta': 'Normalmente, quantos litros de sangue uma pessoa tem ? ',
                        'respostas': {'a': 'Tem entre 2 a 4 litros.', 'b': 'Tem entre 4 a 6 litros.', 'c': 'Tem 10 litros.', 'd': 'Tem 7 litros.'},
                        'resposta_certa': 'b'
                    },
                    'Pergunta 2': {
                        'pergunta': 'De quem é a famosa frase “Penso, logo existo” ? ',
                        'respostas': {'a': 'Platão. ', 'b': 'Galileu Galilei. ', 'c': 'Descartes. ', 'd': 'Sócrates.'},
                        'resposta_certa': 'c'
                    },
                    'Pergunta 3': {
                        'pergunta': ' De onde é a invenção do chuveiro elétrico? ',
                        'respostas': {'a': 'França.', 'b': 'Inglaterra.', 'c': 'Austrália', 'd': 'Brasil'},
                        'resposta_certa': 'd'
                    },
                    'Pergunta 4': {
                        'pergunta': '  Quais são as duas maiores aglomerações urbanas da região Norte brasileira ? ',
                        'respostas': {'a': 'Belém e Macapá', 'b': 'Belém e Manaus', 'c': 'Manaus e Palmas', 'd': 'Palmas e Rio Branco'},
                        'resposta_certa': 'b'
                    },
                    'Pergunta 5': {
                        'pergunta': 'Quais o menor e o maior país do mundo? ',
                        'respostas': {'a': 'Vaticano e Rússia.', 'b': 'Nauru e China.', 'c': 'Mônaco e Canadá.', 'd': 'Malta e EUA.'},
                        'resposta_certa': 'a'
                    },
                    'Pergunta 6': {
                        'pergunta': ' Qual o número mínimo de jogadores numa partida de futebol ?',
                        'respostas': {'a': '8.', 'b': '10.', 'c': '9.', 'd': '7.'},
                        'resposta_certa': 'd'
                    },
                 }

    respostas_certas = 0
    for pk, pv in perguntas.items():
            print(f'{pk} : {pv["pergunta"]}')

            print('Escolha as opçoes abaixo : ')

            for rk, rv in pv['respostas'].items():
                print(f'[{rk}]: {rv}')
                print()

            respostas_usuario = input('Sua resposta: ')
            respostas_usuario = respostas_usuario.lower()

            if respostas_usuario == pv['resposta_certa']:
                print('Resposta Certa')
                respostas_certas += 1
            else:
                print('Resposta Errada')
                print()

            qtd_perguntas = len(perguntas)
            porcentagem_acerto = respostas_certas / qtd_perguntas * 100

            print(f'Voce acertou {respostas_certas} respostas.')
            print(f'Sua porcentagem de acerto em Conhecimentos Gerais foi de {round(porcentagem_acerto,1)} %')
