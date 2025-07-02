'''
Steps for ingestion:
1. Set the path for raw, training, and test sets. --> using dataclasses
2. Initalize the ingestion method() ==>  RETURNS BOTH TRAIN AND TEST DATASET FILE PATHS.
    a. Load the dataset.
    b. Make the directory from raw datapath given in step 1
    c. Store the raw data set in the given location in step 1. 
    d. Split the dataset in to train and test sets using train test split.
    e. Save both the splitted datasets in the given locations in the config. 
    f. Return both training and test set locations. 
'''

import os
import sys


from sklearn.model_selection import train_test_split
import pandas as pd

from src.logger import logging
from src.exception import CustomExcetion

from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    raw_set_path = os.path.join('artifacts', 'raw_dataset.csv')
    train_set_path = os.path.join('artifacts', 'train_dataset.csv')
    test_set_path = os.path.join('artifacts', 'test_dataset.csv')

class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
    
    def initialize_data_ingestion(self):
        pass

