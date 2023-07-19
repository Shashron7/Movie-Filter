import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(page_title="Sales_Dashboard", page_icon=":bar_chart:", layout="wide")

df = pd.read_csv("imdb_1000.csv")
st.header("Movies based on your preference:")
# Now you can work with the DataFrame as needed
print(df.head())  



st.sidebar.markdown("<span style='font-size: 50px; font-family: Times New Roman;'> Filter here:</span>", unsafe_allow_html=True)

genres = st.sidebar.multiselect("Select your genre:", options=df["genre"].unique())

actor=st.sidebar.text_input("Enter the actor name:")



# df_selection=df[df["genre"].isin(genres)]
filtered_df = df[df['actors_list'].apply(lambda x: any(item in x for item in [actor])) & df["genre"].isin(genres)]
st.dataframe(filtered_df, width=1500)


col1, col2, col3 = st.columns(3)
with col1:
    st.image("poster1.jpeg", width=300)
    
with col2:
    st.image("poster2.jpeg", width=300)

with col3:
    st.image("poster3.jpeg", width=300)
    
    
    


hover_style = """
<style>
    .hover-text:hover {
        color: red;
        cursor: pointer;
    }
    .hover-text{
        font-size: 40px;
        margin-left:400px;
    }
</style>
"""

# Write the CSS style using st.markdown
st.markdown(hover_style, unsafe_allow_html=True)

# Display the text with the hover effect
st.markdown('<p class="hover-text">Happy Watching !</p>', unsafe_allow_html=True)
