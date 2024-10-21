from pacoteViagem import PacoteViagem

opcao = 0

while opcao != 6:
    print('--- Agência de Viagem ---')
    print('1.Cadastrar Pacote;\n2.Consultar Pacotes;\n3.Deletar Pacote;\n4.Atualizar Pacote;\n5.Consultar Pacote Individual;\n6.Sair')
    opcao = int(input('Selecione uma opção: '))
    pacote = PacoteViagem()
    if opcao == 1:
        destino = str(input('Destino da Viagem: '))
        preco = float(input('Preço do Pacote: '))
        descricao = input('Descreva o destino: ')
        pacote.cadastrarPacote(destino, preco, descricao)
        print('===============')
    elif opcao == 2:
        print('===', 'Pacotes:')
        pacote.consultarPacotes()
        print('===============')
    elif opcao == 3:
        print('Pacotes:')
        pacote.consultarPacotes()
        id = int(input('Informe o Id do Pacote: '))
        pacote.deletarPacote(id)
        print('===============')
    elif opcao == 4:
        print('Pacotes:')
        pacote.consultarPacotes()
        id = int(input('Informe o Id do Pacote: '))
        pacote.atualizarPacote(id)
        print('===============')
    elif opcao == 5:
        print('Pacotes:')
        pacote.consultarPacotes()
        id = int(input('Informe o Id do Pacote: '))
        pacote.consultarPacoteIndividual(id)
        print('===============')
    elif opcao == 6:
        print('===============')
        break
print('Seja Sempre Bem-Vindo(a)!')