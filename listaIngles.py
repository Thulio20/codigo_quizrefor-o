def ingles():
        print('------------------------------------------------------')
        print('                      Ingles'                          )
        print('------------------------------------------------------')
        perguntas = {
            'Pergunta 1': {
                'pergunta': 'Qual é a tradução de Cachorro ? ',
                    'respostas': {'a': 'Dog.', 'b': 'Cat.', 'c': 'Play.', 'd': 'Gamer.'},
                    'resposta_certa': 'a'
                },
            'Pergunta 2': {
                'pergunta': 'Como se diz "Olá" em ingles ? ',
                    'respostas': {'a': 'HI.', 'b': 'You.', 'c': 'What.', 'd': 'How'},
                    'resposta_certa': 'a'
                },
            'Pergunta 3': {
                'pergunta': ' Como se chama "Cabo" em ingles ? ',
                    'respostas': {'a': 'Cable.', 'b': 'What.', 'c': 'Magic', 'd': 'Center'},
                    'resposta_certa': 'a'
                },
            'Pergunta 4': {
                'pergunta': ' Qual a tradução da frase "what´s your name" ? ',
                    'respostas': {'a': 'Qual o seu esporte', 'b': 'Você é especial', 'c': 'Qual o seu nome', 'd': 'Você é bonita'},
                    'resposta_certa': 'c'
                },
            'Pergunta 5': {
                'pergunta': ' Qual a tradução da frase "where are you from"  ? ',
                    'respostas': {'a': 'De onde voce é', 'b': 'Voce mora onde', 'c': 'Dia muito especial', 'd': 'Vai para onde'},
                    'resposta_certa': 'a'
                },
            'Pergunta 6': {
                'pergunta': ' Qual a resposta para a pergunta "where are you from"  ? ',
                    'respostas': {'a': 'I´m from Brasil .', 'b': 'I love You.', 'c': 'Tomorrow.', 'd': 'I do engineering.'},
                    'resposta_certa': 'a'
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
        print(f'Sua porcentagem de acerto em Ingles foi de {round(porcentagem_acerto,1)} %')
