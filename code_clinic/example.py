import pandas as pd
from csv import DictReader
import numpy as np

# data = pd.read_csv('Exercise_Files/Ch01/resources/Environmental_Data_Deep_Moor_2012.txt', sep='\t')
# print(data[1])

csv_data = DictReader('Exercise_Files/Ch01/resources/Environmental_Data_Deep_Moor_2012.txt')
data_array = np.array(csv_data)
print(list(csv_data))
