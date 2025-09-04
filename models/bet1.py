import random

class Game:
    MAX_RODADAS = 5  # Limite de rodadas para balancear o jogo

    def __init__(self, aposta, escolha, rodadas, explosivo=False):
        self.aposta = aposta
        self.escolha = escolha
        # Limita as rodadas para o máximo definido
        self.rodadas = min(rodadas, self.MAX_RODADAS)
        self.explosivo = explosivo
        self.multiplicadores = self.gerar_multiplicadores()

    def gerar_multiplicadores(self):
        """Gera multiplicadores lineares ou exponenciais"""
        if self.explosivo:
            # Exponencial: 2^1, 2^2, 2^3...
            return [2 ** (i + 1) for i in range(self.rodadas)]
        else:
            # Linear: x2, x3, x4...
            return [i + 2 for i in range(self.rodadas)]

    def sortear_nums(self):
        """Sorteia um número entre 1 e 10"""
        return random.randint(1, 10)

    def executar_rodadas(self):
        """Executa todas as rodadas e retorna resultados"""
        resultados = []
        for i in range(self.rodadas):
            sorteio = self.sortear_nums()
            mult = self.multiplicadores[i]

            if self.escolha == sorteio:
                self.aposta *= mult
                status = "ganhou"
            else:
                # Mantém aposta mínima = multiplicador, não zera tudo
                self.aposta = max(1, mult)
                status = "perdeu"

            resultados.append({
                "rodada": i + 1,
                "sorteio": sorteio,
                "multiplicador": mult,
                "aposta": self.aposta,
                "status": status
            })

        return resultados
