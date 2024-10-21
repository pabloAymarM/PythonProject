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
    elif opcao == 2:
        print('===', 'Pacotes:')
        pacote.consultarPacotes()
        print('===============')
    elif opcao == 3:
        print('Pacotes:')
        pacote.consultarPacotes()
        id = int(input('Informe o Id do Pacote: '))
        pacote.deletarPacote(id)
    elif opcao == 4:
        print('Pacotes:')
        pacote.consultarPacotes()
        id = int(input('Informe o Id do Pacote: '))
        print('-> Campos para mudança:\n1.Destino\n2.Preço\n3.Descricao')
        opcaoChange = int(input('Informe o campo escolhido: '))
        pacote.atualizarPacote(id, opcaoChange)
    elif opcao == 5:
        print('Pacotes:')
        pacote.consultarPacotes()
        id = int(input('Informe o Id do Pacote: '))
        pacote.consultarPacoteIndividual()
    elif opcao == 6:
        break
print('Seja Sempre Bem-Vindo(a)!')