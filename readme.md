📝 Gerenciador de Tarefas API (Flask) - Projeto Python Pro
Este projeto consiste em uma API RESTful simplificada desenvolvida com o micro-framework Flask. O objetivo é gerenciar o fluxo de atividades de um desenvolvedor, permitindo a listagem de tarefas factuais e a adição de novos itens à lista de controle.

🚀 Funcionalidades
O projeto atende aos requisitos de manipulação de dados via web utilizando funções integradas do Python e da biblioteca Flask:

Rota de Boas-vindas (/): Retorna uma mensagem de recepção confirmando que o servidor está ativo.

Listagem de Tarefas (/tarefas - GET): Exibe todas as tarefas atuais (como "Ler documentação", "Iniciar projeto") em formato JSON.

Criação de Tarefas (/tarefas - POST): Permite o envio de novos objetos JSON para serem anexados à lista de tarefas do servidor.

🛠️ Tecnologias Utilizadas
Linguagem: Python 3.x

Framework: Flask 3.1.0

Ambiente de Desenvolvimento: VS Code

Formato de Dados: JSON (JavaScript Object Notation)

📦 Como Instalar e Rodar
Siga os passos abaixo para executar o projeto em sua máquina local:

Clone ou baixe este repositório.

Abra a pasta do projeto no VS Code.

Certifique-se de ter o Python instalado. Recomenda-se o uso de um ambiente virtual (venv).

Instale as dependências necessárias utilizando o arquivo requirements.txt:

Bash
pip install -r requirements.txt
Execute o arquivo principal:

Bash
python main.py
O servidor iniciará em http://127.0.0.1:5000/.

📁 Estrutura do Projeto
main.py: Código-fonte principal contendo a lógica das rotas e inicialização do Flask.

requirements.txt: Lista de dependências e versões para garantir a reprodutibilidade do projeto.

README.md: Documentação completa do projeto (este arquivo).

👨‍💻 Critérios Técnicos Atendidos
Utilização de funções integradas (decorators @app.route, jsonify, request).

Inexistência de classes obrigatórias, mantendo o código leve e funcional.

Tratamento de métodos HTTP distintos (GET e POST) na mesma rota.

Configuração de Modo Debug para facilitar ajustes em tempo real.

Desenvolvido por Lincoln Honorio – Instrutor de Programação Python | Algoritmos e Pensamento Computacional.