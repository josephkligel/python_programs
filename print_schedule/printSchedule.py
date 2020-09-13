import pandas as pd
import os

schedule = pd.read_excel(os.path.join(os.path.dirname(__file__), 'lib/schedule.xlsx'))
print(schedule)
