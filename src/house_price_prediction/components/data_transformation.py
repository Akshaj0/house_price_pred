import sys
import os
import pandas as pd
import numpy as np
from dataclasses import dataclass
from sklearn.preprocessing import MinMaxScaler,OrdinalEncoder
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from src.house_price_prediction.exception import CustomException
from src.house_price_prediction.logger import logging
from src.house_price_prediction.utils import save_object
from sklearn.compose import ColumnTransformer

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("artifacts", "preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
        self.numerical_columns = ['MSSubClass',
                                    'OverallQual',
                                    'YearRemodAdd',
                                    '1stFlrSF',
                                    'GrLivArea',
                                    'BsmtFullBath',
                                    'Fireplaces',
                                    'GarageCars']
        self.categorical_columns = ['MSZoning',
                                        'Neighborhood',
                                        'RoofStyle',
                                        'BsmtQual',
                                        'BsmtExposure',
                                        'HeatingQC',
                                        'CentralAir',
                                        'KitchenQual',
                                        'FireplaceQu',
                                        'GarageType',
                                        'GarageFinish',
                                        'PavedDrive',
                                        'SaleCondition']
        self.overall_columns = self.numerical_columns + self.categorical_columns
    
    def get_data_transformation_object(self):
        '''
        This function is responsible for data transformation
        '''
        try:
            logging.info("Data transformation initiated")
            # numerical_columns = ['MSSubClass',
            #                     'OverallQual',
            #                     'YearRemodAdd',
            #                     '1stFlrSF',
            #                     'GrLivArea',
            #                     'BsmtFullBath',
            #                     'Fireplaces',
            #                     'GarageCars']
            # categorical_columns = ['MSZoning',
            #                         'Neighborhood',
            #                         'RoofStyle',
            #                         'BsmtQual',
            #                         'BsmtExposure',
            #                         'HeatingQC',
            #                         'CentralAir',
            #                         'KitchenQual',
            #                         'FireplaceQu',
            #                         'GarageType',
            #                         'GarageFinish',
            #                         'PavedDrive',
            #                         'SaleCondition']
            # overall_columns = numerical_columns + categorical_columns

            num_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", MinMaxScaler())
                ]
            )

            cat_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy='constant', fill_value='missing')),
                    ("ordinal_encoder", OrdinalEncoder()),
                    ("scaler", MinMaxScaler())
                ]
            )

            logging.info(f"Categorical columns: {self.categorical_columns}")
            logging.info(f"Numerical columns: {self.numerical_columns}")

            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline", num_pipeline, self.numerical_columns),
                    ("cat_pipeline", cat_pipeline, self.categorical_columns)
                ]
            )

            return preprocessor
        


        except Exception as e:
            raise CustomException(e, sys)
        
    
    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Read train and test data completed")
            logging.info("Obtaining preprocessing object")

            preprocessing_obj = self.get_data_transformation_object()

            required_columns = self.overall_columns
            target_column_name = "SalePrice"

            input_feature_train_df = train_df[required_columns]
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df[required_columns]
            target_feature_test_df = test_df[target_column_name]

            logging.info(
                "Applying preprocessing object on training and testing dataframe."
            )

            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object.")

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
        

        except Exception as e:
            raise CustomException(e, sys)