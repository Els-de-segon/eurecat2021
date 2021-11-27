import os
import pandas as pd


amoni =pd.read_csv(os.path.dirname(__file__) + "/dataset/amoni.csv")
water = pd.read_csv(os.path.dirname(__file__) + "/dataset/aigua.csv")
air = pd.read_csv(os.path.dirname(__file__) + "/dataset/aire.csv")

result = amoni.set_index('row_date').join(water.set_index('row_date'),how = "inner",lsuffix= "_amoni",rsuffix="_water")
result = result.join(air.set_index('row_date'),how = "inner")
result = result[["value_amoni","value_water","value","is_drift","dangerous_drift"]]
result.to_csv(os.path.dirname(__file__) + "/dataset/data.csv")