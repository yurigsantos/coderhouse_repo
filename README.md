<p align="center">
  <source media="(prefers-color-scheme: dark)">
  <img alt="BOTW Logo" src="docs/botw.png" length=10% width=10%>
</p>

<h2 align="center">Guia para Legend of Zelda: Breath of the Wild</h2>


Um banco de dados para facilitar o acesso aos recursos disponíveis no mundo de **Hyrule**.\
Com as tabelas disponíveis é possível acessar cada item específico, sua localização, ou até mesmo todos de uma região.

## Processo
### Criação das tabelas:
- tabela item: mostra cada recurso único e onde encontrar
- tabela food: mostra os recursos consumíveis que curam e seus possíveis efeitos
- tabela compendium: tabela bruta onde se tem tudo disponível ao mesmo tempo

### Tratamento das tabelas:
Como cada linha da tabela common_locations e drops estava em lista para acomodar as várias regiões
onde determinado recurso estaria disponível foi utilizado a função DataFrame.explode() para tornar cada elemento em único, sendo assim tendo uma mesma id com index diferentes.\
DataFrame.dropna() para se desfazer dos elementos vazios onde seria necessário ter informação,\
DataFrame.fillna() para efeitos de visualização da tabela bruta,\
DataFrame.drop(columns=) para se desfazer de colunas sem informação relevante,\
DataFrame[columns].apply(astype()) para corrigir erro de formato não lido pelo sql.

## Equipe

* **Mateus**  - [@mateus-na](https://github.com/mateus-na)
* **Victor**  - [@victorspacheco](https://github.com/victorspacheco)
* **Yuri**    - [@yurigsantos](https://github.com/yurigsantos)

## Fonte
Feito com [Hyrule Compendium API](https://gadhagod.github.io/Hyrule-Compendium-API/#/compendium-api)