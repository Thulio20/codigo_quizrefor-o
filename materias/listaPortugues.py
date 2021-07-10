def portugues():
    print('------------------------------------------------------')
    print('                   Português'                          )
    print('------------------------------------------------------')
    perguntas = {
            'Pergunta 1': {
                'pergunta': 'Qual é o sinonimo de pequeno? ',
                'respostas': {'a': 'estreito', 'b': 'grande', 'c': 'alargado', 'd': 'orgulho' },
                'resposta_certa': 'a'
            },
            'Pergunta 2': {
                'pergunta': 'Assinale a alternativa em que haja erro de regência verbal? ',
                'respostas': {'a': 'Deu-lhe um belo presente de aniversario.', 'b': 'Levei-o para o medico esta manhã.', 'c': 'Gostamos deste novo filme', 'd': 'Fui no cinema ontem'},
                'resposta_certa': 'd'
            },
            'Pergunta 3': {
                'pergunta': 'Qual o tipo de sujeito da frase "A folha caiu no outono" ? ',
                'respostas': {'a' : 'sujeito simples ', 'b': 'sujeito coomposto', 'c': 'sujeito oculto', 'd': 'sujeito indeterminado'},
                'resposta_certa': 'a'
            },
            'Pergunta 4': {
                'pergunta': 'Qual das alternativas abaixo representa o núcleo do sujeito da frase :"Os avós, os pais e seus filhos viviam na fazenda da família.? ',
                'respostas': {'a': 'avós', 'b': 'avós,pais', 'c': 'avós,pais,filhos', 'd': 'pais,filhos'},
                'resposta_certa': 'c'
            },
            'Pergunta 5': {
                'pergunta': 'Qual o núcleo do predicado da frase : "Os alunos saíram do teatro encantados"? ',
                'respostas': {'a': 'alunos', 'b': 'saíram', 'c': 'encantados','d':'saíram encantados' },
                'resposta_certa': 'd'
            },
            'Pergunta 6': {
                'pergunta': 'Identifique a frase em que o predicado é verbo-nominal? ',
                'respostas': {'a': 'Luis Fernando é competente.', 'b': 'O pôr-do-sol é maravilhoso.', 'c': 'Ana Maria continua triste.', 'd':'Iara chegou cansada.'},
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
    print(f'Sua porcentagem de acerto em portugues foi de {round(porcentagem_acerto,1)} %')
