# coding=utf-8
import streamlit as st
import pandas as pd
import numpy as np
import os
import plotly.express as px
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

# -- Create sidebar for plot controls
st.sidebar.markdown('## 控制台')

#-- Set time by GPS or event
select_event = st.sidebar.selectbox('选择瓦斯预测模型',
                                    ['模型1', '模型2', '模型3'])

if select_event == '模型1':

    rootPath = './data/20201016'
    filenames = sorted(os.listdir(rootPath), key=lambda x:int(x.split('.')[0][-2:]))
    df1 = pd.read_csv(os.path.join(rootPath, filenames[0]), encoding=u'gbk')
    for filename in filenames[1:]:
        print(filename)
        df = pd.read_csv(os.path.join(rootPath, filename), encoding=u'gbk')
        df1 = pd.concat([df1, df], ignore_index=True)

    df1['时间'] = pd.to_datetime(df1['时间'], format='%Y/%m/%d %H:%M')
    df1.set_index('时间', inplace=True)

    t1 = df1.loc[df1.地点=='8470运料巷配巷掘进面甲烷T1', '检测值']
    t1 = pd.to_numeric(t1)
    t1 = t1.values[:15]
    st.write(t1)
    print(t1)

    t4 = df1.loc[df1.地点=='8470运料巷配巷掘进面分风口甲烷T4', '检测值']
    t4 = pd.to_numeric(t4)
    t4 = t4.values

    fig = px.line(t1)
    fig2 = px.line(t4)

    f = plt.figure()
    plt.plot(t1)

    f2 = plt.figure()
    plt.plot(t4)

    # Plot!
    st.title('传感器T1')
    st.plotly_chart(f, use_container_width=True)

    st.title('传感器T4')
    st.plotly_chart(f2, use_container_width=True)

    st.title('T4预测结果')
    st.plotly_chart(f2, use_container_width=True)


elif select_event == '模型2':
    st.title('模型2预测结果')

    rootPath = './data/20201016'
    filenames = os.listdir(rootPath)
    df1 = pd.read_csv(os.path.join(rootPath, filenames[0]), encoding=u'gbk')
    for filename in filenames[1:]:
        #print(filename)
        df = pd.read_csv(os.path.join(rootPath, filename), encoding=u'gbk')
        df1 = pd.concat([df1, df], ignore_index=True)

    df1['时间'] = pd.to_datetime(df1['时间'], format='%Y/%m/%d %H:%M')
    df1.set_index('时间', inplace=True)

    t4 = df1.loc[df1.地点=='8470运料巷配巷掘进面分风口甲烷T4', '检测值']
    t4 = pd.to_numeric(t4)

    fig = px.scatter(t4)

    # Plot!
    st.plotly_chart(fig, use_container_width=True)

    st.title('传感器原始数据')
    st.plotly_chart(fig, use_container_width=True)

else:
    st.title('模型3预测结果')
    # chart_data = pd.DataFrame(
    #      np.random.randn(20, 3),
    #      columns=['g', 'h', 'i'])
    # st.line_chart(chart_data)
    pass



# import streamlit as st
# import plotly.graph_objs as go
# # st.set_page_config(layout="wide")
# c1, c2, c3, c4, c5 = st.columns([0.05,1.5,0.2,1.5,0.2])
# with c1:
#     st.empty()
# with c2:
#     #柱状图
#     trace_basic = [go.Bar(
#                 x = ['分类1', '分类2', '分类3', '分类4', '分类5'],
#                 y = [1, 2, 3, 2, 4],
#                 textposition="outside",
#                 text = [1, 2, 3, 2, 4],
#                 marker_color=['#ff3385', '#ff00ff', '#ffff1a', '#1aff1a', '#00ccff']
#         )]
#     layout_basic = go.Layout(
#                 title = '柱状图',
#                 xaxis_tickangle=-45
#         )
#     figure_basic = go.Figure(data = trace_basic, layout = layout_basic)
#     # Plot
#     st.plotly_chart(figure_basic)
#
#
#     #饼图
#     labels=['股票', '债券', '现金', '衍生品', '其他']
#     values=[33.7, 20.33, 9.9, 8.6, 27.47]
#     trace=[go.Pie(labels=labels,
#                   values=values,
#                   texttemplate=[33.7, 20.33, 9.9, 8.6, 27.47],
#                   textposition="outside",
#                   hole=0.5,
#                   hoverinfo='label+percent')
#            ]
#     layout=go.Layout(
#         title='饼图'
#     )
#     fig=go.Figure(data=trace,layout=layout)
#     st.plotly_chart(fig)
#
#     #散点图
#     trace = go.Scatter(
#         x = [1,3,5,7,9,10,7,5,9],
#         y = [3,7,5,9,2,6,7,9,10],
#         mode = 'markers',# 纯散点图
#         marker=dict(
#         size=10,
#         color = 'rgba(255, 182, 193, .9)',
#         line = dict(
#             width = 1,
#             color = 'blue'
#         )
#       )
#     )
#     data=[trace]
#     layout=go.Layout(
#         title='散点图'
#     )
#     fig=go.Figure(data=data,layout=layout)
#     st.plotly_chart(fig)
#
# with c3:
#     st.empty()
# with c4:
#     #折线图
#     trace1 = go.Scatter(
#         x = [1,2,3,4,5,6,7,8,9],
#         y = [3,7,5,9,2,6,7,9,10],
#         name = '第一组数据',
#         mode = 'lines',
#         text = [3,7,5,9,2,6,7,9,10],
#     )
#     trace2 = go.Scatter(
#         x = [1,2,3,4,5,6,7,8,9],
#         y = [5,3,5,6,9,10,9,5,6],
#         name = '第一组数据',
#         mode = 'lines+markers',
#     )
#     data=[trace1, trace2]
#     layout=go.Layout(
#         title='散点图'
#     )
#     fig = go.Figure(data=data,layout=layout)
#     st.plotly_chart(fig)
#
#     #箱型图
#     c1 = [0, 1, 1, 2, 3, 5, 8, 13, 21]
#     c2 = [1, 2, 3, 5, 7, 9, 15, 21, 33]
#
#     trace1 = go.Box(y=c1,fillcolor="#ff7500",marker_color="#ff7500",name="ABC")
#     trace2 = go.Box(y=c2,fillcolor="#16a951",marker={'color':"#16a951"},name="DEF")
#
#     data = [trace1,trace2]
#     layout = go.Layout(plot_bgcolor='#ffffff',width=500,height=500,title='箱型图')
#     fig = go.Figure(data=data,layout=layout)
#     st.plotly_chart(fig, layout=layout)
#
#     #漏斗图
#     trace0 = go.Funnel(
#         y = ["注册", "实名认证", "绑卡", "合格投资者", "投资", "复投"],
#         x = [220, 180, 160, 80, 40, 20],
#         textinfo = "value+percent initial",
#         marker=dict(color=["deepskyblue"]*6),
#         connector = {"line": {"color": "royalblue", "dash": "solid", "width": 3}})
#
#     trace1 = go.Funnel(
#         y = ["注册", "实名认证", "绑卡", "合格投资者", "投资", "复投"],
#         x = [320, 280, 140, 99, 55, 23],
#         textinfo = "value+percent initial",
#         marker=dict(color=["green"]*6),
#         connector = {"line": {"color": "lightsalmon", "dash": "solid", "width": 3}})
#     data = [trace0, trace1]
#     layout = go.Layout(title='漏斗图')
#     fig = go.Figure(data=data,layout=layout)
#     st.plotly_chart(fig, layout=layout)
# with c5:
#     st.empty()
