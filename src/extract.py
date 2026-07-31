import logging

import requests

def obtener_datos(config):
    coin = config["coin"]
    parametros = {
         "vs_currency": config["vs_currency"],
        "days": config["days"],
    }
    url = f'https://api.coingecko.com/api/v3/coins/{coin}/market_chart'
    logging.info(f"Solicitando datos de CoinGecko para '{coin}'")
    response = requests.get(url, params=parametros)
    data = response.json()
    logging.info(f"Se recibieron {len(data['prices'])} registros")
    return response.json()






