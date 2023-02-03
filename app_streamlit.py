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
        #print(filename)
        df = pd.read_csv(os.path.join(rootPath, filename), encoding=u'gbk')
        df1 = pd.concat([df1, df], ignore_index=True)

    df1['时间'] = pd.to_datetime(df1['时间'], format='%Y/%m/%d %H:%M')
    df1.set_index('时间', inplace=True)

    t1 = df1.loc[df1.地点=='8470运料巷配巷掘进面甲烷T1', '检测值']
    t1 = pd.to_numeric(t1)
    # t1 = t1.values
    # st.write(t1)
    # print(t1)

    t4 = df1.loc[df1.地点=='8470运料巷配巷掘进面分风口甲烷T4', '检测值']
    t4 = pd.to_numeric(t4)
    #t4 = t4.values

    fig = px.line(t1, markers=True)
    fig2 = px.line(t4, markers=True)

    # f = plt.figure()
    # plt.plot(t1)
    #
    # f2 = plt.figure()
    # plt.plot(t4)

    # Plot!
    st.title('传感器T1')
    st.plotly_chart(fig, use_container_width=True)

    st.title('传感器T4')
    st.plotly_chart(fig2, use_container_width=True)

    st.title('传感器T4(预测结果)')
    st.plotly_chart(fig2, use_container_width=True)


elif select_event == '模型2':
    rootPath = './data/20201016'
    filenames = sorted(os.listdir(rootPath), key=lambda x:int(x.split('.')[0][-2:]))
    df1 = pd.read_csv(os.path.join(rootPath, filenames[0]), encoding=u'gbk')
    for filename in filenames[1:]:
        #print(filename)
        df = pd.read_csv(os.path.join(rootPath, filename), encoding=u'gbk')
        df1 = pd.concat([df1, df], ignore_index=True)

    df1['时间'] = pd.to_datetime(df1['时间'], format='%Y/%m/%d %H:%M')
    df1.set_index('时间', inplace=True)

    t1 = df1.loc[df1.地点=='8470运料巷配巷掘进面甲烷T1', '检测值']
    t1 = pd.to_numeric(t1)

    t4 = df1.loc[df1.地点=='8470运料巷配巷掘进面分风口甲烷T4', '检测值']
    t4 = pd.to_numeric(t4)

    fig = px.line(t1, markers=True)
    fig['data'][0]['line']['color'] = '#f00056'
    fig['data'][0]['line']['width'] = 1
    fig2 = px.line(t4, markers=True)
    fig2['data'][0]['line']['color'] = '#f00056'
    fig2['data'][0]['line']['width'] = 1

    # Plot!
    st.title('传感器T1')
    st.plotly_chart(fig, use_container_width=True)

    st.title('传感器T4')
    st.plotly_chart(fig2, use_container_width=True)

    st.title('传感器T4(预测结果)')
    st.plotly_chart(fig2, use_container_width=True)


else:
    st.title('传感器T1')

    st.title('传感器T4')

    st.title('传感器T4(预测结果)')
    # chart_data = pd.DataFrame(
    #      np.random.randn(20, 3),
    #      columns=['g', 'h', 'i'])
    # st.line_chart(chart_data)
    pass
