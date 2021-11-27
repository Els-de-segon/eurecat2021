import os
import pandas as pd

os.chdir("/dataset/amoni.csv")
amoni =pd.read_csv("/dataset/amoni.csv")
print(amoni)
