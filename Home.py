import pandas as pd
import streamlit as st
import re

survey = pd.read_csv('cleaned_data.csv')
st.set_page_config(page_title="FARC Gender Attitudes", page_icon="🏚️", layout="wide")

st.image("images/img5.jpg", caption="Teach-In with FARC excombatants on the parallels of their guerrilla insurgency with that of the Kurdish PKK-YPG. Tierra Grata, Colombia. (October 2021)")

st.divider()

st.title("Introduction - FARC Gender Attitudes Dashboard", text_alignment="center")
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

st.space("small") 

st.image("images/img1.jpg", caption="Mural reading #SantrichLibre in the Pondores ETCR - a federally designated transitional rural zone for FARC excombatant reinsertion into civilian life. (May 2021)")
st.space("xsmall") 
st.image("images/img2.jpg", caption="Dr. Fernández conducting a field interview with one of the female excombatant leaders of the Gender Task Force (“Mesa de Género”). Tierra Grata ETCR Camp. (August 2021).")
st.space("xsmall") 
st.image("images/img3.jpg", caption="Conducting interviews in the field with ex-combatants of the Colombian FARC. (All images used are with the explicit informed consent of the interviewee.) Tierra Grata, Colombia. (August 2021)")
st.space("xsmall") 
st.image("images/img4.jpg", caption="Interview with a prominent male excombatant leader of the Gender Task Force. These gendered and differential stipulations were explicitly negotiated by the FARC in the 2016 Colombian Peace Deal. (June 2021)")

st.divider()
st.space("xsmall") 

st.markdown(
    "**Use the sidebar on each page** to choose a survey question and adjust the view. "
    "The Raw Data page shows response counts and percentages for former FARC combatants, "
    "while the Chart Comparisons page lets you compare those responses with civilian "
    "World Values Survey data and toggle side-by-side comparison charts."
)

st.write("")
left_space, col1, col2, right_space = st.columns([1, 1.2, 1.2, 1])

with col1:
    if st.button("Raw Data Page →", use_container_width=True):
        st.switch_page("pages/01_Raw Data.py")

with col2:
    if st.button("Chart Comparisons Page →", use_container_width=True):
        st.switch_page("pages/02_Chart Comparisons.py")
