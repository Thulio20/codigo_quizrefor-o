def historia():
    print('------------------------------------------------------')
    print('                     Historia'                        )
    print('------------------------------------------------------')
    perguntas = {
          'Pergunta 1': {
              'pergunta': 'A Proclamação da República foi realizada por: ',
              'respostas': {'a': 'Benjamin Constant.', 'b': 'Deodoro da Fonseca.', 'c': 'Floriano Peixoto.', 'd': 'José do Patrocínio.'},
                'resposta_certa': 'd'
               },
           'Pergunta 2': {
               'pergunta': 'O período colonial no Brasil teve início em : ',
              'respostas': {'a': '1530. ', 'b': '1500. ', 'c': '1600. ', 'd': '1589.'},
                'resposta_certa': 'a'
               },
           'Pergunta 3': {
               'pergunta': 'No período pré-colonial a atividade econômica que teve maior destaque foi:  ',
              'respostas': {'a': 'Rio Branco.', 'b': 'Rio Madeira.', 'c': 'Rio Tucuruí', 'd': 'Rio Amazonas'},
                'resposta_certa': 'd'
               },
           'Pergunta 4': {
               'pergunta': '  Quais são as duas maiores aglomerações urbanas da região Norte brasileira ? ',
              'respostas': {'a': 'Mineração', 'b': 'Pau-brasil', 'c': 'Café ', 'd': 'Algodão'},
                'resposta_certa': 'b'
               },
           'Pergunta 5': {
               'pergunta': 'Qual a foi a primeira capital do Brasil  ? ',
              'respostas': {'a': 'São Paulo.', 'b': 'Rio de Janeiro.', 'c': 'Salvador.', 'd': 'Brasília.'},
                'resposta_certa': 'c'
               },
           'Pergunta 6': {
               'pergunta': 'Oficialmente, a abolição da escravidão no Brasil ocorre através da:',
              'respostas': {'a': 'Lei do Ventre Livre.', 'b': 'Lei Eusébio de Queirós.', 'c': 'Lei Áurea.', 'd': 'Lei dos Sexagenários.'},
                'resposta_certa': 'c'
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
    print(f'Sua porcentagem de acerto em Historia foi de {round(porcentagem_acerto,1)} %')
