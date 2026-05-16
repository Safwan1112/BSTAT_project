import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)   # show all columns
pd.set_option('display.max_rows', None)      # shows all rows
pd.set_option('display.width', 1000)         # increase total width
pd.set_option('display.expand_frame_repr', False)  # prevent wrapping

from Gas_permit import gas_df
from Pluming_permits import plum_df
