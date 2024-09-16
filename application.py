from src.house_price_prediction.logger import logging
from src.house_price_prediction.exception import CustomException
import sys
from src.house_price_prediction.components.data_ingestion import DataIngestion
from src.house_price_prediction.components.data_ingestion import DataIngestionConfig
from src.house_price_prediction.components.data_transformation import DataTransformation
from src.house_price_prediction.components.data_transformation import DataTransformationConfig
from src.house_price_prediction.components.model_trainer import ModelTrainer
from src.house_price_prediction.components.model_trainer import ModelTrainerConfig

if __name__ == "__main__":
    logging.error("We are testing logging")

    try:
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

        data_transformation = DataTransformation()
        train_array, test_array, _ = data_transformation.initiate_data_transformation(train_data_path, test_data_path)

        model_trainer=ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_array, test_array))


    except Exception as e:
        raise CustomException(e,sys)