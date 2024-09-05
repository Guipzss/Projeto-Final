from flask import Flask, jsonify, request

gameapi = Flask(__name__)

#inicio
@gameapi.route("/")
def inicio():
    return "JOGOS."

#dicionarios
jogos = [
    {
        "id": 1,
        "título": "Elden Ring",
        "desenvolvedor(a)": "FromSoftware"
    },
    {
        "id": 2,
        "título": "The Binding Of Isaac",
        "desenvolvedor(a)": "Edmund McMillen"
    },
    {
        "id": 3,
        "título": "Persona 3 Reload",
        "desenvolvedor(a)": "Atlus"
    }
]

#Consultar
@gameapi.route("/jogos",methods=["GET"])
def obter_jogo():
    return jsonify(jogos)

#Buscar
@gameapi.route("/jogos/<int:id>",methods=["GET"])
def buscar_jogo(id):
    for jogo in jogos:
        if jogo.get("id") == id:
            return jsonify(jogo)

#Editar
@gameapi.route("/jogos/<int:id>",methods=["PUT"])
def editar_jogo(id):
    jogo_alterado = request.get_json()
    for indice,jogo in enumerate(jogos):
        if jogo.get("id") == id:
            jogos[indice].update(jogo_alterado)
            return jsonify(jogos[indice])
        
#Criar
@gameapi.route("/jogos",methods=["POST"])
def incluir_jogo():
    novo_jogo = request.get_json()
    jogos.append(novo_jogo)
    
    return jsonify(jogos)

#Excluir
@gameapi.route("/jogos/<int:id>",methods=["DELETE"])
def deletar_jogo(id):
    for indice, jogo in enumerate(jogos):
        if jogo.get("id") == id:
            del jogos[indice]

    return jsonify(jogos)

gameapi.run(port=5000,host="localhost", debug=True)
