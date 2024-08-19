import streamlit as st
import pandas as pd
import numpy as np  

# 1. Add the Title of the App
st.title('My First Streamlit App')

# 2. Add a Subheader
st.subheader('Data Analysis with Streamlit')

# 3. Displaying Text
st.text('Hello Streamlit')

# 4. Displaying Markdown
st.markdown('### This is a Markdown')

# 5. Displaying Data Frame

data = {
    'Name': ['Tom', 'Jerry', 'Mickey', 'Donald'],
    'Age': [10, 20, 30, 40]
}
df = pd.DataFrame(data)

st.write("this is a dataFrame",df)

# 6. Displaying Line Chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.write("## this is a line chart")
st.line_chart(chart_data)

# 7. Text Input

st.write("## Text Input")
text = st.text_input('Enter your Name')
st.write('Your Name:', text)

# 8. Slider
st.write("## Slider")
age = st.slider('Enter your Age', 1, 100,29)
st.write('Your Age:', age)

# 9. Button
st.write("## Button")
btn = st.button('Click Me')
if btn:
    st.write('Button is clicked')

# 10. Select box
st.write("## Select Box")
options = ['Python', 'Java', 'C++', 'C', 'Ruby']
choice = st.selectbox('Select your favorite Language', options)
st.write('You selected:', choice)

# 11. MultiSelect
st.write("## MultiSelect")
options = ['Python', 'Java', 'C++', 'C', 'Ruby']
choices = st.multiselect('Select your favorite Language', options)
st.write('You selected:', choices)

# 12. File Uploader
st.write("## File Uploader")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data)

# 13. Side Bar

st.sidebar.write("# Side Bar")
st.sidebar.write("This is a Side Bar")


# 14. Expander
st.write("## Expander")

with st.expander("See Explanation"):
    st.write("Explanation goes here")
    st.write("Here you could put in some really, really long explanations...")

# 15. Balloons and progress bar
st.write("## Balloons and Progress Bar")
if st.button('Show Balloons and Progress Bar'):
    st.balloons()
    st.write("Balloons are shown")
    my_bar = st.progress(0)
    import time 
    for percent_complete in range(20):
        time.sleep(0.09)
        my_bar.progress(percent_complete + 1)
    st.write("Progress Bar is completed")

# 16. Plotting

st.write("## Plotting")
import matplotlib.pyplot as plt

arr = np.random.normal(1, 1, size=100)
fig = plt.figure(figsize=(12, 6))
plt.hist(arr, bins=20,color='skyblue', edgecolor='black', linewidth=1.2, alpha=0.7)
plt.title('Histogram')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
st.pyplot(fig)





