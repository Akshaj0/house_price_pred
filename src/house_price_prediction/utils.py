import os
import sys
from src.house_price_prediction.exception import CustomException
from src.house_price_prediction.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from dotenv import load_dotenv
import pymysql
import pickle

load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
database = os.getenv("db")

def read_sql_data():
    logging.info("Reading data from MySql database")
    try:
        mydb= pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database  
        )
        logging.info("Connection successful")
        df = pd.read_sql_query("select * from house_values",mydb)
        print(df.head())
        return df
    
    except Exception as e:
        raise CustomException(e,sys)

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e,sys)