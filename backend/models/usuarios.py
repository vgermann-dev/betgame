class Usuario: 
    def __init__(self, login, email, senha, pix):
        self.login = login
        self.email = email
        self.senha = senha
        self.pix = pix
        self.saldo = 50
        self.historico_jogadas = []

    def verificar_senha(self, senha):
        return self.senha == senha
    
    def atualizar_saldo(self, valor):
        self.saldo = valor

    def adicionar_historico(self, resultado):
        self.historico_jogadas.append(resultado)

    def obter_historico(self):
        return self.historico_jogadas
    
    def atualizar_saldo(self, valor):
        self.saldo += valor