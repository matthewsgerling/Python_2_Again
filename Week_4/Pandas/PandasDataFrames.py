import pandas as pd
weekTemps = pd.read_csv("Week_Temps.csv",sep=',',index_col='Day of the Week')

weekSnow = pd.read_csv("Week_Snow.csv",sep=',',index_col='Day of the Week')
