import plotly.figure_factory as ff
import pandas as pd
import csv

df = pd.read_csv("dataaaa.csv")
fig = ff.create_distplot([df["Avg Rating"].tolist()], ["Avg Ration"], show_hist=False)
fig.show()
