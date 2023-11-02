from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

# ...

with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 4000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)
    
    # 追加のUIコンポーネントをここに配置
    color = st.color_picker('Choose a color for the spiral', '#0068c9')
    shape = st.selectbox('Choose the shape of the points', ['circle', 'square', 'triangle', 'star'])
    opacity = st.slider('Opacity of the spiral points', 0.0, 1.0, 0.5)
    point_size = st.slider('Size of the points on the spiral', 1, 100, 10)
    density = st.slider('Density of points on spiral', 0.1, 2.0, 1.0)
    show_tooltip = st.checkbox('Show tooltip on hover')

    Point = namedtuple('Point', 'x y')
    data = []

    # スパイラルの点を生成するループを更新
    points_per_turn = total_points / (num_turns * density)
    for curr_point_num in range(int(total_points * density)):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / (total_points * density)
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    # アルタイチャートの描画部分を更新
    chart = alt.Chart(pd.DataFrame(data), height=500, width=500).mark_point(
        shape=shape,  # マークの形状を変更
        color=color,  # マークの色を変更
        opacity=opacity,  # マークの透明度を変更
        size=point_size  # マークのサイズを変更
    ).encode(
        x='x:Q',
        y='y:Q',
        tooltip='index:N' if show_tooltip else None  # ツールチップの設定を追加
    )

    st.altair_chart(chart)
