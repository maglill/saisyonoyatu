import streamlit as st


st.title('文字数カウントサイト')
st.write('')
#ただの改行
'このサイトは入力された文章の文字数をカウント出来るサイトです。'
'「文字数足りてるかな？」と思ったら活用してみて下さい。'
st.write('')
#ただの改行


text=st.text_input('↓　↓　↓　　入力してね　　↓　↓　↓')
#これ1つでテキストボックスも完備。

st.write('')
#ただの改行

n=len(text)
#textをnと置く。

if n==0:
    st.write('文字が入力されていないよ。')
    #未入力の時

if st.button('カウント'):
    st.write('文字数は',n,'です。')
    #ボタン押したとき文字数表示
    if n==0:
        st.write('ｎothing in the textbox.　ａre you kidding me　：△')    
    elif 1100<= n <=1300:
        st.write('およそA4一枚程度だよ。')
    elif 20000<= n <=40000:
        st.write('おおよそ卒業論文の文字数だよ。')
    else:
        st.write('')
