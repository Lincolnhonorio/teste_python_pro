from flask import Flask, jsonify, request

app = Flask(__name__)

tarefas = [
    {"id": 1, "titulo": "Ler o conteúdo do teste", "concluida": True},
    {"id": 2, "titulo": "Iniciar planejamento e o projeto no VSCode", "concluida": True},
    {"id": 3, "titulo": "Enviar projeto para avaliação", "concluida": False}
]


@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    return jsonify(tarefas)


@app.route('/tarefas', methods=['POST'])
def adicionar_tarefa():
    nova_tarefa = request.get_json()

    if not nova_tarefa or "titulo" not in nova_tarefa:
        return jsonify({"erro": "Dados inválidos"}), 400
 
    novo_id = max(t["id"] for t in tarefas) + 1 if tarefas else 1
    nova_tarefa = {
        "id": novo_id,
        "titulo": nova_tarefa["titulo"],
        "concluida": nova_tarefa.get("concluida", False)
    }

    tarefas.append(nova_tarefa)
    return jsonify({"mensagem": "Tarefa adicionada com sucesso!", "tarefa": nova_tarefa}), 201


@app.route('/tarefas/<int:id>', methods=['PUT'])
def atualizar_tarefa(id):
    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "Dados inválidos"}), 400

    tarefa = next((t for t in tarefas if t["id"] == id), None)

    if not tarefa:
        return jsonify({"erro": "Tarefa não encontrada"}), 404

    # Atualiza apenas os campos permitidos
    tarefa["titulo"] = dados.get("titulo", tarefa["titulo"])
    tarefa["concluida"] = dados.get("concluida", tarefa["concluida"])

    return jsonify({
        "mensagem": "Tarefa atualizada com sucesso!",
        "tarefa": tarefa
    }), 200


@app.route('/tarefas/<int:id>', methods=['DELETE'])
def deletar_tarefa(id):
    tarefa = next((t for t in tarefas if t["id"] == id), None)

    if not tarefa:
        return jsonify({"erro": "Tarefa não encontrada"}), 404

    tarefas.remove(tarefa)
    return jsonify({"mensagem": "Tarefa removida com sucesso!"}), 200


@app.route('/')
def mensagem_inicial():
    return jsonify({'mensagem': 'Bem-vindo ao projeto Kodland!'})


if __name__ == '__main__':
    app.run(debug=True)
