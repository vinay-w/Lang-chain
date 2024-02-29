import streamlit
import streamlit as slt

import langchainhelper

slt.title("Restaurant name generetor")
cuisine=slt.sidebar.selectbox("Pick a cuisine",("Indian","American","Mexican","chinese","Italian"))

if cuisine:
    response=langchainhelper.generate_name(cuisine)
    slt.header(response['name'].strip())
    Menu_items=response['Menu'].strip().split(",")
    slt.write("**MENU ITEMS**")
    for item in Menu_items:
        slt.write("-", item)
