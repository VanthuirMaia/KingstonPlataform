from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_mail import Mail, Message



# Configurações
app = Flask(__name__)
app.config['SECRET_KEY'] = 'palm8X9394'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'kingston.analytics.dados@gmail.com'
app.config['MAIL_PASSWORD'] = 'tiao oqkh azda jftm'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

# Rotas

# Rota Principal
@app.route('/')
def home():
    return render_template('index.html')

# Rota de Projetos
@app.route('/projetos')
def projetos():
    return render_template('projetos.html')

# Rota de Contato
@app.route('/contato', methods=['GET', 'POST'])
def contato():
    form = ContatoForm()

    if form.validate_on_submit():
        # Criação do e-mail
        msg = Message('Novo Contato',
                      sender=form.email.data,
                      recipients=['kingston.analytics.dados@gmail.com'])

        msg.body = f"Nome: {form.nome.data}\nEmail: {form.email.data}\nMensagem: {form.mensagem.data}"

        try:
            # Enviar e-mail
            mail.send(msg)

            # Limpa os campos do formulário manualmente
            form.nome.data = ""
            form.email.data = ""
            form.mensagem.data = ""

            # Adiciona a mensagem flash para sucesso
            flash('Sua mensagem foi enviada com sucesso!', 'success')

            # Redireciona para recarregar a página e garantir que os campos sejam limpos
            return redirect(url_for('contato'))

        except Exception as e:
            flash(f"Ocorreu um erro ao tentar enviar o e-mail: {e}", 'danger')

    return render_template('contato.html', form=form)

# Rota de Sobre
@app.route('/sobre')
def sobre():
    return render_template('sobre.html')



# Classes

# Classe de Formulário
class ContatoForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    mensagem = TextAreaField('Mensagem', validators=[DataRequired()])
    enviar = SubmitField('Enviar')









if __name__ == '__main__':
    app.run(debug=True)