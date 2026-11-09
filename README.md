# WVS Civilian Insurgent Dashboard

An interactive Streamlit research dashboard exploring gender attitudes among former combatants of the Revolutionary Armed Forces of Colombia (FARC), with selected comparisons to civilian responses in the World Values Survey (WVS).

The original FARC survey includes 153 former combatants interviewed during fieldwork in Colombia in October 2021. Based largely on WVS Wave 7 questions, it covers attitudes toward gender roles and equality alongside demographic characteristics. The dashboard presents response summaries and lets readers compare selected questions with civilian survey data from Colombia and Turkey.

## Dashboard pages

- **Introduction:** Research background and fieldwork context.
- **Raw Data:** Response counts and percentages for the FARC survey.
- **Chart Comparisons:** Side-by-side views comparing former combatant responses with selected WVS civilian data.

Use the Streamlit sidebar to navigate between the raw-data and comparison pages.

## Built with

Python, Streamlit, pandas, NumPy, Matplotlib, Seaborn, Plotly, and scikit-learn.

## Run locally

Use Python 3, create and activate a virtual environment, then install dependencies and start the dashboard:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
streamlit run Home.py
```

The dashboard reads CSV datasets and supporting images from the repository. Keep those files in place when running it locally.

## Data context

The project is intended for research exploration and communication. The survey data are observational and reflect a specific population, place, and fieldwork period; visual comparisons should be interpreted in that context.
