three_charts.py

# adapted from: https://plot.ly/python/pie-charts/
#https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/plotly.md

import plotly
import plotly.graph_objs as go

labels = ["Oxygen", "Hydrogen", "Carbon_Dioxide", "Nitrogen"]
values = [4500, 2500, 1053, 500]

trace = go.Pie(labels=labels, values=values)

plotly.offline.plot([trace], filename="basic_pie_chart.html", auto_open=True)