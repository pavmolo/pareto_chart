# Import required libraries
import streamlit as st
import pandas as pd
import uuid
import base64
import numpy as np
from plotly.graph_objects import Figure, Scatter, Bar

# Build data frame
uploaded_file = st.file_uploader("Выберите XLSX файл", accept_multiple_files=False)
data = pd.read_excel(uploaded_file)
data = data[[data.columns[0]]]
#data_columns = data.columns[1:]
st.dataframe(data)
"""
for column in data_columns:
  df = data[[data_columns[0], column]]
  df = df.sort_values(by=column, ascending=False)
  df = df.set_index(data_columns[0])
  # Add cumulative percentage column
  df[f"cum_percentage"] = round(df[column].cumsum()/df[column].sum()*100,2)

  # Set figure and axis
  data = [Bar(name = "Count",  x= df.index, y= df[f'{col}_count'], marker= {"color": list(np.repeat('rgb(71, 71, 135)', 5)) + list(np.repeat('rgb(112, 111, 211)', len(df.index) - 5))}),
          Scatter(line= {"color": "rgb(192, 57, 43)", "width": 3}, name= "Percentage", x=  df.index, y= df['cumulative'], yaxis= "y2", mode='lines+markers'),]
  layout = {"title": {'text': f"{col} Pareto", 'font': dict(size=30)}, "font": {"size": 14, "color": "rgb(44, 44, 84)", "family": "Times New Roman, monospace"},
            "margin": {"b": 20, "l": 50, "r": 50, "t": 10,}, "height": 400, 
            "plot_bgcolor": "rgb(255, 255, 255)", "legend": {"x": 0.79, "y": 1.2, "font": {"size": 12, "color": "rgb(44, 44, 84)", "family": "Courier New, monospace"}, 'orientation': 'h',},
            "yaxis": {"title": f"Count {col}", "titlefont": {"size": 16, "color": "rgb(71, 71, 135)", "family": "Courier New, monospace"},}, 
            "yaxis2": {"side": "right", "range": [0, 100], "title": f"Percentage {col}", "titlefont": {"size": 16, "color": "rgb(71, 71, 135)", "family": "Courier New, monospace"}, "overlaying": "y", "ticksuffix": " %",},}
  fig = Figure(data=data, layout=layout)
st.dataframe(data_fin)
"""
