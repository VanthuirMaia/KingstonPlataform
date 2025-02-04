📌 Plano para o Portfólio com Flask
Home – Apresentação rápida sobre você
Projetos – Página dinâmica listando seus trabalhos
Detalhes do Projeto – Página específica para cada projeto
Contato – Formulário para receber mensagens (opcional)
Blog (opcional) – Para compartilhar conhecimento

🔹 Tecnologias usadas
Flask (framework principal)
Jinja2 (templates dinâmicos)
SQLite (ou JSON para armazenar projetos)
Bootstrap (para um design responsivo)

###################################################################################################
Estrutura do projeto

/portfolio_flask/
│── app.py               # Arquivo principal do Flask
│── config.py            # Configurações (opcional)
│── requirements.txt     # Dependências do projeto
│── /static/             # Arquivos estáticos (CSS, JS, imagens)
│── /templates/          # Arquivos HTML
│   ├── base.html        # Template base
│   ├── index.html       # Página inicial
│   ├── projetos.html    # Lista de projetos
│   ├── projeto.html     # Detalhes do projeto
│   ├── contato.html     # Página de contato
│── /data/               # Dados (ex: JSON ou banco de dados)
│── /models/             # Definição do banco de dados (se necessário)

###################################################################################################
