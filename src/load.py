import logging


def guardar_csv(df, filename = "coingecko.csv"):
    df.to_csv(filename, index=False)
    logging.info(f"File, {filename}, saved successfully")


def guardar_excel(df, filename = "coingecko.xlsx"):
    df.to_excel(filename, index=False)
    logging.info(f"File, {filename} saved successfully")


