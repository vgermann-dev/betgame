from flask import Flask, request, jsonify
from models.sistema import Sistema

app = Flask(__name__)
sistema = Sistema()

@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    dados = request.json
    sucesso, msg = sistema.cadastro(
        login=dados.get("login"),
        email=dados.get("email"),
        senha=dados.get("senha"),
        pix=dados.get("pix")
    )
    status = 200 if sucesso else 400
    return jsonify({"mensagem": msg}), status

@app.route("/login", methods=["POST"])
def login():
    dados = request.json
    sucesso, msg = sistema.login(
        login=dados.get("login"),
        senha=dados.get("senha")
    )
    status = 200 if sucesso else 400
    return jsonify({"mensagem": msg}), status

@app.route("/jogar", methods=["POST"])
def jogar():
    dados = request.json
    sucesso, resultado = sistema.jogar(
        login=dados.get("login"),
        escolha=dados.get("escolha"),
        aposta=dados.get("aposta"),
        rodadas=dados.get("rodadas"),
        explosivo=dados.get("explosivo", False)
    )
    status = 200 if sucesso else 400
    return jsonify(resultado), status

if __name__ == "__main__":
    app.run(debug=True)
