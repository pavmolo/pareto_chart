# Import required libraries
import streamlit as st
import pandas as pd
import numpy as np
from plotly.graph_objects import Figure, Scatter, Bar

input_row = st.columns(2)
with input_row[0]:
  uploaded_file = st.file_uploader("Выберите XLSX файл", accept_multiple_files=False)


if uploaded_file:
  with input_row[1]:
    st.markdown('Если хотите скачать график файлом **Нажмите на значек фото**.')
    st.image('https://i.ibb.co/5Yn0CpP/2023-06-02-22-53-06.png')
  
  # Build data frame
  df = pd.read_excel(uploaded_file)
  for i in df.columns[1:]:
    df_1 = df.set_index(df.columns[0])[i]
    df_1 = df_1.sort_values(ascending=False)
    df_2 = round(df_1.cumsum()/df_1.sum()*100,2)
    data = pd.concat([df_1, df_2], axis=1)
    data.columns = [i, 'cumsum']
    quantile_02 = data[i].quantile(0.2)
    quantile_lover = data[i].tail((data[i] <= quantile_02).sum()).sum()
    quantile_higher = data[i].head((data[i] > quantile_02).sum()).sum()
    total = quantile_lover + quantile_higher
    quantile_lover_share = (quantile_lover / total) * 100
    quantile_higher_share = (quantile_higher / total) * 100
    df_total = pd.DataFrame([[quantile_higher_share, quantile_lover_share]], columns = ['20% "голова" содержит, %%', '80% "хвост" содержит, %%'], index = [i])
    
    
    # транформируем датасет для случая слишком длинного датасета
    if len(data) > 25:
      if len(data) < 250:
        q = data[i].quantile(0.2)
      else:
        q = data[i].quantile(0.2)
      head_quant = (data[i] > q).sum()
      tail_quant = (data[i] <= q).sum()
      data_without_tail = data.head(head_quant)
      data_tail = data.tail(tail_quant)
      #data = data_without_tail.append(pd.Series(data_tail.sum()), ignore_index=True)
      data = pd.concat([data_without_tail, pd.Series(data_tail.sum(), index=data_without_tail.columns, name='Прочее').to_frame().T], axis=0)
      #st.dataframe(data)
    # Выводим график Парето
    data = [Bar(name = 'Объем',  x= data.index, y= data[i], marker= {"color": list(np.repeat('rgb(16, 50, 115)', 5)) + list(np.repeat('rgb(0, 163, 194)', len(data.index) - 5))}),
            Scatter(line= {"color": "rgb(233, 72, 64)", "width": 3}, name= "Суммарные проценты", x=  data.index, y= data['cumsum'], yaxis= "y2", mode='lines+markers'),]
    layout = {"title": {'text': f"Парето {i}", 'font': dict(size=30)}, "font": {"size": 14, "color": "rgb(44, 44, 84)", "family": "Arial"},
              "margin": {"b": 20, "l": 50, "r": 50, "t": 10,}, "height": 800, "width": 1200,
              "plot_bgcolor": "rgb(255, 255, 255)", "legend": {"x": 0.79, "y": 1.1, "font": {"size": 12, "color": "rgb(16, 50, 115)", "family": "Arial"}, 'orientation': 'h',},
              "yaxis": {"title": i, "titlefont": {"size": 16, "color": "rgb(71, 71, 135)", "family": "Arial"},}, 
              "yaxis2": {"side": "right", "range": [0, 100], "title": i, "titlefont": {"size": 16, "color": "rgb(71, 71, 135)", "family": "Arial"}, "overlaying": "y", "ticksuffix": " %",},}
    fig = Figure(data=data, layout=layout)
    st.plotly_chart(fig)
    st.title('Таблица парето')
    st.table(df_total)
    st.markdown('----------------------------------------------------')
    st.markdown('----------------------------------------------------')
    st.markdown('----------------------------------------------------')
else:
  st.markdown('Подготовьте файл эксель по следующей форме **следующей форме**.')
  st.markdown('Столбец может быть один. Если столбцов несколько для одних и тех же строк, то для каждого из них в отдельности будет создано Парето')
  st.markdown('После того, как подготовите файл закачайте его, нажав **Browse Files**.')
  st.image('https://i.ibb.co/2nkXKds/2023-06-02-22-43-43.png')
