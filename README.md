# WVS Civilian Insurgent Dashboard

A Streamlit research dashboard about gender attitudes among former combatants of the Revolutionary Armed Forces of Colombia (FARC), with selected comparisons to civilian World Values Survey (WVS) responses.

The app describes its original survey as 153 former combatants interviewed during fieldwork in Colombia in October 2021. It presents response summaries for questions about gender roles and equality, and provides selected comparisons with WVS civilian data. The comparison is descriptive: the datasets represent different populations, instruments, sampling frames, and fieldwork periods.

## Dashboard pages

- **Introduction (`Home.py`)** — research background and the project’s fieldwork context.
- **Raw Data (`pages/01_Raw Data.py`)** — question-level response counts, percentages, and charts for the FARC survey.
- **Chart Comparisons (`pages/02_Chart Comparisons.py`)** — selected former-combatant responses alongside WVS civilian responses.

Use the Streamlit sidebar to move between pages and choose the survey question and chart options.

## Technology

- Python 3.
- Streamlit for the dashboard.
- pandas and NumPy for tabular processing.
- Plotly for interactive charts; Matplotlib and Seaborn are also listed dependencies.
- CSV files bundled in the repository for the FARC and WVS inputs.

## Requirements

- Python 3.9 or newer is recommended for a current Streamlit environment.
- Packages listed in `requirements.txt`.

## Run locally

From the repository root, create and activate a virtual environment, install the project packages, and start Streamlit:

```bash
python3 -m venv .venv
source .venv/bin/activate       # Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run Home.py
```

Open the local URL printed by Streamlit. Keep the working directory at the repository root because the pages load CSV and image files using relative paths.

## Project layout and data files

```text
Home.py                                      Introduction and dashboard entry point
pages/01_Raw Data.py                         FARC survey summaries and charts
pages/02_Chart Comparisons.py                Question mapping and WVS comparisons
cleaned_data.csv                             FARC survey data used by the dashboard
WVS_Wave_7_Colombia_Csv_v5.1.csv             WVS Wave 7 Colombia comparison data
WV6_Data_Colombia_Csv_v20221117.csv          WVS Wave 6 Colombia data used for selected items
WVS_Wave_7_Turkey_Csv_v5.1.csv               Included WVS file; not currently loaded by the pages
images/                                      Fieldwork and project images
requirements.txt                             Python package list
sortCSV.py                                   Data-preparation utility
AGE_ENTERED.txt, lookup.txt                  Supporting mapping and cleaning material
```

`data.csv`, `data_Age_Entered.csv`, and `datawocolumns.csv` are additional intermediate or alternate data files in the repository; the dashboard pages currently read `cleaned_data.csv` and the Colombia WVS files listed above.

## Data sources and citation

The WVS files in this repository are derived from public WVS releases. The official WVS Wave 7 cross-national dataset citation is:

> Haerpfer, C., Inglehart, R., Moreno, A., Welzel, C., Kizilova, K., Diez-Medrano, J., Lagos, M., Norris, P., Ponarin, E., & Puranen, B. (2022). *World Values Survey Wave 7 (2017–2022) Cross-National Data-Set*, Version 4.0.0. World Values Survey Association. https://doi.org/10.14281/18241.18

See the [official WVS data and documentation portal](https://www.worldvaluessurvey.org/WVSContents.jsp?CMSID=Documentation) for wave documentation, questionnaires, data terms, and citation requirements. A Wave 6 Colombia data file is also included in this repository and should be attributed to its WVS release if used.

The repository’s introduction identifies the 2021 FARC survey and its sample, but the repository does not provide a full bibliographic citation or separate redistribution statement for that survey dataset. Add the original study’s citation and confirm the dataset’s reuse terms before reusing or redistributing it. Captions in `Home.py` identify the fieldwork photographs and state that the pictured interviewees consented to their use.

## Interpretation

These charts summarize the included files; they do not establish causal effects or make the FARC sample statistically equivalent to the civilian WVS samples. WVS item wording, response scales, waves, and country files vary. Read each chart label and question mapping in `pages/02_Chart Comparisons.py` before interpreting a comparison.

## Sources

- [World Values Survey data and documentation](https://www.worldvaluessurvey.org/WVSContents.jsp?CMSID=Documentation)
- [World Values Survey Wave 7 documentation](https://www.worldvaluessurvey.org/WVSDocumentationWV7.jsp)
- [Streamlit documentation](https://docs.streamlit.io/)
- [Plotly Python documentation](https://plotly.com/python/)
