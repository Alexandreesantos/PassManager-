from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'chave_secreta'

# Usuários cadastrados manualmente
usuarios = {
    'admin@email.br': '12345',
    'admin@email.com': 'admin123'
}

@app.route('/')
def index():
    if 'usuario' in session:
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    senha = request.form['senha']

    if email in usuarios and usuarios[email] == senha:
        session['usuario'] = email
        return redirect(url_for('dashboard'))
    else:
        return 'Login falhou. Verifique seu email e senha!'

@app.route('/dashboard')
def dashboard():
    if 'usuario' in session:
        return f'Bem-vindo, {session["usuario"]}! <a href="/logout">Logout</a>'
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('index'))

@app.route('/esqueci_senha')
def esqueci_senha():
    return 'Página de recuperação de senha em construção.'

if __name__ == '__main__':
    app.run(debug=True)
