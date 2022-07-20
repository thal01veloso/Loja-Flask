from crypt import methods
from flask import Flask, jsonify, request


app = Flask(__name__)

produtos=[
    {
        "id":1,
        "nome":"Chinelo",
        "preço":10.85
    },
    {   "id":2,
        "nome":"Sapato",
        "preço":90.85 
    }
]
@app.route("/produtos/", methods=['GET'])
def getProdutos():
    return jsonify(produtos)

@app.route("/produtos/<int:cod>", methods=["GET"])
def getById(cod:int):
    return jsonify(list(filter(lambda x: x["id"]==cod,produtos))[0])

@app.route("/produto/cadastrar",methods=["POST","GET"])
def cadastrar():
    produto = request.get_json()
    produtos.append(produto)
    return jsonify(produtos)
@app.route("/produtos/deletar/<int:cod>", methods=["GET","DELETE"])
def deletar(cod):
    result = list(filter(lambda x: x["id"]==cod,produtos))[0]
    produtos.remove(result)
    return jsonify(produtos)
    


if __name__=="__main__":
    app.run(debug=True)