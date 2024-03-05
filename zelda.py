from plyer import notification
from datetime import datetime
import pandas as pd
import requests

hoje = datetime.now()
hoje = hoje.strftime("%d/%m/%Y %H:%M:%S")

def alerta():
    notification.notify(
    title = 'Erro',
    message = f'Não foi possível acessar a API.\n{hoje}',
    app_name = 'Zelda',
    timeout = 10)

url = 'https://botw-compendium.herokuapp.com/api/v3/compendium/all'
response = requests.get(url)

if response.status_code == 200:
    data_json = response.json()
else:
    print(alerta())

data_json = data_json['data']
zelda_df = pd.DataFrame(data_json)

print(zelda_df.head(0))
print('----------------------------------------')


name = [zelda_df['name'] for zelda_df in data_json]
local = [zelda_df['common_locations'] for zelda_df in data_json]
category = [zelda_df['category'] for zelda_df in data_json]

items_df = pd.DataFrame({
    'Nome': name,
    'Região': local,
    'Categoria': category})

print(items_df.head(10))
print('----------------------------------------')


effect = zelda_df['cooking_effect']
heal = zelda_df['hearts_recovered']

effect_df = pd.DataFrame({
    'Nome': name,
    'Efeito': effect,
    'Cura': heal})

print(effect_df.head(10))
print('----------------------------------------')