# 🍷 Wine Quality Predictor

A **Streamlit web application** that predicts wine quality scores using a Gradient Boosting machine learning model. Enter the chemical properties of any wine sample and receive an instant quality prediction with a visual rating.

---

## ✨ Features

- **Instant Predictions** — Powered by a pre-trained Gradient Boosting model
- **Supports Red & White Wine** — Handles both wine types in one unified interface
- **Rich Dark UI** — Elegant wine-themed design with gold accents and hover effects
- **Animated Result Card** — Visual score display with star rating and quality badge
- **Grouped Input Sections** — Inputs organized by chemical category for easy entry

---

## 🖥️ Demo

![Wine Quality Predictor UI](https://via.placeholder.com/800x450.png?text=Wine+Quality+Predictor+Screenshot)

> Replace with an actual screenshot of your running app.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/wine-quality-predictor.git
cd wine-quality-predictor

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

---

## 📁 Project Structure

```
wine-quality-predictor/
│
├── app.py                 # Main Streamlit application
├── model_GB.pkl           # Pre-trained Gradient Boosting model
├── model_columns.pkl      # Feature column names for input alignment
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## 📦 Requirements

```txt
streamlit
pandas
scikit-learn
joblib
```

Install all at once:

```bash
pip install streamlit pandas scikit-learn joblib
```

---

## 🧪 Input Features

The model uses the following physicochemical properties as input:

| Feature | Description | Typical Range |
|---|---|---|
| **Wine Type** | Red or White | — |
| **Fixed Acidity** | Tartaric acid concentration | 4.0 – 16.0 |
| **Volatile Acidity** | Acetic acid (vinegar) level | 0.1 – 1.6 |
| **Citric Acid** | Freshness-contributing acid | 0.0 – 1.0 |
| **Residual Sugar** | Sugar remaining after fermentation | 0.9 – 65.0 |
| **Chlorides** | Salt content | 0.01 – 0.6 |
| **Free Sulfur Dioxide** | Free SO₂ (preservative) | 1 – 289 |
| **Total Sulfur Dioxide** | Total SO₂ | 6 – 440 |
| **Density** | Wine density (g/cm³) | 0.990 – 1.004 |
| **pH** | Acidity/alkalinity level | 2.7 – 4.0 |
| **Sulphates** | Antimicrobial additive | 0.2 – 2.0 |
| **Alcohol** | Alcohol by volume (%) | 8.0 – 15.0 |

---

## 📊 Model Details

| Property | Value |
|---|---|
| **Algorithm** | Gradient Boosting Regressor |
| **Training Data** | UCI Wine Quality Dataset |
| **Output** | Quality score (0–10 scale) |
| **File** | `model_GB.pkl` |

### Quality Score Interpretation

| Score | Rating | Badge |
|---|---|---|
| **≥ 7** | Excellent Quality | 🟢 |
| **5 – 6.9** | Average Quality | 🟡 |
| **< 5** | Low Quality | 🔴 |

---

## 🎨 UI Highlights

The interface features a custom dark wine-themed design:

- **Deep burgundy gradient background** with rich red tones
- **Gold accent palette** (`#c9a96e`) on labels, borders, and headings
- **Hover effects** on all input fields — glowing border on mouse-over
- **Animated prediction card** — fades in with score, colored divider, and ★ star rating
- **Playfair Display serif** font for headings; Inter for body text

---

## 📖 Dataset

This model was trained on the [UCI Wine Quality Dataset](https://archive.ics.uci.edu/ml/datasets/wine+quality):

> P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis. *Modeling wine preferences by data mining from physicochemical properties.* Decision Support Systems, 2009.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License. See `LICENSE` for details.

---

<p align="center">Made with 🍷 and Python</p>
