import logging
def validar_datos(df):
    if df.empty:
        raise ValueError("Datos no encontrado")
    if df.isnull().values.any():
        logging.warning("Se encontraron valores nulos")
        raise ValueError("✖️ se encontraron valores nulos")

    logging.info("Validación de datos completada")
    return df



