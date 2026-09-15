import streamlit as st
import pandas as pd

st.markdown("## Display Elements")

strcode = "print('Hello, World!')"
st.code(strcode, language="python")
st.markdown(" [google](https://www.google.com)")
st.markdown("|Column 1 | Column 2 | Column 3 | \n | --- | --- | --- | \n | Row 1, Col 1 | Row 1, Col 2 | Row 1, Col 3 | \n | Row 2, Col 1 | Row 2, Col 2 | Row 2, Col 3 |")

st.json({
    "name": "John Doe",
    "age": 30,
    "city": "New York"
})

st.markdown("This is how multiple emojis look like: 😄 😎 😍  🥳 🎉")

st.markdown("---")

st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

table = pd.DataFrame({
    'Column 1': [1, 2, 3, 4],
    'Column 2': [10, 20, 30, 40],
    'column 3': [100, 200, 300, 400]
})

st.table(table)
st.dataframe(table)