from src.house_price_prediction.logger import logging
from src.house_price_prediction.exception import CustomException
import sys
from src.house_price_prediction.components.data_ingestion import DataIngestion
from src.house_price_prediction.components.data_ingestion import DataIngestionConfig

if __name__ == "__main__":
    logging.error("We are testing logging")

    try:
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()

    except Exception as e:
        raise CustomException(e,sys)