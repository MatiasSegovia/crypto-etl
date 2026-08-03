import logging
import json
from src.transform import transformar_datos
from src.validate import validar_datos
from src.extract import obtener_datos
logging.basicConfig(filename="logs/crypto_etl.log",
                    encoding= "utf-8",
                    level=logging.INFO,
                    format='%(asctime)s : %(levelname)s : %(message)s')

def main():
    try:
        logging.info("Start of the ETL process")
        with  open("config.json", "r") as f:
            config = json.load(f)
            logging.info("Settings loaded successfully")
            data = obtener_datos(config)
            df = transformar_datos(data)
            df = validar_datos(df)
            from src.load import guardar_excel,guardar_csv
            guardar_excel(df)
            guardar_csv(df)
            logging.info("ETL completed successfully.")
    except Exception :
        logging.exception("An error occurred during the ETL run.")



if __name__ == "__main__":
    main()