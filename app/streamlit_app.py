import streamlit as st
import requests

# OAuth login (to be implemented)
# ...


def main():
    # Use st.write with HTML for the title
    st.write("<h1>FastAPI Streamlit Demo</h1>", unsafe_allow_html=True)

    # Demo GET request
    if st.button("Get Data"):
        response = requests.get("http://localhost:8000/")
        st.write(response.json())

    # Demo POST request
    data = st.text_input("Enter data to post:")
    if st.button("Post Data"):
        # Endpoint to be implemented in the API
        response = requests.post("http://localhost:8000/demo_post", json={"data": data})
        st.write(response.json())


if __name__ == "__main__":
    main()
