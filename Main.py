from flask import *
import dao

app = Flask(__name__)
app.secret_key = '123'

@app.route('/')
def pageHome():
    if 'login' in session:
        return render_template('pageUser/homeUser.html')
    else:
        return render_template('page/home.html')

@app.route('/pageVitrine', methods=['GET'])
def pageVitrine():
    listaItens = dao.carregarItensVitrine(dao.conectardb())

    if 'login' in session:
        login = session['login']
        return render_template('page/vitrine.html', login=login, listaItens=listaItens)
    else:
        return render_template('page/vitrine.html', listaItens=listaItens)

@app.route('/addItemVitrine', methods=['POST'])
def addItemVitrine():
    nomeItem = request.form.get('nomeItem')
    valorItem = float(request.form.get('valorItem'))
    qtdItem = int(request.form.get('qtdItem'))

    if dao.cadastrarItem(nomeItem, valorItem, qtdItem, dao.conectardb()):
        mgsCadastrado = 'Item cadastrado com sucesso!'
    else:
        mgsCadastrado = 'Erro: esse item já existe.'

    listaItens = dao.carregarItensVitrine(dao.conectardb())
    login = session['login']
    return render_template('page/vitrine.html', login=login, mgsCadastrado=mgsCadastrado, listaItens=listaItens)

@app.route('/pageCarrinho', methods=['GET'])
def pageCarrinho():
    if 'login' in session:
        return render_template('pageUser/carrinhoUser.html')
    else:
        return render_template('page/login.html')

@app.route('/pageLogin', methods=['GET'])
def pageLogin():
    return render_template('page/login.html')

@app.route('/login', methods=['POST'])
def login():
    login = request.form.get('login')
    senha = request.form.get('senha')
    query = dao.verificarLogin(login, senha, dao.conectardb())

    if query[0] > 0:
        session['login'] = login
        return render_template('pageUser/homeUser.html', hello=login)
    else:
        return render_template('page/login.html', msg='login ou senha incorreto')

@app.route('/pageCadastrar', methods=['GET'])
def pageCadastrar():
    return render_template('page/cadastro.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    login = request.form.get('login')
    senha = request.form.get('senha')
    resultado = dao.cadastrarUser(login, senha, dao.conectardb())

    if resultado:
        return render_template('page/login.html')
    else:
        return render_template('page/cadastro.html', msg="Login já usado")

@app.route('/sair')
def sair():
    if 'login' in session:
        session.pop('login')
        return render_template('page/home.html')
    else:
        return render_template('page/home.html')

if __name__ == '__main__':
    app.run(debug=True)