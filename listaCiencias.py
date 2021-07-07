def ciencias():
        print('------------------------------------------------------')
        print('                     Ciencias'                         )
        print('------------------------------------------------------')
        perguntas = {
            'Pergunta 1': {
                'pergunta': 'Qual é o maior planeta do nosso sistema solar ? ',
                'respostas': {'a': 'Planeta Terra.', 'b': 'Planeta Júpiter.', 'c': 'Planeta Marte.', 'd': 'Planeta Saturno.'},
                'resposta_certa': 'b'
            },
            'Pergunta 2': {
                'pergunta': 'Qual é o 7ª elemento na tabela periódica dos elementos ? ',
                'respostas': {'a': 'Nitrogênio.', 'b': 'Oxigênio.', 'c': 'Cobre.', 'd': 'Aluminio'},
                'resposta_certa': 'a'
            },
            'Pergunta 3': {
                'pergunta': ' A água pura tem um nível de pH aproximadamente de ? ',
                'respostas': {'a': '8.', 'b': '9.', 'c': '10', 'd': '7'},
                'resposta_certa': 'd'
            },
            'Pergunta 4': {
                'pergunta': 'O medo de que animal é conhecido como "aracnofobia" ? ',
                'respostas': {'a': 'peixe', 'b': 'vaca', 'c': 'aranha', 'd': 'cachorro'},
                'resposta_certa': 'c'
            },
            'Pergunta 5': {
                'pergunta': 'Qual é o nome da parte do esqueleto humano que protege nosso cérebro ? ',
                'respostas': {'a': 'Braço', 'b': 'Perna', 'c': 'Pé', 'd': 'Crânio'},
                'resposta_certa': 'd'
            },
            'Pergunta 6': {
                'pergunta': 'Como se chamam as ondas gigantes ? ',
                'respostas': {'a': 'Tsunami .', 'b': 'Ondas Grandes.', 'c': 'Furacão.', 'd': 'Seca.'},
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
        print(
            f'Sua porcentagem de acerto em ciencias foi de {round(porcentagem_acerto,1)} %')
