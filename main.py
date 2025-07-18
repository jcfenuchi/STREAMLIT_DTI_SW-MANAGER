import streamlit as st
import pandas as pd
import mongo_client

st.set_page_config(layout="wide")

pages = {
    "Dashboards" : [
        st.Page("web_switch.py", title='Switches'),
        st.Page("web_accesspoint.py", title='Access Points'),
    ],
    "Resources": [
        st.Page("scripts.py", title='Scripts'),
    ],
}


pg = st.navigation(pages)
pg.run()
