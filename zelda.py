from plyer import notification
from datetime import datetime
import pandas as pd
import requests

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

url = 'https://botw-compendium.herokuapp.com/api/v3/compendium/all'


response = requests.get(url)

if response.status_code == 200:
    data_json = response.json()
else:
    print(f'error')

data_json = data_json['data']

zelda_df = pd.DataFrame(data_json)

name = [name for name in zelda_df['name']]
local = [loc for loc in zelda_df['common_locations']]
category = [cat for cat in zelda_df['category']]
loot = [drop for drop in zelda_df['drops']]

items_df = pd.DataFrame({
    'Nome': name,
    'Região': local,
    'Categoria': category,
    'Loot': loot})

items_reg_exploded = items_df.explode('Região', ignore_index=True)
items_loot_exploded = items_reg_exploded.explode('Loot', ignore_index=True)
items_loot = items_loot_exploded.dropna()