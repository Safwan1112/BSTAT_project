import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)   # show all columns
pd.set_option('display.max_rows', None)      # shows all rows
pd.set_option('display.width', 1000)         # increase total width
pd.set_option('display.expand_frame_repr', False)  # prevent wrapping

gas_df = pd.read_csv("Gas_Permits.csv")

# print(df['STATUS'].describe()) # Shows count as 36231 should be 39k rows around 3k missing rows

# print(len(df.columns)) There are 68 columns in the raw data sheet not sure how many are completely null


gas_df= gas_df.dropna(axis=1, how='all') # dropped all null columns now 19 columns removed 49 columns

gas_df['STATUS'] = gas_df['STATUS'].replace('ISSUE','ISSUED')

# print(df['STATUS'].unique()) : The Status column is now clean

# print(df.columns) :  All the columns ['X', 'Y', 'OBJECTID', 'STATUS', 'LATITUDE_WGS', 'LONGITUDE_WGS', 'PERMITNO', 'APPL_DATE',
# 'ISSDATE', 'OWNER_NAME', 'OWNER_ADD', 'P_ADDRESS', 'P_ST_NAME', 'P_ST_NO', 'DESCRIPTION_TYPE',
# 'DESC_WORK', 'ZIP', 'LATITUDE', 'LONGITUDE']

# print(df['DESCRIPTION_TYPE'].unique())
# print(df.head())
residential_gas_df = gas_df[gas_df['DESCRIPTION_TYPE'] == 'RESIDENTIAL GAS']
commercial_gas_df = gas_df[gas_df['DESCRIPTION_TYPE'] == 'COMMERCIAL GAS']
# print(df['STATUS'].unique())
