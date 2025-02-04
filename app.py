from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# Rota de Projetos
@app.route('/projetos')
def projetos():
    return render_template('projetos.html')

# Rota de Contato
@app.route('/contato')
def contato():
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)