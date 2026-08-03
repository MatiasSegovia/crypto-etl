import logging
def validar_datos(df):
    if df.empty:
        raise ValueError("Data not found")
    if df.isnull().values.any():
        logging.warning("Zero values were found")
        raise ValueError("✖️ Zero values were found")

    logging.info("Data Validation Complete")
    return df



