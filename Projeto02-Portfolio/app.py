from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message

app=Flask(__name__)

mail_settings={
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'rlgbluet3c6@gmail.com',
    "MAIL_PASSWORD": '15793*82'
}

app.config.update(mail_settings)
mail=Mail(app)

class Contato:
    def __init__(self, nome, email, mensagem):
        self.nome=nome
        self.email=email
        self.mensagem=mensagem

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contactform', methods=['GET', 'POST'])
def send():
    if request.method=='POST':
        formContato=Contato(
            request.form['name'],
            request.form['email'],
            request.form['message']
        )

        msg=Message(
            subject="Contato do seu portfólio",
            sender=app.config.get("MAIL_USERNAME"),
            recipients=[app.config.get("MAIL_USERNAME")],
            body=f'''{formContato.nome} enviou a seguinte mensagem
            {formContato.mensagem}'''
        )
        mail.send(msg)
    return render_template('contactform.html',
    formContato=formContato)

if __name__ == '__main__':
    app.run(debug=True)