import sqlite3

class PacoteViagem:
    def conexao(self):
        # 1.estabelecendo conexão com oo banco de dados.
        conexao = sqlite3.connect('agencia.db')

        # 2.verificar se a tabela existe ou não, se não, criará.
        tabela = '''  
        CREATE TABLE IF NOT EXISTS pacotes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            destino VARCHAR(100),
            preco FLOAT,
            descricao VARCHAR(300)
        );
        '''

        consulta = conexao.cursor()
        consulta.execute(tabela)
        return conexao
    
    #“cadastrarPacote”: recebe como parâmetros o destino, preço e descrição de um pacote e insere um novo pacote no banco de dados.
    def cadastrarPacote(self, destino, preco, descricao):
        conexao = self.conexao()
        consulta = conexao.cursor()
        sql = 'INSERT INTO pacotes VALUES(?,?,?,?)'
        campos = (None, destino, preco, descricao)
        consulta.execute(sql, campos)
        conexao.commit()
        print('Pacote cadastrado com sucesso.')
        conexao.close()
    
    #“consultarPacotes”: recupera todos os pacotes cadastrados no banco de dados e imprime as informações de cada pacote (destino, preço e descrição).
    def consultarPacotes(self):
        conexao = self.conexao()
        consulta = conexao.cursor()
        sql = 'SELECT * FROM pacotes'
        consulta.execute(sql)
        resultado = consulta.fetchall()
        for itens in resultado:
            print(f'Id: {itens[0]}, Destino: {itens[1]}')
        conexao.close()

    #“deletarPacote”: recebe como parâmetro o ID do pacote e, caso o pacote exista, deve ser mostrada uma mensagem de sucesso. Caso contrário, deve ser exibida uma mensagem de erro.
    def deletarPacote(self, id):
        conexao = self.conexao()
        consulta = conexao.cursor()
        sql = 'DELETE FROM pacotes WHERE id = ?'
        campos = (id,)
        consulta.execute(sql, campos)
        conexao.commit()
        if consulta.rowcount >= 1:
            print('Deletado com sucesso.')
        else:
            print('Erro.')
        import sqlite3

    #“atualizarPacote”: recebe como parâmetro o ID do pacote e alguma (ou toda) informação que se deseja atualizar. Fica a seu critério escolher quais dados deverão ser atualizados.
    def atualizarPacote(self, id):
        conexao = self.conexao()
        consulta = conexao.cursor() 
        print(consulta.rowcount)           
        if consulta.rowcount <= 1:
            print('-> Campos para mudança:\n1.Destino\n2.Preço\n3.Descricao')
            change = int(input('Informe o campo escolhido: '))
            if change == 'destino' or change == 'Destino' or change == 1:
                destino = input('Informe o seu novo destino: ')
                sql = 'UPDATE pacotes SET destino = ? WHERE id = ?'
                campos = (destino, id)
                consulta.execute(sql, campos)

            elif change == 'preco' or change == 'Preco' or change == 2:
                preco = input('Informe o novo preço: ')
                sql = 'UPDATE pacotes SET preco = ? WHERE id = ?'
                campos = (preco, id)
                consulta.execute(sql, campos)

            elif change == 'descricao' or change == 'Descricao' or change == 3:
                descricao = input('Informe uma nova descrição do destino: ')
                sql = 'UPDATE pacotes SET descricao = ? WHERE id = ?'
                campos = (descricao, id)
                consulta.execute(sql, campos)
        else:
            print('Erro.')
        conexao.commit()
        conexao.close()
        
    #“consultarPacoteIndividual”: recebe como parâmetro o código do pacote e recupera apenas esse registro da tabela e exibe todas as informações apenas do item que possui esse ID, ou seja, será feita uma consulta no banco utilizando o código como filtro para retornar um único item da tabela.
    def consultarPacoteIndividual(self, id):
        conexao = self.conexao()
        consulta = conexao.cursor()
        if consulta.rowcount <= 1:
            sql = 'SELECT * FROM pacotes WHERE id = ?'
            campos = (id,)
            consulta.execute(sql, campos)
            resultado = consulta.fetchall()
            for itens in resultado:
                print(f'Id: {itens[0]}, Destino: {itens[1]}, Preço: {itens[2]}, Descrição: {itens[3]}')
            #for linha in consulta.fetchall():
            #   if id == linha[0]:
            #       print('Pacote: ',linha)
        else:
            print('Erro.')
        conexao.commit()
        conexao.close()