import pandas as pd
import streamlit as st
import re

survey = pd.read_csv('cleaned_data.csv')
st.set_page_config(page_title="FARC Gender Attitudes", page_icon="🏚️", layout="wide")

st.title("Introduction - FARC Gender Attitudes Dashboard")
#st.caption("Survey tables and comparison charts for gender attitude questions")

st.markdown(
    "This original dataset contains survey data collected from **153 former combatants "
    "of the Revolutionary Armed Forces of Colombia (FARC)** during fieldwork in Colombia "
    "in October 2021. The survey, based largely on questions from the **World Values "
    "Survey (Wave 7)**, measures former insurgents' attitudes toward **gender roles, "
    "gender equality, and social norms between men and women**, alongside demographic "
    "characteristics such as age, race/ethnicity, and marital status. The data form part "
    "of a broader mixed-methods research project examining the gendered attitudes of "
    "Global South insurgents from Colombia and Kurdistan and asking whether participation "
    "in armed struggle can transform individual attitudes and perceptions of gender "
    "roles. More broadly, the project explores whether and how war and insurgency can "
    "create the conditions for feminist transformation, and the extent to which these "
    "wartime changes endure after demobilization and transition into civilian life."
)

st.markdown(
    "Use the sidebar on each page to choose a survey question and adjust the view. "
    "The Raw Data page shows response counts and percentages for former FARC combatants, "
    "while the Chart Comparisons page lets you compare those responses with civilian "
    "World Values Survey data and toggle side-by-side comparison charts."
)

st.write("")
left_space, col1, col2, right_space = st.columns([1, 1.2, 1.2, 1])

with col1:
    if st.button("Raw Data Page 📈", use_container_width=True):
        st.switch_page("pages/01_Raw Data.py")

with col2:
    if st.button("Chart Comparisons Page 📊", use_container_width=True):
        st.switch_page("pages/02_Chart Comparisons.py")
