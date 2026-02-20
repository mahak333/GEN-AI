import streamlit as st
import pandas as pd
import numpy as np

st.title("My first stream lit app")
st.write(":streamlit: Hello mahak")
st.text("Lets start")

name=st.text_input("Enter name: ")
if st.button("Greet"):
    st.success(f"hello, {name} !")

df=pd.DataFrame(np.random.randn(10,2),columns=['A','B'])
st.line_chart(df)
st.bar_chart(df)

st.sidebar.title("Navigation")
st.image("https://i.pinimg.com/564x/a9/c2/dc/a9c2dc88da90a75c10ee66860eee6fd2.jpg",caption="cat")
st.video("https://youtu.be/wE8s993ZV-8?si=D7BHRYlNrk-PXp0m")

upload_files=st.file_uploader("C://Users//HP//Downloads//annual-enterprise-survey-2024-financial-year-provisional.csv", type='csv')
if upload_files:
    df=pd.read_csv(upload_files)
    st.dataframe(df)

st.title("abc Text and Markdown Demo")
st.header("This is a header")
st.subheader("this is a subehader")
st.markdown("**Bold**, *Italic*,'code',[Link](koi bhi link)")
st.code("for i in range(5): print(i)",language="python")

st.text_input("What's your name?")
st.text_area("Write something...")
st.number_input("Pick a number", min_value=0, max_value=100)
st.slider("Choose a range", 0, 100)
st.selectbox("Select a fruit", ["Apple", "Banana", "Mango"])
st.multiselect("Choose toppings", ["Cheese", "Tomato", "Olives"])
st.radio("Pick one", ["Option A", "Option B"])
st.checkbox("I agree to the terms")


if st.checkbox("Show details"):
    st.info("Here are more details...")

option=st.radio("Choose view",["Show Chart", "Show Table"])
if option== "Show Chart":
    st.write("Chart would appear here")
else:
    st.write("Table would appear here")

with st.form("login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type= "password")
    submitted = st.form_submit_button("Login")

if submitted:
    st.success(f"Welcome {username}")

col1,col2=st.columns(2)
with col1:
    st.button("Press me in column 1")
with col2:
    st.button("Press me in column 2")

with st.expander("See Explanation"):
    st.write("Here is a hidden message inside the expander.")


import matplotlib.pyplot as plt 
fig, ax = plt.subplots()
ax.plot([1,2,3],[1,4,9])
st.pyplot(fig)


import plotly.express as px
df = px.data.iris()
fig = px.scatter(df,x="sepal_width",y="sepal_length",color="species")
st.plotly_chart(fig)
                            
