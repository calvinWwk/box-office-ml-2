# 🎬 Movie Revenue Prediction

This project predicts **movie revenue** using metadata from the [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).  
We explored **Linear Regression (baseline)** and **Random Forest (ensemble)** to evaluate performance and deployed the best-performing model with **Streamlit**.  

---

## 📂 Project Structure
```
├── artifacts/
│   ├── dataset_preprocessed_topk.csv   # Slim dataset with top features + revenue
│   ├── feature_list.json               # Selected features metadata
│   ├── linreg_pipeline.joblib          # Baseline model
│   ├── rf_pipeline.joblib              # Random Forest model
├── Movie_Revenue_Prediction_Colab.ipynb # Main Colab notebook
├── streamlit_app.py                     # Streamlit app for deployment
├── README.md                            # Project overview (this file)
```

---

## 📊 Dataset
- **Source:** [TMDB 5000 Movie Dataset on Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)  
- **Files used:** `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`  
- **Target variable:** `revenue`  

---

## ⚙️ Preprocessing & Feature Engineering
- Dropped irrelevant text-heavy columns.  
- Extracted counts from JSON-like columns (genres, cast, crew, production companies, etc.).  
- Extracted release year.  
- Handled missing values (median imputation) and removed invalid rows.  
- Selected **Top 12 correlated features** with revenue (e.g., `vote_count`, `budget`, `popularity`).  

---

## 🤖 Models & Experiments

### Baseline: Linear Regression (Adam)
- RMSE: ~126.7M  
- MAE: ~62.5M  
- R²: ~0.687  

### Random Forest (Teammate)
- RMSE: ~119.0M  
- MAE: ~57.2M  
- R²: ~0.724  

👉 **Random Forest outperformed the baseline**, capturing nonlinear interactions.  

---

## 🧪 Error Analysis
- Both models underestimated extreme blockbuster revenues.  
- Linear Regression biased toward average values.  
- Random Forest improved fit but still struggled with outliers.  
- Future improvements: **log-transform target**, test **boosting models (XGBoost/LightGBM)**.  

---

## 🚀 Deployment
We deployed a **Streamlit app** for interactive predictions:  
- Users input metadata features (budget, vote counts, etc.).  
- The trained Random Forest model predicts movie revenue.  

Run locally with:  
```bash
streamlit run streamlit_app.py
```

---

## 👥 Team Contributions
- **Adam:** Built baseline Linear Regression model.  
- **[Your Name]:** Developed Random Forest experiments and tuning.  
- **Both:** Prepared artifacts and deployed with Streamlit.  

---

## 📌 Next Steps
- Try log-transformed revenue.  
- Explore gradient boosting and ensemble methods.  
- Add feature importance visualization for explainability.  

---

✨ *This repo is part of our ITI113 Final Project submission.*  
