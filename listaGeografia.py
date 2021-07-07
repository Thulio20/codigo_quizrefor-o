def geografia():
    print('------------------------------------------------------')
    print('                     Geografia'                        )
    print('------------------------------------------------------')
    perguntas = {
          'Pergunta 1': {
              'pergunta': 'No que toca à vegetação, a maior parte da região Norte é coberta por qual tipo florestal ? ',
              'respostas': {'a': 'Mata Atlântica.', 'b': 'Mata de Araucárias.', 'c': 'Mata de Cocais.', 'd': 'Floresta Amazônica.'},
                'resposta_certa': 'd'
               },
           'Pergunta 2': {
               'pergunta': 'Qual alternativa indica corretamente os três tipos de matas presentes na vegetação amazônica ? ',
              'respostas': {'a': 'Matas de igapó, várzea e terra firme. ', 'b': 'Matas de galeria, ciliar e submersa. ', 'c': 'Matas de altitude, de planalto e de planície. ', 'd': 'Campos altos, campos de altitude e cerradão.'},
                'resposta_certa': 'a'
               },
           'Pergunta 3': {
               'pergunta': ' A hidrografia da região Norte do Brasil é marcada por rios caudalosos que formam a maior bacia hidrográfica do planeta. Qual o principal rio dessa bacia ? ',
              'respostas': {'a': 'Rio Branco.', 'b': 'Rio Madeira.', 'c': 'Rio Tucuruí', 'd': 'Rio Amazonas'},
                'resposta_certa': 'd'
               },
           'Pergunta 4': {
               'pergunta': '  Quais são as duas maiores aglomerações urbanas da região Norte brasileira ? ',
              'respostas': {'a': 'Belém e Macapá', 'b': 'Belém e Manaus', 'c': 'Manaus e Palmas', 'd': 'Palmas e Rio Branco'},
                'resposta_certa': 'b'
               },
           'Pergunta 5': {
               'pergunta': 'Quais as duas atividades produtivas que estão diretamente relacionadas ao desmatamento da Amazônia ? ',
              'respostas': {'a': 'A extração de petróleo e a pesca ilegal.', 'b': 'A produção de soja e a criação de bovinos.', 'c': 'A exploração de sal e a biopirataria.', 'd': 'A retirada de areia e a criação avícola.'},
                'resposta_certa': 'b'
               },
           'Pergunta 6': {
               'pergunta': 'Sobre o avanço da agricultura, é correto afirmar:',
              'respostas': {'a': 'A região apresenta a maior produção de celulose do país.', 'b': 'O maior rebanho bovino do país encontra-se nessa região.', 'c': 'O cultivo da soja é o que mais tem incorporado áreas da Amazônia.', 'd': 'As culturas irrigadas de fruticultura têm registrado uma forte expansão.'},
                'resposta_certa': 'b'
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
    print(f'Sua porcentagem de acerto em Geografia foi de {round(porcentagem_acerto,1)} %')
