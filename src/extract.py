import logging

import requests

def obtener_datos(config):
    coin = config["coin"]
    parametros = {
         "vs_currency": config["vs_currency"],
        "days": config["days"],
    }
    url = f'https://api.coingecko.com/api/v3/coins/{coin}/market_chart'
    logging.info(f"Retrieving data from CoinGecko for '{coin}'")
    response = requests.get(url, params=parametros)
    data = response.json()
    logging.info(f"{len(data['prices'])} records have been received")
    return response.json()






