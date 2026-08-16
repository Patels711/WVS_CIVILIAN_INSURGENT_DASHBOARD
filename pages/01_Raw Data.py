import pandas as pd
import streamlit as st
import re
import plotly.express as px

survey = pd.read_csv('cleaned_data.csv')
# st.bar_chart(survey, x="age", y=["age_entered", "years_active_guerilla"])
st.set_page_config(page_title="Raw Data", page_icon="📈")
# st.title("Data Analysis for FINAL CLEANUP")

report = []

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
        "survey": "question 2 (wvs #33)"
    },
    "Q35": {
        "question": "If a woman earns more money than her husband, it's almost certain to cause problems",
        "scale": "3 Neither, 1 Agree, 2 Disagree",
        "survey": "question 3 (wvs #35)"
    },
    "Q48": {
        "question": "Having a job is the best way for a woman to be an independent person.",
        "scale": "1 Agree, 2 Disagree, 3 Neither",
        "survey": "question 5 (wvs-6 #48)"
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


st.title("Guerrilla FARC Survey")

options = [
    f"{key} : {value['question']}"
    for key, value in WVS_COLUMN_TO_QUESTION.items()
]

st.sidebar.title("Table Controls")
st.sidebar.markdown("Select the question to see the table.")

options = sorted(
    [f"{k} : {meta['question']}" for k, meta in WVS_COLUMN_TO_QUESTION.items()]
)

selected = st.sidebar.selectbox(
    "Question",
    options,
)

group_options = [
    "Race",
    "Combatant Age",
    "Gender",
    "Enlistment Age",
]

selected_group = st.sidebar.selectbox(
    "Guerrilla FARC Survey by:",
    group_options,
)

selected_wvs_col = selected.split(" :")[0]
meta = WVS_COLUMN_TO_QUESTION[selected_wvs_col]

survey_col = meta["survey"]


response_label_map = {}

for part in meta["scale"].split(","):
    part = part.strip()
    match = re.match(r"^(\d+)\s+(.*)$", part)
    if match:
        response_label_map[int(match.group(1))] = match.group(2)


survey_counts = (
    survey[survey_col]
    .value_counts(dropna=True)
    .sort_index()
)

max_survey_response = survey_counts.idxmax()
max_survey_count = int(survey_counts.max())
max_survey_label = response_label_map.get(int(max_survey_response), str(max_survey_response))

table_df = pd.DataFrame({
    "Response Code": survey_counts.index,
    "Response": [
        response_label_map.get(int(code), str(code))
        for code in survey_counts.index
    ],
    "Count": survey_counts.values
})

table_df["Percent"] = (
    table_df["Count"]
    / table_df["Count"].sum()
    * 100
).round(2)


st.subheader(meta["question"])

col1, col2 = st.columns(2)

with col1:
    st.metric("# Responsed from Total (153)", int(table_df["Count"].sum()))

with col2:
    max_row = table_df.loc[table_df["Count"].idxmax()]
    st.metric(
        "Most Common Response",
        max_survey_label,
        f"{max_row['Count']} responses",
    )


st.dataframe(
    table_df,
    use_container_width=True,
    hide_index=True
)


def make_grouped_data(dataframe, group_name, response_column):
    grouped_df = dataframe[dataframe[response_column].notna()].copy()

    if group_name == "Race":
        grouped_df["Group"] = grouped_df["race"].fillna("Missing")
    elif group_name == "Gender":
        grouped_df["Group"] = grouped_df["gender"].fillna("Missing")
    elif group_name == "Combatant Age":
        grouped_df["Group"] = pd.cut(
            grouped_df["age"],
            bins=[19, 29, 39, 49, 59, 100],
            labels=["20-29", "30-39", "40-49", "50-59", "60+"],
        )
        grouped_df["Group"] = grouped_df["Group"].cat.add_categories("Missing").fillna("Missing")
    else:
        enlistment_age = grouped_df["age_entered"]
        q1 = enlistment_age.quantile(0.25)
        q3 = enlistment_age.quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        grouped_df = grouped_df[
            enlistment_age.isna() | enlistment_age.between(lower_bound, upper_bound)
        ].copy()
        grouped_df["Group"] = pd.cut(
            grouped_df["age_entered"],
            bins=[0, 12, 17, 24, 34],
            labels=["12 or younger", "13-17", "18-24", "25-34"],
        )
        grouped_df["Group"] = grouped_df["Group"].cat.add_categories("Missing").fillna("Missing")

    grouped_counts = (
        grouped_df["Group"]
        .value_counts(dropna=False)
        .rename_axis("Group")
        .reset_index(name="Count")
    )
    grouped_counts["Group"] = grouped_counts["Group"].astype(str).replace("nan", "Missing")
    return grouped_counts


grouped_counts = make_grouped_data(survey, selected_group, survey_col)

st.subheader(f"Guerrilla FARC Survey by: {selected_group}")

pie_chart = px.pie(
    grouped_counts,
    names="Group",
    values="Count",
    color="Group",
    title=f"{selected_group} Breakdown",
)
pie_chart.update_traces(
    textinfo="percent+label",
    hovertemplate="%{label}<br>Responses: %{value}<br>Percent: %{percent}<extra></extra>",
)
st.plotly_chart(pie_chart, use_container_width=True)