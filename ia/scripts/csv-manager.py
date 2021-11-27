import os
from numpy import integer, result_type
import pandas as pd
import math 


amoni =pd.read_csv(os.path.dirname(__file__) + "/dataset/amoni.csv")
water = pd.read_csv(os.path.dirname(__file__) + "/dataset/aigua.csv")
air = pd.read_csv(os.path.dirname(__file__) + "/dataset/aire.csv")

result = amoni.set_index('row_date').join(water.set_index('row_date'),lsuffix= "_amoni",rsuffix="_water",how = "inner")
result = result.join(air.set_index('row_date'),how = "inner")
result = result[["value_amoni","value_water","value","is_drift","dangerous_drift"]]
res_len = len(result.index)
train = result.iloc[:math.trunc(res_len*0.8),:]
test = result.iloc[math.trunc(res_len*0.8):,:]
train.to_csv(os.path.dirname(__file__) + "/dataset/train.csv")
test.to_csv(os.path.dirname(__file__) + "/dataset/test.csv")
