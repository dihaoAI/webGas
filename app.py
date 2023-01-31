import matplotlib.pyplot as plt
import pandas as pd
import os

rootPath = './data/20201016'
filenames = os.listdir(rootPath)
df1 = pd.read_csv(os.path.join(rootPath, filenames[0]), encoding=u'gbk')
for filename in filenames[1:]:
    #print(filename)
    df = pd.read_csv(os.path.join(rootPath, filename), encoding=u'gbk')
    df1 = pd.concat([df1, df], ignore_index=True)

df1['时间'] = pd.to_datetime(df1['时间'], format='%Y/%m/%d %H:%M')
df1.set_index('时间', inplace=True)

t1 = df1.loc[df1.地点=='8470运料巷配巷掘进面甲烷T1', '检测值']
t4 = df1.loc[df1.地点=='8470运料巷配巷掘进面分风口甲烷T4', '检测值']
t1 = pd.to_numeric(t1)
t4 = pd.to_numeric(t4)

# print(t1)
# print(t4)
#df = pd.read_csv('./data/_2020-10-16_2020-10-16 01.csv', encoding=u'gbk')
#df_values = df.values  # ndarray
# df['时间'] = pd.to_datetime(df['时间'], format='%Y/%m/%d %H:%M')
# df.set_index('时间', inplace=True)
# b = df.loc[df.地点=='8470运料巷配巷掘进面甲烷T1', '检测值']
# b = pd.to_numeric(b)
# plt.plot(b, marker='o')
# plt.show()
# c = df.loc[df.地点=='42采区回风改造风速']['时间']
#
# ser = pd.concat([c, b], axis=1)
# d = pd.to_datetime(ser['时间'], format='%Y/%m/%d %H:%M')
#
#
# #print(df.loc[df.地点=='42采区回风改造风速'])
# print(d)






import dash
print(dash.__version__)
# 2.7.0
# 1.19.0

from dash import Dash, html, dcc
# from dash import Dash
# import dash_html_components as html
# import dash_core_components as dcc

import plotly.express as px
from dash.dependencies import Input, Output

app = Dash(__name__)

#fig = px.scatter(x=range(10), y=range(10))
fig = px.line(t1, markers='o')
fig2 = px.line(t4, markers='o')

app.layout = html.Div(
    [
        html.Br(),
        html.H1('请选择瓦斯预测模型'),
        dcc.Dropdown(
            id='xaxis-column',
            options=[
                {'label': '模型1', 'value': 'm1'},
                {'label': '模型2', 'value': 'm2'},
                {'label': '模型3', 'value': 'm3'}
            ],
            value = 'm1'
        ),

        html.Br(),
        html.Br(),
        html.Br(),

        #html.H1(id='city'),
        #html.H1('羊城矿-8470运料巷配巷掘进面甲烷T1'),
        #dcc.Graph(figure=fig),
        html.H1('羊城矿-8470运料巷配巷掘进面甲烷T1'),
        dcc.Graph(id='indicator-graphic'),

        html.Br(),

        html.H1('羊城矿-8470运料巷配巷掘进面甲烷T4'),
        dcc.Graph(figure=fig2)
    ]
)



@app.callback(
    Output('indicator-graphic', 'figure'),
    Input('xaxis-column', 'value'))
def update_graph(xaxis_column_name):

    print(xaxis_column_name)
    if xaxis_column_name == 'm1':
        fig = px.line(t1, markers='o')
    elif xaxis_column_name == 'm2':
        fig = px.line(t4, markers='o')
    else:
        fig = px.scatter(t1)


    return fig





if __name__ == '__main__':
    app.run_server(debug=True, port=8787)