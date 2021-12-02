# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 17:13:04 2021

@author: nao
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 11:21:44 2021

@author: nao
"""

import time
import streamlit as st
from PIL import Image


st.title("おめでとうございます。")
st.write("あなたは2021年間ビジターアンケートの参加者に選ばれました！")
st.write("Chrome「ありがとう」を込めてApple iPhone 13 Pro が当たる")
st.write("チャンスを差し上げます！")

#iPhineの画像入れる。
img=Image.open('sumaho.png')
st.image(img, caption='iPhone13Pro',use_column_width=True)

st.write('iPhone13Pro')
st.write('定価：￥146800')
st.write('期間限定：￥500')

st.write("")
st.write("")
st.write("以下の質問に答えて下さい。")
st.write("")

option=st.selectbox("1日に約何時間ネットを見ますか？",list(['1','2','3','4','5','それ以上']))

option=st.selectbox("普段何時間SNSを見ますか？",list(['1','2','3','4','5','それ以上']))

option=st.selectbox("普段何時間動画を見ますか？",list(['1','2','3','4','5','それ以上']))




st.write("")#改行のためにおいた。
st.write("")


status_area = st.empty()

# カウントダウン
count_down_sec = 10
for i in range(count_down_sec):
    # プレースホルダーに残り秒数を書き込む
    status_area.write( f'あと {count_down_sec - i}   秒で自動的に申請されます。')
    # スリープ処理を入れる
    time.sleep(1)

status_area.write('回答を送信しております。しばらくお待ち下さい。')

latest_iteration = st.empty() #空コンテンツと⼀緒に変数を作成
bar = st.progress(0)#プログレスを作る 値は０
for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')#空のIterationにテキストを⼊れていく
    bar.progress(i +1)#barの中⾝をぐいぐい増やしていく
    time.sleep(0.01)
    
st.write("申請が完了しました。")

st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")

st.text("以下にあなたの情報を入力して下さい。")
st.text_input("お名前")
st.text_input("住所")
st.text_input("電話番号")
st.text_input("連絡の取れるメールアドレス")
st.write("")
st.text_input("何か要望があればお書き下さい。")

st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
###################################################################################################################################################
#回答送信ボタン
st.text('※回答送信には時間がかかります。')
if st.button('送信'):
    st.balloons()
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write('本部への送信が完了致しました。')
    st.write('お届け予定日は４月１日以降です。')
    st.balloons()
else:
    st.write('')


#################################################################################################################################################







