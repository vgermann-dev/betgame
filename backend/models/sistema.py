from models.usuarios import Usuario
from models.bet1 import Game

class Sistema:
    def __init__(self):
        self.usuarios = {}  # Dicionário para armazenar usuários: login -> Usuario

    def cadastro(self, login, email, senha, pix):
        """Cadastra um novo usuário"""
        if login in self.usuarios:
            return False, "Usuário já existente."
        self.usuarios[login] = Usuario(login, email, senha, pix)
        return True, "Usuário cadastrado com sucesso."

    def login(self, login, senha):
        """Verifica login e senha do usuário"""
        usuario = self.usuarios.get(login)
        if usuario and usuario.verificar_senha(senha):
            return True, "Login realizado com sucesso."
        return False, "Login ou senha inválidos."

    def jogar(self, login, escolha, aposta, rodadas, explosivo=False):
        """Executa uma partida do jogo para o usuário"""
        usuario = self.usuarios.get(login)
        if not usuario:
            return False, "Usuário não encontrado."

        # Cria uma instância do Game
        jogo = Game(aposta=aposta, escolha=escolha, rodadas=rodadas, explosivo=explosivo)
        resultado = jogo.executar_rodadas()

        # Atualiza saldo e histórico do usuário
        usuario.atualizar_saldo(jogo.aposta)
        usuario.adicionar_historico(resultado)

        return True, {"resultado": resultado, "saldo_atual": usuario.saldo}
