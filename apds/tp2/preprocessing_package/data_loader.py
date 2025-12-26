import logging
import pandas as pd

logger = logging.getLogger(__name__)


class CSVReader:
    """
    A simple class to read CSV files and preview their contents.

    Attributes:
        file_path (str): The path to the CSV file to be read.

    Methods:
        read(): Reads the CSV file into a pandas DataFrame.
        preview(df, n): Returns the first n rows of the given DataFrame.
    """

    def __init__(self, filepath: str):
        self.file_path = filepath
        logger.info(f"CSVReader initialized with file: {self.file_path}")

    def read(self):
        try:
            df = pd.read_csv(self.file_path)
            logger.info(f"CSV file '{self.file_path}' read sucessfully.")
            return df
        except FileNotFoundError:
            logger.error(f"File at {self.file_path} not found")
            return None

    def preview(self, df, n):
        if df is not None:
            logger.info(f"Previewing the first {n} rows of the DataFrame.")
            return df.head(n)
        else:
            logger.warning("No DataFrame to preview.")
            return None
