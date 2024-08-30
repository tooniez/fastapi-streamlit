import streamlit as st
from streamlit.testing.v1 import AppTest


def test_streamlit_app():
    # Create an instance of AppTest from file
    at = AppTest.from_file("app/streamlit_app.py")

    # Run the app
    at.run()

    print("test_streamlit_app completed successfully")
