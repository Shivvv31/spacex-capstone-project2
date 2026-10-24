# SpaceX Falcon 9 First-Stage Landing Prediction

IBM Applied Data Science Capstone project. The workflow collects historical launch data, prepares a landing-success target, explores patterns with Python and SQL, visualizes launch geography with Folium, builds a Plotly Dash dashboard, and evaluates classification models.

**Repository URL used in the presentation:** https://github.com/Shivvv31/spacex-falcon9-landing-prediction

## Files
- `01_jupyter-labs-spacex-data-collection-api.ipynb` — API collection
- `02_jupyter-labs-webscraping.ipynb` — Wikipedia launch-table scraping
- `03_labs-jupyter-spacex-Data_wrangling.ipynb` — cleaning and binary landing class
- `04_jupyter-labs-eda-sql-coursera_sqllite.ipynb` — SQL EDA
- `05_edadataviz.ipynb` — exploratory analysis and visualizations
- `06_lab_jupyter_launch_site_location.ipynb` — Folium map
- `07_SpaceX_Machine_Learning_Prediction_Part_5.ipynb` — classification models
- `spacex_dash_app.py` — Plotly Dash dashboard
- `Spacex.csv`, `spacex_launch_dash.csv` — supplied project data files
- `proximity_measurement.py` — haversine calculator for map-selected coordinates
- `requirements.txt` — dependencies

## Key findings described in the presentation
- Landing success tends to improve with flight experience in the historical dataset.
- The site analysis reports 10 successful landings from 13 KSC LC-39A launches (76.9%).
- Orbit, launch site, and booster generation show useful associations with landing outcomes. Payload mass alone is not sufficient to explain the result.
- The course report gives 83.33% first-run Decision Tree test accuracy on 18 held-out observations (15/18 correct). The confusion matrix in the updated presentation is aligned to that 18-observation test set: TN=7, FP=1, FN=2, TP=8.

## Important evaluation note
Model metrics must be regenerated from the exact executed notebook and same train/test split before being treated as definitive. The course exercise uses a small test set, so accuracy can vary materially with a few predictions. Compare accuracy, precision, recall, F1 and confusion matrices; use cross-validation for model selection. The SQL exercise may use a different course data snapshot from the 90-record modeling dataset, so row counts should not be assumed identical across notebooks.

## SQL coverage
The SQL notebook demonstrates `DISTINCT`, `LIKE`, `WHERE`, `BETWEEN`, `SUM`, `AVG`, `MIN`, `GROUP BY`, `ORDER BY`, date extraction with `substr()` and a nested `MAX()` query. Reported examples include NASA (CRS) total payload of 45,596 kg, average F9 v1.1 payload of approximately 2,534.7 kg, and first successful ground-pad landing on 2015-12-22. Check the notebook output when reproducing results because data snapshots can differ.

## Folium proximity analysis
Current presentation values are approximate straight-line distances from manually selected map points near CCAFS LC-40: shoreline ~3 km, railway corridor ~1 km, highway corridor ~2 km, and Titusville centre ~23 km. These are not surveyed measurements or driving distances. To produce reproducible measurements, record the exact latitude/longitude for the launch site and each feature, then run `python proximity_measurement.py` and enter those coordinates.

## Run locally
1. Use Python 3.10 or newer.
2. Install dependencies: `pip install -r requirements.txt`.
3. Open notebooks in Jupyter or VS Code and run cells in order.
4. Start dashboard: `python spacex_dash_app.py`; open `http://127.0.0.1:8050`.

## Before submission
- Verify the GitHub URL opens and the repository is public if required.
- Ensure all notebooks and Python files are committed.
- Export the final PowerPoint to PDF and upload the PDF separately if the course requests it.
- Rerun model evaluation and replace reported values if the executed notebook differs.

## Submission links (verified against files in this project)

Repository: https://github.com/Shivvv31/spacex-falcon9-landing-prediction

- [01 — SpaceX API data collection](https://github.com/Shivvv31/spacex-falcon9-landing-prediction/blob/main/01_jupyter-labs-spacex-data-collection-api.ipynb)
- [02 — Wikipedia web scraping](https://github.com/Shivvv31/spacex-falcon9-landing-prediction/blob/main/02_jupyter-labs-webscraping.ipynb)
- [03 — Data wrangling](https://github.com/Shivvv31/spacex-falcon9-landing-prediction/blob/main/03_labs-jupyter-spacex-Data_wrangling.ipynb)
- [04 — EDA with SQL](https://github.com/Shivvv31/spacex-falcon9-landing-prediction/blob/main/04_jupyter-labs-eda-sql-coursera_sqllite.ipynb)
- [05 — EDA and data visualization](https://github.com/Shivvv31/spacex-falcon9-landing-prediction/blob/main/05_edadataviz.ipynb)
- [06 — Folium launch-site map](https://github.com/Shivvv31/spacex-falcon9-landing-prediction/blob/main/06_lab_jupyter_launch_site_location.ipynb)
- [07 — Classification modelling](https://github.com/Shivvv31/spacex-falcon9-landing-prediction/blob/main/07_SpaceX_Machine_Learning_Prediction_Part_5.ipynb)
- [Plotly Dash app](https://github.com/Shivvv31/spacex-falcon9-landing-prediction/blob/main/spacex_dash_app.py)
- [Proximity measurement utility](https://github.com/Shivvv31/spacex-falcon9-landing-prediction/blob/main/proximity_measurement.py)

## Model-evaluation evidence note

The presentation reports the course first-run test accuracy as 83.33% (15/18) for the four classifiers. The exported notebook in this ZIP does not contain saved cell outputs, so per-model precision, recall, F1, and cross-validation scores must be regenerated by running notebook 07. Do not treat missing metrics as measured values.
