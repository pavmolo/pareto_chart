# Import required libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import uuid
import base64

# Build data frame
uploaded_file = st.file_uploader("Выберите XLSX файл", accept_multiple_files=False)
data = pd.read_excel(uploaded_file)
data_columns = data.columns[1:]
data_fin = data.copy()
data_fin = data_fin.set_index(data_fin.columns[0])
for column in data_columns:
  df = data[[column]]
  df = df.sort_values(by=column, ascending=False)

  # Add cumulative percentage column
  data_fin[f"cum_percentage_{column}"] = round(df[column].cumsum()/df[column].sum()*100,2)

  # Set figure and axis
  fig, ax = plt.subplots(figsize=(22,10))

  # Plot bars (i.e. frequencies)
  ax.bar(data_fin.index, data_fin[column])
  ax.set_title("Pareto Chart")
  ax.set_xlabel("Medication Error")
  ax.set_ylabel("Frequency");

  # Second y axis (i.e. cumulative percentage)
  ax2 = ax.twinx()
  ax2.plot(data_fin.index, data_fin[f"cum_percentage_{column}"], color="red", marker="D", ms=7)
  ax2.axhline(80, color="orange", linestyle="dashed")
  ax2.yaxis.set_major_formatter(PercentFormatter())
  ax2.set_ylabel("Cumulative Percentage")
  st.pyplot(fig)
st.dataframe(data_fin)
