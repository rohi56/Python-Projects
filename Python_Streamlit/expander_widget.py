import streamlit as st

tab1, tab2, tab3 = st.tabs(["JavaScript", "Python", "Java"])

with tab1:
    st.header("JavaScript")
    st.image("javascript.png")
    with st.expander("More about JavaScript"):
        st.write("JavaScript is a versatile programming language primarily used for web development. It allows developers to create interactive and dynamic web pages, enabling features such as form validation, animations, and real-time updates. JavaScript can be executed on the client side (in the browser) or on the server side (using Node.js). It is an essential technology for building modern web applications.")

with tab2:
    st.header("Python")
    st.image("python.png")
    with st.expander("More about Python"):
        st.write("Python is a high-level, interpreted programming language known for its simplicity and readability. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming. Python is widely used in web development, data analysis, artificial intelligence, scientific computing, and automation. Its extensive standard library and active community make it a popular choice for developers of all skill levels.")

with tab3:
    st.header("Java")
    st.image("java.png")
    with st.expander("More about Java"):
        st.write("Java is a versatile, object-oriented programming language designed to be platform-independent. It follows the principle of 'write once, run anywhere,' allowing developers to create applications that can run on any device with a Java Virtual Machine (JVM). Java is widely used for building enterprise-level applications, Android apps, web applications, and large-scale systems. Its strong community support and extensive libraries make it a popular choice for developers worldwide.")