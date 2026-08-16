import pandas as pd
import streamlit as st
import re

survey = pd.read_csv('cleaned_data.csv')
# st.bar_chart(survey, x="age", y=["age_entered", "years_active_guerilla"])
st.set_page_config(page_title="Cleanup Stats", page_icon="🧹")
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
        "scale": "1 1, 2 2, 3 3, 4 4, 5 5, 6 6, 7 7, 8 8, 9 9, 10 10",
        "survey": "homosexuality"
    },
    "Q183": {
        "question": "Prostitution",
        "scale": "1 1, 2 2, 3 3, 4 4, 5 5, 6 6, 7 7, 8 8, 9 9, 10 10",
        "survey": "prostitution"
    },
    "Q184": {
        "question": "Abortion",
        "scale": "1 1, 2 2, 3 3, 4 4, 5 5, 6 6, 7 7, 8 8, 9 9, 10 10",
        "survey": "abortion"
    },
    "Q185": {
        "question": "Divorce",
        "scale": "1 1, 2 2, 3 3, 4 4, 5 5, 6 6, 7 7, 8 8, 9 9, 10 10",
        "survey": "divorce"
    },
    "Q186": {
        "question": "Sex before marriage",
        "scale": "1 1, 2 2, 3 3, 4 4, 5 5, 6 6, 7 7, 8 8, 9 9, 10 10",
        "survey": "premarital_sex"
    },
    "Q189": {
        "question": "For a man to beat his wife",
        "scale": "1 1, 2 2, 3 3, 4 4, 5 5, 6 6, 7 7, 8 8, 9 9, 10 10",
        "survey": "husband_hitting_wife"
    },
}

st.title("Guerrilla Survey Tables")

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
    st.metric("Total Responses", int(table_df["Count"].sum()))

with col2:
    max_row = table_df.loc[table_df["Count"].idxmax()]
    st.metric(
        "Most Common Response",
        max_row["Response"],
        f"{max_row['Count']} responses",
    )


st.dataframe(
    table_df,
    use_container_width=True,
    hide_index=True
)

# for col in survey.columns:
#     null_count = survey[col].isnull().sum()
#     non_num_count=pd.to_numeric(survey[col], errors="coerce").isnull().sum()
#     actual_non_num = max(0, non_num_count-null_count)

#     if survey[col].dtype == "object":
#         space_issues = (
#             survey[col].astype(str).str.startswith(" ").sum() + survey[col].astype(str).str.endswith(" ").sum()
#         )
#     else:
#         space_issues = 0

#     report.append(
#         {
#             "Column Name": col,
#             "Data Type": str(survey[col].dtype),
#             "Null/Missing Count": null_count,
#             "Non-Numeric Hidden in Column": actual_non_num,
#             "Trailing Space Values": space_issues,
#         }
#     )

# report_df = pd.DataFrame(report)
# st.dataframe(report_df)

if st.button("Go to Dashboard 🚀"):
    st.switch_page("pages/chart_page.py")