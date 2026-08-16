import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import re


survey = pd.read_csv("cleaned_data.csv")
wvs = pd.read_csv("WVS_Wave_7_Colombia_Csv_v5.1.csv")

WVS_COLUMN_TO_QUESTION = {
    "Q28": {
        "question": "When a mother works for pay, the children suffer",
        "scale": "1 Strongly agree, 2 Agree, 3 Disagree, 4 Strongly disagree",
        "survey": "question 6 (wvs #28)"
    },
    "Q29": {
        "question": "On the whole, men make better political leaders than women do",
        "scale": "1 Strongly agree, 2 Agree, 3 Disagree, 4 Strongly disagree",
        "survey": "question 8 (wvs #29)"
    },
    "Q30": {
        "question": "A university education is more important for a boy than for a girl",
        "scale": "1 Strongly agree, 2 Agree, 3 Disagree, 4 Strongly disagree",
        "survey": "question 9 (wvs #30)"
    },
    "Q31": {
        "question": "On the whole, men make better business executives than women do",
        "scale": "1 Strongly agree, 2 Agree, 3 Disagree, 4 Strongly disagree",
        "survey": "question 11 (wvs #31)"
    },
    "Q32": {
        "question": "Being a housewife is just as fulfilling as working for pay",
        "scale": "1 Strongly agree, 2 Agree, 3 Disagree, 4 Strongly disagree",
        "survey": "question 12 (wvs #32)"
    },
    "Q33": {
        "question": "When jobs are scarce, men should have more right to a job than women",
        "scale": "3 Neither, 1 Agree, 2 Disagree",
        "survey": "question 2 (wvs #33)",
        "custom_file": "WVS_Wave_7_Colombia_Csv_v5.1.csv", 
        "custom_header": "Q33_3"
    },
    "Q35": { 
        "question": "If a woman earns more money than her husband, it's almost certain to cause problems",
        "scale": "3 Neither, 1 Agree, 2 Disagree",
        "survey": "question 3 (wvs #35)",
        "custom_file": "WVS_Wave_7_Colombia_Csv_v5.1.csv", 
        "custom_header": "Q35_3"
    },
    "Q48": { ##check this one out
        "question": "Having a job is the best way for a woman to be an independent person.",
        "scale": "1 Agree, 2 Disagree, 3 Neither",
        "survey": "question 5 (wvs-6 #48)",
        "custom_file": "WV6_Data_Colombia_Csv_v20221117.csv", 
        "custom_header": "V48"
    },
    "Q182": { 
        "question": "Homosexuality",
        "scale": "1 1(Strongly Disagree), 2, 3, 4, 5, 6, 7, 8, 9, 10 10(Strongly Agree)",
        "survey": "homosexuality"
    },
    "Q183": { 
        "question": "Prostitution",
        "scale": "1 1(Strongly Disagree), 2, 3, 4, 5, 6, 7, 8, 9, 10 10(Strongly Agree)",
        "survey": "prostitution"
    },
    "Q184": { 
        "question": "Abortion",
        "scale": "1 1(Strongly Disagree), 2, 3, 4, 5, 6, 7, 8, 9, 10 10(Strongly Agree)",
        "survey": "abortion"
    },
    "Q185": { 
        "question": "Divorce",
        "scale": "1 1(Strongly Disagree), 2, 3, 4, 5, 6, 7, 8, 9, 10 10(Strongly Agree)",
        "survey": "divorce"
    },
    "Q186": {
        "question": "Sex before marriage",
        "scale": "1 1(Strongly Disagree), 2, 3, 4, 5, 6, 7, 8, 9, 10 10(Strongly Agree)",
        "survey": "premarital_sex"
    },
    "Q189": {
        "question": "For a man to beat his wife",
        "scale": "1 1(Strongly Disagree), 2, 3, 4, 5, 6, 7, 8, 9, 10 10(Strongly Agree)",
        "survey": "husband_hitting_wife"
    },
}


st.set_page_config(page_title="Charts", page_icon="📈")
options = {
    f"{k} : {meta['question']}"
    for k, meta in WVS_COLUMN_TO_QUESTION.items()
}

st.sidebar.title("Chart Controls")
st.sidebar.markdown("Select the question and display options.")

options = sorted(
    [f"{k} : {meta['question']}" for k, meta in WVS_COLUMN_TO_QUESTION.items()]
)

selected = st.sidebar.selectbox(
    "Question",
    options,
)

compare = st.sidebar.checkbox(
    "Compare side-by-side",
    value=False,
)

selected_wvs_col = selected.split(" :")[0]
wvs_meta = WVS_COLUMN_TO_QUESTION[selected_wvs_col]
selected_survey_col = wvs_meta["survey"]
response_label_map = {}
try:
    scale_parts = [p.strip() for p in str(wvs_meta.get("scale", "")).split(",") if p.strip()]
    for part in scale_parts:
        m = re.match(r"^(\d+)\s+(.*)$", part)
        if m:
            response_label_map[int(m.group(1))] = m.group(2).strip()
except Exception:
    response_label_map = {}



survey_counts = (survey[selected_survey_col].value_counts(dropna=True).sort_index())


if "custom_file" in wvs_meta:
    custom_df = pd.read_csv(wvs_meta["custom_file"])
    custom_col = wvs_meta["custom_header"]
    wvs_counts = custom_df[custom_col].value_counts(dropna=True).sort_index()
else:
    wvs_counts = wvs[selected_wvs_col].value_counts(dropna=True).sort_index()


all_responses = sorted(set(survey_counts.index).union(set(wvs_counts.index)))


comparison_df = pd.DataFrame({
    "response": all_responses,
    "response_label": [response_label_map.get(int(r), str(r)) for r in all_responses],
    "Guerrilla Respondents": [survey_counts.get(r, 0) for r in all_responses],
    "Civilian Respondents": [wvs_counts.get(r, 0) for r in all_responses],
})

max_survey_response = survey_counts.idxmax()
max_survey_count = int(survey_counts.max())
max_wvs_response = wvs_counts.idxmax()
max_wvs_count = int(wvs_counts.max())

max_survey_label = response_label_map.get(int(max_survey_response), str(max_survey_response))
max_wvs_label = response_label_map.get(int(max_wvs_response), str(max_wvs_response))

st.title(f":green[{wvs_meta['question']}]")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        label="Most Common Guerrilla Response",
        value=max_survey_label,
        delta=f"{max_survey_count} responses"
    )

with col2:
    st.metric(
        label=f"Most Common Civilian Response",
        value=max_wvs_label,
        delta=f"{max_wvs_count} responses"
    )

with st.expander("Question Information", expanded=False):
    st.write(f"**Guerrilla Survey Variable:** {selected_survey_col}")
    st.write(f"**World Values Survey Variable:** {selected_wvs_col}")
    st.write(f"**Response Scale:** {wvs_meta["scale"]}")

col1, col2, col3 = st.columns(3)
with col2:
    if not compare:
        st.write(f"**Scroll down to see the graphs ↓**")

total_guerrilla = comparison_df["Guerrilla Respondents"].sum()+1 #153
total_civilian = comparison_df["Civilian Respondents"].sum()
if compare:
    if total_guerrilla == 0:
        comparison_df["Guerrilla % of survey total"] = 0.0
    else:
        comparison_df["Guerrilla % of survey total"] = (
            comparison_df["Guerrilla Respondents"] / total_guerrilla * 100
        )

    if total_civilian == 0:
        comparison_df["Civilian % of survey total"] = 0.0
    else:
        comparison_df["Civilian % of survey total"] = (
            comparison_df["Civilian Respondents"] / total_civilian * 100
        )

    fig = px.bar(
        comparison_df,
        x="response_label",
        y=["Guerrilla % of survey total", "Civilian % of survey total"],
        barmode="group",
        custom_data=[
            comparison_df["Guerrilla Respondents"],
            comparison_df["Civilian Respondents"]
        ],
        labels={
            "value": "Percent of responses (within survey)",
            "response_label": "Responses",
        },
        title = "Side-by-Side Graph (Guerilla Combatants vs. Civilians)"
    )

    fig.data[0].marker.color = "#4E79A7"
    fig.data[1].marker.color = "#F28E2B"
    fig.data[0].hovertemplate = (
        "Percent: %{y:.2f}%<br>"
        f"Responses: %{{customdata[0]}} / {total_guerrilla}"
        "<extra></extra>"
    )

    fig.data[1].hovertemplate = (
        "Percent: %{y:.2f}%<br>"
        f"Responses: %{{customdata[1]}} / {total_civilian}"
        "<extra></extra>"
    )

    fig.update_yaxes(
        ticksuffix="%",
        rangemode="tozero"
    )

    st.plotly_chart(fig, use_container_width=True)

else:

    survey_dataframe = pd.DataFrame({
        "Responses":[response_label_map.get(int(v), str(v)) for v in survey_counts.sort_index().index],
        "Counts": survey_counts.sort_index().values
    })
    fig_survey = px.bar(
        survey_dataframe,
        x="Responses",
        y="Counts", 
        title = "Guerilla Combatants Survey Graph",
    )
    fig_survey.update_traces(
        marker_color="#4E79A7",
        hovertemplate = f"(%{{x}}, %{{y}}/{total_guerrilla})"
    )
    st.plotly_chart(fig_survey, use_container_width = True)


    wvs_dataframe = pd.DataFrame({
        "Responses":[response_label_map.get(int(v), str(v)) for v in wvs_counts.sort_index().index],
        "Counts": wvs_counts.sort_index().values
    })
    fig_wvs = px.bar(
        wvs_dataframe,
        x="Responses",
        y="Counts",
        title = "Civilian World Value Survey Graph"
    )
    fig_wvs.update_traces(
        marker_color="#F28E2B",
        hovertemplate = f"(%{{x}}, %{{y}}/{total_civilian})"
    )
    st.plotly_chart(fig_wvs, use_container_width = True)