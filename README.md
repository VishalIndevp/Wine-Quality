# 🍷 Wine Quality Prediction (Machine Learning + Streamlit)

## 📌 Project Overview

This project predicts the **quality score of wine** using machine learning based on its **chemical properties**.
The model analyzes features such as acidity, sugar level, alcohol, sulphates, and sulfur dioxide to estimate the wine quality.

The final model is deployed with a **Streamlit web application**, allowing users to enter wine characteristics and get an instant prediction.

---

## 🎯 Problem Statement

Wine quality is usually determined through **sensory evaluation by experts**, which can be expensive and time-consuming.

This project uses **machine learning** to predict wine quality automatically from measurable chemical attributes.

---

## 📊 Dataset Features

| Feature              | Description                                      |
| -------------------- | ------------------------------------------------ |
| type                 | Type of wine (Red / White)                       |
| fixed acidity        | Non-volatile acids that contribute to wine taste |
| volatile acidity     | Acetic acid content (vinegar taste indicator)    |
| citric acid          | Adds freshness and flavor                        |
| residual sugar       | Sugar remaining after fermentation               |
| chlorides            | Salt content in wine                             |
| free sulfur dioxide  | Free SO₂ preventing microbial growth             |
| total sulfur dioxide | Total amount of SO₂ in wine                      |
| density              | Density of the wine                              |
| pH                   | Acidity strength                                 |
| sulphates            | Preservative compound                            |
| alcohol              | Alcohol percentage                               |
| quality              | Wine quality score (Target Variable)             |

---

## ⚙️ Data Preprocessing

The following preprocessing steps were applied:

* Missing value handling
* Outlier detection and treatment
* Encoding categorical feature (`type`)
* Train–test split

Since tree-based models were used, **feature scaling was not required**.

---

## 🤖 Machine Learning Models Tested

Several models were trained and evaluated:

* Linear Regression
* Decision Tree
* Random Forest
* Gradient Boosting
* XGBoost
* Logistic Regression
* SVM
* K-Nearest Neighbors
* Naive Bayes

### 🏆 Best Model

**Gradient Boosting Regressor** achieved the best performance and was selected for deployment.

Evaluation metrics used:

* **R² Score**
* **RMSE (Root Mean Squared Error)**

---

## 🚀 Streamlit Web Application

A **Streamlit UI** was built where users can:

1. Select wine type (Red / White)
2. Enter chemical properties
3. Click **Predict Quality**
4. Get the predicted wine quality score instantly

---

## 🖥️ Project Structure

```
wine-quality-project
│
├── app.py                # Streamlit web application
├── model_GB.pkl          # Trained Gradient Boosting model
├── model_columns.pkl     # Feature column order
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## 📦 Installation

Clone the repository:

```
git clone https://github.com/your-username/wine-quality-prediction.git
cd wine-quality-prediction
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the Streamlit application:

```
streamlit run app.py
```

---

## 📈 Example Prediction

After entering wine attributes such as acidity, alcohol, and sugar level, the model predicts a **quality score between 3 and 9**.

The app also classifies the result as:

* 🔴 Low Quality Wine
* 🟡 Average Quality Wine
* 🟢 Good Quality Wine

---

## 🧠 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* XGBoost
* Joblib
* Streamlit

---

## 👨‍💻 Author

**Vishal Singh**
Data Analytics & Machine Learning Enthusiast

LinkedIn: https://www.linkedin.com/in/vishal-singh-here/
GitHub: https://github.com/VishalIndevp

---

## ⭐ Future Improvements

* Add feature importance visualization
* Deploy the app on **Streamlit Cloud**
* Implement hyperparameter tuning
* Improve UI with interactive charts

---

## 📜 License

This project is open-source and available under the MIT License.
