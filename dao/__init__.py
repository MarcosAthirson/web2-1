import psycopg2

def conectardb():
    con = psycopg2.connect(
        #host='localhost',
        #database='loja',
        #user='postgres',
        #password='12345'

        host = 'dpg-cu7995a3esus73fhpalg-a.oregon-postgres.render.com',
        database = 'bancoweb2',
        user = 'bancoweb2_user',
        password = 'WcFOjr0Yq8TzefZeZp1XD0lvd8xRDJrK'
    )
    return con

def verificarLogin(login, senha, conexao):
    cur = conexao.cursor()
    cur.execute(f"select count(*) from usuarios where login = '{login}' and senha = '{senha}'")
    resultado = cur.fetchone()
    cur.close()
    conexao.close()
    return resultado

def cadastrarUser(login, senha, conexao):
    cur = conexao.cursor()
    exito = False

    try:
        cur.execute(f"INSERT INTO usuarios (login, senha) VALUES('{login}', '{senha}')")
    except psycopg2.IntegrityError:
        conexao.rollback()
        exito = False
    else:
        conexao.commit()
        exito = True

    cur.close()
    conexao.close()
    return exito

def cadastrarItem(nomeItem, valorItem, qtdItem, conexao):
    cur = conexao.cursor()
    exito = False

    try:
        cur.execute(f"insert into itens (nomeitem, valoritem, qtditem) values ('{nomeItem}', '{valorItem}', '{qtdItem}')")
    except psycopg2.IntegrityError:
        conexao.rollback()
        exito = False
    else:
        conexao.commit()
        exito = True

    cur.close()
    conexao.close()
    return exito

def carregarItensVitrine(conexao):
    cur = conexao.cursor()
    cur.execute(f"select * from itens")
    resultado = cur.fetchall()
    cur.close()
    conexao.close()
    return resultado
