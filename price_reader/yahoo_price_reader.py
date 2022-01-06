# coding: utf-8
import pandas as pd
from pandas_datareader import data as wb

AMD = wb.DataReader('AMD', data_source='yahoo', start='1995-1-1')
print(AMD)
