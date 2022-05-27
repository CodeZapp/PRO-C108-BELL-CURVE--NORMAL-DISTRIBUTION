import plotly.figure_factory as ff
import pandas as pd
df = pd.read_csv('bellCurveData.csv')
fig = ff.create_distplot([df['Avg Rating'].tolist()], ['Avg Rating'])
fig.show()