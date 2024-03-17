from plyer import notification
from datetime import datetime
import pandas as pd
import requests
import sqlite3


'''Aviso em caso de falha'''
def alerta(nivel, base, etapa):

    hoje = datetime.now()
    hoje = hoje.strftime("%d/%m/%Y %H:%M:%S")

    message = f'Falha no carregamento da base {base} na etapa {etapa}.\n{hoje}'
    
    if nivel == 1:
        title = 'ATENÇÃO: Alerta Baixo',
    elif nivel == 2:
        title = 'ATENÇÃO: Alerta Médio',
    elif nivel == 3:
        title = 'ATENÇÃO: Alerta Alto',
    
    notification.notify(
        title = title,
        message = message,
        app_name = 'alerta',
        timeout = 10
        )


'''Banco de dados'''
def retrieve_table():
    conn = sqlite3.connect('zelda.db')
    query = "SELECT name FROM sqlite_master WHERE type='table'"
    schema = pd.read_sql_query(query,conn)

    conn.close()
    return schema

def save_db(df,table_name):
    conn = sqlite3.connect('zelda.db')
    df.to_sql(table_name, conn, if_exists='replace', index=False)

    conn.close()
    return True

def load_db(table_name):
    conn = sqlite3.connect('zelda.db')
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql(query,conn)

    conn.close()
    return df


'''Extração'''
def get_api(url):
    response = requests.get(url)

    if response.status_code == 200:
        data_json = response.json()
    else:
        print(f'Erro {response.status_code}')

def get_botw():
    url = 'https://botw-compendium.herokuapp.com/api/v3/compendium/all'
    data_json = data_json['data']
    zelda_df = pd.DataFrame(data_json)