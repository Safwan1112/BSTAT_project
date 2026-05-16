import pandas as pd

pd.set_option('display.max_columns', None)   # show all columns
pd.set_option('display.max_rows', None)      # shows all rows
pd.set_option('display.width', 1000)         # increase total width
pd.set_option('display.expand_frame_repr', False)

plum_df = pd.read_csv('Plumbing_Permits.csv', low_memory = False)
plum_df = plum_df.dropna(axis=1, how='all')

plum_df['STATUS'] = plum_df['STATUS'].replace('ISSUE','ISSUED')
