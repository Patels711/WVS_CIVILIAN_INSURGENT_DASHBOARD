import pandas as pd
import streamlit as st


survey = pd.read_csv('cleaned_data.csv')
#st.bar_chart(survey, x="AGE", y=["AGE_ENTERED", "YEARS_ACTIVE_GUERILLA"])
st.set_page_config(page_title="Cleanup Stats", page_icon="🧹")
st.title("Data Analysis for FINAL CLEANUP")

report = []

for col in survey.columns:
    null_count = survey[col].isnull().sum()
    non_num_count=pd.to_numeric(survey[col], errors="coerce").isnull().sum()
    actual_non_num = max(0, non_num_count-null_count)

    if survey[col].dtype == "object":
        space_issues = (
            survey[col].astype(str).str.startswith(" ").sum() + survey[col].astype(str).str.endswith(" ").sum()
        )
    else:
        space_issues = 0

    report.append(
        {
            "Column Name": col,
            "Data Type": str(survey[col].dtype),
            "Null/Missing Count": null_count,
            "Non-Numeric Hidden in Column": actual_non_num,
            "Trailing Space Values": space_issues,
        }
    )

report_df = pd.DataFrame(report)
st.dataframe(report_df)

if st.button("Go to Dashboard 🚀"):
    st.switch_page("pages/chart_page.py")