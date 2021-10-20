# -*- coding: utf-8 -*-
from pathlib import Path
import pandas as pd
import logging
logger = logging.getLogger('main_logger')

import constants as cst

def read_csv_from_path(path: Path):
    """
    Reads a csv from a path
    Args:
        path: path of the file to read

    Returns: dataframe

    """
    df = pd.read_csv(path,sep=";")
    if df.shape[1] == 1:
        df = pd.read_csv(path, sep=",")
    logger.debug('Read file: '+ path)

    return df

def write_csv_from_path(df: pd.DataFrame, path: Path):
    """
    Writes the dataframe to the correct file path
    Args:
        df: dataframe to write
        path: local file path from constants 
    """
    df.to_csv(path, sep=";", index=False)
    logger.debug('Wrote file in: '+ path)