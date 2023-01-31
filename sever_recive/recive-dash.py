import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px
from flask import request
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import time

app = Dash(__name__,
           #external_stylesheets=['../assets/css/bootstrap.min.css'],
           external_stylesheets=['https://cdn.staticfile.org/twitter-bootstrap/4.5.2/css/bootstrap.min.css'],
           suppress_callback_exceptions=True)

app.layout = html.Div(
    dbc.Container(
        [
            html.H1('羊城矿-42采区回风改造风速'),
            #dcc.Graph(id='output1')
            dbc.Button('开始计算', id='start', n_clicks=0, color='light'),
            html.Br(),
            dcc.Dropdown(
                id='province',
                options=[
                    {'label': '四川省', 'value': '四川省'},
                    {'label': '陕西省', 'value': '陕西省'},
                    {'label': '广东省', 'value': '广东省'}
                ],
                value='四川省'
            ),
            dcc.Loading(dcc.Graph(id='output1')),
            dcc.Loading(dcc.Graph(id='output2'))
        ],
        fluid=True
    )

)


@app.server.route('/upload', methods=['POST'])
def save_file():

    data = request.files
    file = data['file']
    file.save(file.filename + '.csv')
    # df = pd.read_csv(file, encoding=u'gbk')
    # df['时间'] = pd.to_datetime(df['时间'], format='%Y/%m/%d %H:%M')
    # df.set_index('时间', inplace=True)
    # b = df.loc[df.地点=='42采区回风改造风速', '检测值']
    # b = pd.to_numeric(b)
    # print(b)
    # fig = px.line(b, markers='o')
    return 'ok'


# 对应app实例的回调函数装饰器
@app.callback(
    Output(component_id='output1', component_property='figure'),
    #Input(component_id='start', component_property='n_clicks'),
    Input(component_id='province', component_property='value'),
    prevent_initial_call=True
)
def input_to_output(x):
    '''
    简单的回调函数
    '''
    print('123')
    time.sleep(0.2)  # 增加应用的动态效果
    print(x)
    df = pd.read_csv('new_1.csv', encoding=u'gbk')
    df['时间'] = pd.to_datetime(df['时间'], format='%Y/%m/%d %H:%M')
    df.set_index('时间', inplace=True)
    b = df.loc[df.地点=='42采区回风改造风速', '检测值']
    b = pd.to_numeric(b)
    print(b)


    fig = px.line(b, markers='o')

    return fig

# 对应app实例的回调函数装饰器
@app.callback(
    Output(component_id='output2', component_property='figure'),
    Input(component_id='start', component_property='n_clicks'),
    prevent_initial_call=True
)
def input_to_output2(x):
    '''
    简单的回调函数
    '''
    print('123')
    time.sleep(0.2)  # 增加应用的动态效果
    print(x)
    df = pd.read_csv('new_1.csv', encoding=u'gbk')
    df['时间'] = pd.to_datetime(df['时间'], format='%Y/%m/%d %H:%M')
    df.set_index('时间', inplace=True)
    b = df.loc[df.地点=='42采区回风改造风速', '检测值']
    b = pd.to_numeric(b)
    print(b)


    fig = px.line(b, markers='o')

    return fig

#fig = px.scatter(x=range(10), y=range(10))
#fig = px.line(b, markers='o')



if __name__ == '__main__':
    app.run_server(port=8787)