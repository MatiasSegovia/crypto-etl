import logging

import pandas as pd

def transformar_datos(data):
    df = pd.DataFrame(data['prices'], columns=["timestamp",'price'])
    logging.info("JSON → DataFrame conversion completed")
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    logging.info("Timestamp-to-datetime conversion completed")
    return df



