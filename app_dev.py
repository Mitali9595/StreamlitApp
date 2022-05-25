import streamlit as st
import base64
from PIL import Image

#st.header('This is a header')
st.image('Logo.png', width=100)


#bgcolor = st.color_picker("#A9BDF9")
#fontcolor = st.color_picker("Pick a Font Color","#fff")

html_temp = """
<div style="background-color:{};padding:10px">
<h1 style="color:{};text-align:center;">Welcome User </h1>
</div>
"""
st.markdown(html_temp.format("#3789FB","#F9F7F7"),unsafe_allow_html=True)
#st.markdown("<div><p style='color:{}'>Hello Streamlit</p></div>".format("#3789FB"),unsafe_allow_html=True)


with st.sidebar:
    st.subheader('Hi Mitali..!')
    button1 = st.button("📆 Calendar")
    button2 = st.button("News Letter")
    button3 = st.button("My Connections")


C1=st.container()
C1.title("Dataset Library")
col1,col2,col3,col4= st.columns(4)
Category=col1.selectbox("Select Category",["Choice1","Choice2","Choice3"])
Sub_entity=col2.selectbox("Select Sub-entity",["Choice1","Choice2","Choice3"])
Entity=col3.selectbox("Select Entity",["Choice1","Choice2","Choice3"])
#Search=col4.write("Search")
query = col4.text_input("Search", "")
col4.write(f"Query = '{query}'")

C2=st.container()
C2.title("POV")
col1, col2, col3 = st.columns(3)

image = Image.open('Picture1.png')
col1.subheader("Recommender")
col1.image(image, caption='Recommender System using Neo4j')
#agree = col2.checkbox("Read More")
if col1.checkbox("Recommender - Read More"):
        def show_pdf(file_path):
            with open(file_path,"rb") as f:
                  base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)
        st.write(show_pdf("Recommender.pdf"))



image = Image.open('Picture2.png')
col2.subheader("Time Series")
col2.image(image, caption='Time Series Basics')

if col2.checkbox("Time Series - Read More"):
        def show_pdf(file_path):
            with open(file_path,"rb") as f:
                  base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)
        st.write(show_pdf("TimeSeries.pdf"))

image = Image.open('Picture3.png')
col3.subheader("Cell Detection")
col3.image(image, caption='Cell Detection using PyTorch')

if col3.checkbox("Cell Detection - Read More"):
        def show_pdf(file_path):
            with open(file_path,"rb") as f:
                  base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)
        st.write(show_pdf("Cell.pdf"))







