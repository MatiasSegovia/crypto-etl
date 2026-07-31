import logging

import pandas as pd

def transformar_datos(data):
    df = pd.DataFrame(data['prices'], columns=["timestamp",'price'])
    logging.info("Transformación JSON → DataFrame completada")
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    logging.info("Conversión de timestamp a datetime completada")
    return df



