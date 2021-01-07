import plotly.figure_factory as pf
import pandas as ps
import csv

df = ps.read_csv("C:/Users/HOME/Downloads/bellcurve.csv")
fig = pf.create_distplot([df["weight"].tolist()],["weight"],show_hist = False)
fig.show()