from preprocessing_package.data_loader import CSVReader
from preprocessing_package.data_cleaner import DropMissing
from preprocessing_package.config import Config

# import the file path
config = Config()
FILE_PATH = config.FILE_PATH

# read the csv
csv = CSVReader(FILE_PATH)
df = csv.read()

# drop the missing value
cleaner = DropMissing(df)
if df is not None:
    df_clean = cleaner.drop_missing(df)
    print(df_clean.head())
