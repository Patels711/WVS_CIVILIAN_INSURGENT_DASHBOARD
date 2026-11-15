<<<<<<< HEAD
# WVS Civilian–Insurgent Gender Attitudes Dashboard

A Streamlit research dashboard summarizing gender and social attitudes among 153 former combatants of the Revolutionary Armed Forces of Colombia (FARC), interviewed in Colombia in October 2021, and presenting selected descriptive comparisons with civilian responses from the World Values Survey (WVS).

The broader research described in the app examines gender attitudes among Global South insurgents in Colombia and Kurdistan, and asks whether participation in armed struggle can change attitudes toward gender roles and whether those changes endure after demobilization. This repository contains the Colombian FARC dashboard and its bundled survey files.

## What the dashboard does

- **Introduction — `Home.py`:** explains the project, fieldwork, and survey context.
- **FARC survey summaries — `pages/01_Raw Data.py`:** reads `cleaned_data.csv` and displays response counts, percentages, and charts for the former-combatant survey.
- **WVS comparisons — `pages/02_Chart Comparisons.py`:** maps selected FARC questions to WVS items, displays corresponding civilian response distributions, and offers side-by-side charts. It uses WVS Wave 7 Colombia for the selected Wave 7 comparisons and a Wave 6 Colombia file for the Q48 comparison.

The mapped topics include mothers working for pay (Q28), men as political or business leaders (Q29, Q31), education for boys versus girls (Q30), housework and paid work (Q32), jobs when employment is scarce (Q33), a wife earning more than her husband (Q35), women’s economic independence (Q48), and social-norm questions such as homosexuality, prostitution, abortion, divorce, premarital sex, and wife beating (Q182–Q189, as mapped in the page).

The charts are descriptive. The FARC survey and civilian WVS samples have different populations, sampling frames, instruments, and collection periods; the charts do not establish causation or statistical equivalence.

## Data files: names, populations, and use

| Repository file | Dataset represented | How the dashboard uses it |
| --- | --- | --- |
| `cleaned_data.csv` | Project survey of 153 former FARC combatants; fieldwork in Colombia, October 2021. | Main dataset for the Introduction’s context and the Raw Data page; also the insurgent-response side of Chart Comparisons. |
| `WVS_Wave_7_Colombia_Csv_v5.1.csv` | World Values Survey Wave 7, Colombia country file (the repository filename identifies release v5.1). | Civilian comparison data loaded by Chart Comparisons. The page also explicitly reads this file for the custom Q33 and Q35 mappings. |
| `WV6_Data_Colombia_Csv_v20221117.csv` | World Values Survey Wave 6, Colombia country file; filename dates this copy 2022-11-17. | Explicitly used for the custom Q48 comparison (WVS Wave 6 item V48). |
| `WVS_Wave_7_Turkey_Csv_v5.1.csv` | World Values Survey Wave 7, Turkey country file (release v5.1 in the filename). | Bundled in the repository, but not loaded by the current dashboard pages. |
| `data.csv`, `data_Age_Entered.csv`, `datawocolumns.csv` | Additional project CSVs. | Alternate/intermediate files; the current pages do not read them. |

`AGE_ENTERED.txt` and `lookup.txt` are supporting mapping or cleaning materials. `sortCSV.py` is a data-preparation utility. The app’s active input paths are visible in `Home.py`, `pages/01_Raw Data.py`, and `pages/02_Chart Comparisons.py`.

## Technology

- Python 3
- Streamlit for the multipage dashboard
- pandas and NumPy for tabular processing
- Plotly for interactive charts; Matplotlib and Seaborn are also listed dependencies
- CSV files bundled with the repository

## Run locally

Use Python 3.9 or newer and the packages in `requirements.txt`. From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate       # Windows PowerShell: .venv\\Scripts\\Activate.ps1
=======
# FARC Gender Attitudes Dashboard

An interactive Streamlit dashboard for exploring gender and social attitude responses from former FARC combatants in Colombia and comparing selected answers with civilian survey responses from the World Values Survey (WVS). The project is part of a broader research effort on gender norms, armed struggle, and post-conflict life among insurgents in the Global South.

The original field survey was conducted in Colombia in 2021 and includes 153 former combatants. Its questions draw largely on WVS questions about gender roles, work, education, political and business leadership, and social norms. The dashboard reports descriptive counts and percentages; it does not estimate causal effects or establish that the two survey populations are directly comparable.

## What the app does

- **Home page:** introduces the research and links to the analysis pages.
- **Raw Data:** shows response counts and percentages for a selected FARC survey question and a respondent distribution grouped by race, combatant age, gender, or age at enlistment.
- **Chart Comparisons:** displays response distributions for the FARC survey and the Colombian WVS civilian sample. Turn on the sidebar comparison option to view percentages side by side. The app uses selected WVS Wave 7 variables, plus specified variables from the Colombia Wave 7 and Wave 6 files for questions whose coding or source differs.

Percentages are calculated within each dataset's non-missing responses for the selected question. Sample sizes, survey design, fieldwork context, and question coding may differ, so comparisons should be interpreted descriptively and with care.

## Repository contents

| Path | Purpose |
| --- | --- |
| `Home.py` | Streamlit landing page and project description. |
| `pages/01_Raw Data.py` | FARC survey response tables and respondent-group charts. |
| `pages/02_Chart Comparisons.py` | FARC and Colombian WVS response charts. |
| `cleaned_data.csv` | Analysis-ready FARC survey dataset consumed by both dashboard pages. |
| `WVS_Wave_7_Colombia_Csv_v5.1.csv` | Colombian WVS Wave 7 data used for civilian comparisons. |
| `WV6_Data_Colombia_Csv_v20221117.csv` | Colombia Wave 6 source used for the Q48 comparison. |
| `WVS_Wave_7_Turkey_Csv_v5.1.csv` | WVS Turkey data included in the repository; it is not currently loaded by the dashboard. |
| `data.csv`, `datawocolumns.csv`, `data_Age_Entered.csv` | Additional/intermediate project data files; the running app reads `cleaned_data.csv`. |
| `sortCSV.py` | One-off CSV formatting helper for the Colombia Wave 7 file (converts semicolon-delimited input to comma-delimited output). It overwrites its input file; keep a backup before using it. |
| `images/` | Photos displayed on the Home page. |
| `AGE_ENTERED.txt`, `lookup.txt`, `race_quotes_report.txt` | Auxiliary data/cleanup notes retained with the project. |
| `requirements.txt` | Python package dependencies. |

## Set up and run locally

Use Python 3.10 or newer. From the repository root:

```bash
python -m venv .venv
```

Activate the environment:

```bash
# macOS / Linux
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Install dependencies and launch the multipage app:

```bash
>>>>>>> 8eaf0ad (changes to buttons)
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run Home.py
```

<<<<<<< HEAD
Open the local URL printed by Streamlit. Run the command from the repository root because the pages load CSV and image files by relative paths.

## Project structure

```text
Home.py                                      Introduction and app entry point
pages/01_Raw Data.py                         FARC survey summaries and charts
pages/02_Chart Comparisons.py                FARC–WVS question mappings and comparisons
cleaned_data.csv                             Active former-FARC survey input
WVS_Wave_7_Colombia_Csv_v5.1.csv             Active WVS Wave 7 Colombia comparison input
WV6_Data_Colombia_Csv_v20221117.csv          Active WVS Wave 6 Colombia Q48 input
WVS_Wave_7_Turkey_Csv_v5.1.csv               Included, not currently loaded
images/                                      Fieldwork and project images
requirements.txt                             Python dependencies
sortCSV.py                                   Data-preparation utility
AGE_ENTERED.txt, lookup.txt                  Supporting mapping/cleaning material
```

## Sources and citation

The WVS files are derived from public WVS releases. Cite the source release that corresponds to each file when redistributing or publishing analyses. The official Wave 7 cross-national dataset citation is:

> Haerpfer, C., Inglehart, R., Moreno, A., Welzel, C., Kizilova, K., Diez-Medrano, J., Lagos, M., Norris, P., Ponarin, E., & Puranen, B. (2022). *World Values Survey Wave 7 (2017–2022) Cross-National Data-Set*, Version 4.0.0. World Values Survey Association. https://doi.org/10.14281/18241.18

The repository introduction describes the FARC survey sample and fieldwork, but does not provide a full bibliographic citation or a separate data-use/redistribution statement for that dataset. The original study citation and reuse terms should be confirmed with the research team before reuse or redistribution. Image captions in `Home.py` describe the fieldwork photographs and state that pictured interviewees consented to their use.

- [World Values Survey data and documentation](https://www.worldvaluessurvey.org/WVSContents.jsp?CMSID=Documentation)
- [World Values Survey Wave 7 documentation](https://www.worldvaluessurvey.org/WVSDocumentationWV7.jsp)
- [Streamlit documentation](https://docs.streamlit.io/)
- [Plotly Python documentation](https://plotly.com/python/)
=======
Streamlit prints a local URL (typically `http://localhost:8501`). Open it in a browser. Use the left sidebar to switch pages and select questions and chart options. Stop the server with `Ctrl+C` in the terminal.

## Replicate the repository

To get the same project files, clone the repository URL supplied by its owner and enter the project directory:

```bash
git clone <repository-url>
cd <repository-directory>
```

Then follow **Set up and run locally** above. The app expects the CSV files and `images/` directory to remain at the repository root / listed locations; it uses relative paths. Keep the original input datasets alongside the code. If a dataset is not distributed with a future copy of this repository, obtain it from its original provider under that provider's access and reuse terms, then place it at the filename shown in the table.

The dependency list is in `requirements.txt`. For a more repeatable environment, record the Python version and package versions used for your analysis (for example, by exporting a pinned requirements file after confirming the app works). No separate build step, database, API key, or environment variable is required by the current app.

## Data notes and acknowledgments

The dashboard's research dataset comes from fieldwork with former FARC combatants in Colombia. We thank the people who participated in the survey and the researchers and field collaborators who made the work possible. The photos shown in the app are described in their captions; the captions state that images were used with interviewees' informed consent.

The civilian comparison files are World Values Survey data, including Colombia Wave 7 and a Colombia Wave 6 file. Please retain the source documentation and follow the WVS provider's citation, access, and redistribution requirements when using or sharing those data. The repository currently contains the data files but does not include enough source documentation to identify the precise dataset citation, authorship, license, or download record. Add the formal WVS citation and any project/funder acknowledgments here when those details are available; do not infer them from filenames alone.

The analysis is descriptive. In particular, the dashboard does not adjust for sampling differences or other respondent characteristics, and question wording, survey wave, response coding, and missing-data handling should be checked before drawing substantive comparisons.

## Current implementation notes

- Both analysis pages load `cleaned_data.csv`; the comparison page also loads the Colombia WVS files described above.
- Question definitions and response labels are maintained in mappings in the page scripts.
- The Turkey WVS CSV and intermediate data files are present but are not read by the current dashboard pages.
- CSVs may contain sensitive or restricted research data. Confirm consent, ethics, provider terms, and institutional requirements before publishing or redistributing the repository or its data.
>>>>>>> 8eaf0ad (changes to buttons)
