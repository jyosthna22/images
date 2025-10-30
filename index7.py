
import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Cartoon")

    with st.popover("Cartoon Images"):
        img_col1, img_col2, img_col3 = st.columns(3)

        with img_col1:
            st.image("https://up.yimg.com/ib/th/id/OIP.uMXSbhe_djLlVackcKQm3AHaFj?pid=Api&rs=1&c=1&qlt=95&w=138&h=140", width=100)

        with img_col2:
            st.image("https://tse1.mm.bing.net/th/id/OIP.vrbopt9dj0VSm784eXvGzAHaHa?pid=Api&P=0&h=180", width=100)

        with img_col3:
            st.image("https://tse4.mm.bing.net/th/id/OIP.i4jdvmobDvmT-LI9EOSDhgHaHY?pid=Api&P=0&h=180", width=100)
with col2:
    st.header("Nature")
    with st.popover("Nature Images"):
        img_col1, img_col2, img_col3 = st.columns(3)

        with img_col1:
            st.image("https://tse4.mm.bing.net/th/id/OIP.JPogPMSOOv8g9WJdtLUluAHaEe?pid=Api&P=0&h=180", width=150)

        with img_col2:
            st.image("https://tse1.mm.bing.net/th/id/OIP.5rHJf7QWh2i9mGPLkQwHcgHaEK?pid=Api&P=0&h=180", width=150)

        with img_col3:
            st.image("https://tse2.mm.bing.net/th/id/OIP.rgQSpH6aLr8DYQtvhMiZmgHaEK?pid=Api&P=0&h=180", width=150)
    

with col3:
    st.header("Places")
    with st.popover("Tourist place Images"):
        img_col1, img_col2, img_col3 = st.columns(3)

        with img_col1:
            st.image("https://tse2.mm.bing.net/th/id/OIP.po8dZR50vqzPE7L54UFt3QHaE8?pid=Api&P=0&h=180", width=150)

        with img_col2:
            st.image("https://tse1.mm.bing.net/th/id/OIP.mCKAUjSSEz1XQi7mxQH35gHaEK?pid=Api&P=0&h=180", width=150)

        with img_col3:
            st.image("https://tse2.mm.bing.net/th/id/OIP.YbSfNrF-GgygmzUAkCkhigHaFG?pid=Api&P=0&h=180", width=150)