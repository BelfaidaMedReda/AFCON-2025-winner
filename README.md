# Predicting the Winners of the 2025 Africa Cup of Nations (CAN) in Morocco 🏆

This project aims to predict the winning probabilities of teams participating in the 2025 Africa Cup of Nations (CAN), hosted in Morocco. By leveraging a well-constructed database, rigorous feature selection, and a powerful machine learning model, **XGBoost**, we provide accurate probabilities for each team.

---

## 🌟 Project Objectives

1. **Create a reliable database:**
   - Collect and structure historical data on team performances.
   - Integrate data on players, past matches, and other key factors.

2. **Select relevant features:**
   - Analyze the most influential variables (FIFA rankings, recent performances, squad composition, etc.).

3. **Predict winning probabilities:**
   - Train an **XGBoost** model.
   - Evaluate and optimize the model’s performance.
   - Calculate probabilities for each team to win the trophy.

---

## 🔧 Technologies Used

- **Languages:** Python

- **Libraries:**
  - `pandas`: Data manipulation.
  - `scikit-learn`: Preprocessing and evaluation metrics.
  - `xgboost`: Main machine learning model.

- **Tools:**
  - Jupyter Notebook for development and analysis.
  - GitHub for version control.

---

## 🗂 Project Structure

```bash
├── Data_Preprocessing.ipynb  
├── dataset  # Supporting datasets
│   ├── champion.csv
│   ├── data.csv
│   ├── fifa_ranking.csv
│   ├── scraping.py
│   ├── stats.csv
│   └── test.csv
├── Prediction.ipynb
├── README.md
└── requirements.txt
```

---

## 📊 Predictions

Here is a preview of the winning probabilities for the favorite teams:

| Team            | Winning Probability (%) |
|-----------------|--------------------------|
| Ivory Coast     | 11.06%                   |
| Senegal         | 9.71%                    |
| Nigeria         | 9.41%                    |
| Algeria         | 8.58%                    |
| Morocco         | 6.68%                    |

