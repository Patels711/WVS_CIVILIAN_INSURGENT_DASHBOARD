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
    "Q33": { ##check this one out
        "question": "When jobs are scarce, men should have more right to a job than women",
        "scale": "3 Neither, 1 Agree, 2 Disagree",
        "survey": "question 2 (wvs #33)",
        "custom_file": "WVS_Wave_7_Colombia_Csv_v5.1.csv", 
        "custom_header": "Q33_3"
    },
    "Q35": { ##check this one out
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
    "Q182": { ##check the scale to make all of it show up + labels for 1 + 10
        "question": "Homosexuality",
        "scale": "1, 2, 3, 4, 5, 6, 7, 8, 9, 10",
        "survey": "homosexuality"
    },
    "Q183": { ##check the scale to make all of it show up + labels for 1 + 10
        "question": "Prostitution",
        "scale": "1, 2, 3, 4, 5, 6, 7, 8, 9, 10",
        "survey": "prostitution"
    },
    "Q184": { ##check the scale to make all of it show up + labels for 1 + 10
        "question": "Abortion",
        "scale": "1, 2, 3, 4, 5, 6, 7, 8, 9, 10",
        "survey": "abortion"
    },
    "Q185": { ##check the scale to make all of it show up + labels for 1 + 10
        "question": "Divorce",
        "scale": "1, 2, 3, 4, 5, 6, 7, 8, 9, 10",
        "survey": "divorce"
    },
    "Q186": { ##check the scale to make all of it show up + labels for 1 + 10
        "question": "Sex before marriage",
        "scale": "1, 2, 3, 4, 5, 6, 7, 8, 9, 10",
        "survey": "premarital_sex"
    },
    "Q189": { ##check the scale to make all of it show up + labels for 1 + 10
        "question": "For a man to beat his wife",
        "scale": "1, 2, 3, 4, 5, 6, 7, 8, 9, 10",
        "survey": "husband_hitting_wife"
    },
}


st.set_page_config(page_title="Charts", page_icon="📈")
st.title("Charts Testing")
options = {
    f"{k} : {meta['question']}"
    for k, meta in WVS_COLUMN_TO_QUESTION.items()
}
selected = st.selectbox("Choose your comparison question", options)
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

st.write("Selected Question: ", wvs_meta["question"])
st.write("Survey Column: ", selected_survey_col.capitalize())
st.write(" WVS Column: ", selected_wvs_col)
st.write(
    "Max category in Survey (selected_survey_col):",
    max_survey_label,
    "=>",
    max_survey_count,
    "responses",
)
st.write(
    "Max category in WVS (selected_wvs_col):",
    max_wvs_label,
    "=>",
    max_wvs_count,
    "responses",
)
compare = st.checkbox("Check this box if you want to compare the data in a side-by-side", value=False)

if compare:
    total_guerrilla = comparison_df["Guerrilla Respondents"].sum()
    total_civilian = comparison_df["Civilian Respondents"].sum()

    # avoid divide-by-zero
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
        labels={
            "value": "Percent of responses (within survey)",
            "response_label": "Responses",
        },
    )

    fig.data[0].marker.color = "#4E79A7"
    fig.data[1].marker.color = "#F28E2B"

    fig.update_yaxes(
        ticksuffix="%",
        rangemode="tozero"
    )

    st.plotly_chart(fig, use_container_width=True)

else:
    fig_survey = go.Figure()
    fig_survey.add_trace(go.Bar(
        x=[response_label_map.get(int(v), str(v)) for v in survey_counts.sort_index().index],

        y=survey_counts.sort_index().values,
        marker_color="#4E79A7",  
        name="Survey"
    ))
    fig_survey.update_layout(
        xaxis_title="Guerilla Responses",##survey_meta["question"]
        yaxis_title="Respondent Count",
        template="plotly_white",
    )
    st.plotly_chart(fig_survey, use_container_width=True)

    fig_wvs = go.Figure()
    fig_wvs.add_trace(go.Bar(
        x=[response_label_map.get(int(v), str(v)) for v in wvs_counts.sort_index().index],
        y=wvs_counts.sort_index().values,
        marker_color="#F28E2B", 
        name="WVS"
    ))
    fig_wvs.update_layout(
        xaxis_title="Civilian Responses",##wvs_meta["question"]
        yaxis_title="Respondent Count",
        template="plotly_white",
    )
    st.plotly_chart(fig_wvs, use_container_width=False)
