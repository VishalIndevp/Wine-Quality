import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model_GB.pkl")
model_columns = joblib.load("model_columns.pkl")

st.set_page_config(
    page_title="Wine Quality Predictor",
    page_icon="🍷",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@300;400;500;600&display=swap');

* { box-sizing: border-box; }

.stApp {
    background: #0a0a0a !important;
    font-family: 'Inter', sans-serif;
}

.block-container {
    padding: 2.5rem 3rem 3rem 3rem !important;
    max-width: 100% !important;
}

#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }
div[data-testid="stToolbar"] { display: none; }
div[data-testid="stDecoration"] { display: none; }

.hero-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: clamp(4rem, 6vw, 7.5rem);
    line-height: 0.9;
    color: #ffffff;
    letter-spacing: 2px;
    margin-bottom: 1.8rem;
}
.hero-title .accent { color: #e50914; }

.hero-sub {
    color: #555;
    font-size: 0.9rem;
    font-weight: 300;
    line-height: 1.75;
    max-width: 380px;
    margin-bottom: 2.5rem;
}

.stats-row {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 0.75rem;
    margin-bottom: 1.5rem;
}

.stat-box {
    background: #111;
    border: 1px solid #1e1e1e;
    border-top: 2px solid #e50914;
    border-radius: 8px;
    padding: 1rem 1.2rem;
}

.stat-val {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 1.8rem;
    color: #fff;
    letter-spacing: 1px;
    line-height: 1;
}

.stat-lbl {
    font-size: 0.6rem;
    color: #444;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-top: 0.35rem;
}

.how-box {
    background: #110303;
    border: 1px solid #200808;
    border-left: 3px solid #e50914;
    border-radius: 8px;
    padding: 1.3rem 1.5rem;
}

.how-title {
    font-size: 0.62rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #e50914;
    margin-bottom: 0.6rem;
    font-weight: 600;
}

.how-text {
    color: #666;
    font-size: 0.85rem;
    line-height: 1.7;
    font-weight: 300;
}

.sec-label {
    font-size: 0.62rem;
    color: #e50914;
    letter-spacing: 3px;
    text-transform: uppercase;
    font-weight: 600;
    margin-bottom: 0.6rem;
    margin-top: 1.4rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.sec-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: #1a1a1a;
}

label,
div[data-testid="stSelectbox"] label,
div[data-testid="stNumberInput"] label {
    color: #444 !important;
    font-size: 0.62rem !important;
    font-weight: 500 !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    margin-bottom: 4px !important;
}

div[data-testid="stNumberInput"] input {
    background: #111 !important;
    border: 1px solid #222 !important;
    border-radius: 6px !important;
    color: #ffffff !important;
    font-size: 1rem !important;
    font-family: 'Inter', sans-serif !important;
    padding: 0.55rem 0.9rem !important;
    transition: border-color 0.2s !important;
}

div[data-testid="stNumberInput"] input:focus {
    border-color: #e50914 !important;
    box-shadow: 0 0 0 2px rgba(229,9,20,0.12) !important;
}

div[data-testid="stNumberInput"] button {
    background: #161616 !important;
    border: 1px solid #222 !important;
    color: #444 !important;
    border-radius: 5px !important;
}

div[data-testid="stNumberInput"] button:hover {
    border-color: #e50914 !important;
    color: #e50914 !important;
    background: rgba(229,9,20,0.08) !important;
}

div[data-testid="stSelectbox"] > div > div {
    background: #111 !important;
    border: 1px solid #222 !important;
    border-radius: 6px !important;
    color: #ffffff !important;
    font-size: 1rem !important;
}

div[data-testid="stSelectbox"] > div > div:focus-within {
    border-color: #e50914 !important;
}

.stButton > button {
    width: 100% !important;
    background: #e50914 !important;
    color: #ffffff !important;
    font-family: 'Bebas Neue', sans-serif !important;
    font-size: 1.3rem !important;
    letter-spacing: 5px !important;
    padding: 0.85rem 2rem !important;
    border: none !important;
    border-radius: 6px !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 24px rgba(229,9,20,0.3) !important;
    margin-top: 1.2rem !important;
}

.stButton > button:hover {
    background: #ff1a27 !important;
    box-shadow: 0 8px 36px rgba(229,9,20,0.5) !important;
    transform: translateY(-2px) !important;
}

.result-wrap {
    border-radius: 10px;
    padding: 2.2rem 1.8rem;
    text-align: center;
    margin-top: 1.2rem;
    border: 1px solid #1a1a1a;
}

.result-lbl {
    font-size: 0.62rem;
    letter-spacing: 4px;
    text-transform: uppercase;
    color: #444;
    margin-bottom: 0.5rem;
}

.result-num {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 6rem;
    line-height: 1;
    margin-bottom: 0.5rem;
}

.result-badge {
    display: inline-block;
    padding: 0.35rem 1.6rem;
    border-radius: 4px;
    font-size: 0.65rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    font-weight: 600;
}

.result-desc {
    margin-top: 1rem;
    font-size: 0.85rem;
    color: #555;
    font-weight: 300;
    line-height: 1.65;
}

.tier-ex { background: #0a150a; }
.tier-ex .result-num { color: #22c55e; }
.tier-ex .result-badge { background: rgba(34,197,94,0.12); color: #22c55e; border: 1px solid rgba(34,197,94,0.25); }

.tier-av { background: #150f00; }
.tier-av .result-num { color: #f59e0b; }
.tier-av .result-badge { background: rgba(245,158,11,0.12); color: #f59e0b; border: 1px solid rgba(245,158,11,0.25); }

.tier-lo { background: #150303; }
.tier-lo .result-num { color: #e50914; }
.tier-lo .result-badge { background: rgba(229,9,20,0.12); color: #e50914; border: 1px solid rgba(229,9,20,0.25); }

div[data-testid="column"]:first-child {
    border-right: 1px solid #161616;
    padding-right: 3rem !important;
}

div[data-testid="column"]:last-child {
    padding-left: 3rem !important;
}

/* ── FOOTER ── */
.footer {
    margin-top: 4rem;
    padding: 2.5rem 0 2rem;
    border-top: 1px solid #1a1a1a;
    text-align: center;
}

.footer-tagline {
    font-size: 0.72rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #444;
    margin-bottom: 0.5rem;
    font-weight: 400;
}

.footer-main {
    font-size: 0.72rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #444;
    margin-bottom: 2rem;
    font-weight: 400;
}

.footer-main .red { color: #e50914; }

.social-row {
    display: flex;
    justify-content: center;
    gap: 1rem;
    flex-wrap: wrap;
}

.social-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.55rem;
    padding: 0.65rem 1.4rem;
    background: #111;
    border: 1px solid #222;
    border-radius: 50px;
    color: #aaa !important;
    text-decoration: none !important;
    font-size: 0.88rem;
    font-weight: 500;
    font-family: 'Inter', sans-serif;
    transition: all 0.25s ease;
    letter-spacing: 0.3px;
}

.social-btn:hover {
    background: #1a1a1a;
    border-color: #e50914;
    color: #ffffff !important;
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(229,9,20,0.2);
}

.social-btn svg {
    width: 16px;
    height: 16px;
    fill: currentColor;
    flex-shrink: 0;
}
</style>
""", unsafe_allow_html=True)

# ── TWO COLUMN LAYOUT ──
left, right = st.columns([1, 1.1], gap="large")

# ════════════════════════════════
# LEFT
# ════════════════════════════════
with left:
    st.markdown("""
    <div class="hero-title">PREDICT<br><span class="accent">WINE</span><br>QUALITY.</div>
    <p class="hero-sub">Advanced Gradient Boosting model analyzing 11 chemical and physical properties to score wine quality with 69%.</p>
    <div class="stats-row">
        <div class="stat-box"><div class="stat-val">GB</div><div class="stat-lbl">Model Type</div></div>
        <div class="stat-box"><div class="stat-val">11</div><div class="stat-lbl">Features</div></div>
        <div class="stat-box"><div class="stat-val">LIVE</div><div class="stat-lbl">Status</div></div>
        <div class="stat-box"><div class="stat-val">1–10</div><div class="stat-lbl">Score Range</div></div>
    </div>
    <div class="how-box">
        <div class="how-title">↳ How It Works</div>
        <p class="how-text">This model analyzes chemical properties — including acidity levels, sulfur content, density, and alcohol concentration — to compute a wine quality score using Gradient Boosting.</p>
    </div>
    """, unsafe_allow_html=True)

# ════════════════════════════════
# RIGHT
# ════════════════════════════════
with right:

    st.markdown('<div class="sec-label">↳ Wine Selection</div>', unsafe_allow_html=True)
    wine_type = st.selectbox("Wine Variety", ["White", "Red"], label_visibility="collapsed")

    st.markdown('<div class="sec-label">↳ Acidity & Sugars</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        fixed_acidity    = st.number_input("Fixed Acidity", 0.0, 20.0, 7.0)
        citric_acid      = st.number_input("Citric Acid", 0.0, 2.0, 0.3)
    with c2:
        volatile_acidity = st.number_input("Volatile Acidity", 0.0, 2.0, 0.3)
        residual_sugar   = st.number_input("Residual Sugar", 0.0, 70.0, 6.0)

    st.markdown('<div class="sec-label">↳ Sulfur & Salts</div>', unsafe_allow_html=True)
    c3, c4 = st.columns(2)
    with c3:
        chlorides            = st.number_input("Chlorides", 0.0, 1.0, 0.05)
        free_sulfur_dioxide  = st.number_input("Free Sulfur Dioxide", 0.0, 300.0, 30.0)
    with c4:
        total_sulfur_dioxide = st.number_input("Total Sulfur Dioxide", 0.0, 500.0, 115.0)
        sulphates            = st.number_input("Sulphates", 0.0, 2.5, 0.5)

    st.markdown('<div class="sec-label">↳ Physical Properties</div>', unsafe_allow_html=True)
    c5, c6, c7 = st.columns(3)
    with c5:
        density = st.number_input("Density", 0.9800, 1.0100, 0.9950, format="%.4f")
    with c6:
        pH      = st.number_input("pH", 2.5, 4.5, 3.2)
    with c7:
        alcohol = st.number_input("Alcohol %", 5.0, 15.0, 10.0)

    if st.button("ANALYSE WINE QUALITY"):
        wine_enc = 0 if wine_type == "White" else 1
        user_input = {
            "type": wine_enc,
            "fixed acidity": fixed_acidity,
            "volatile acidity": volatile_acidity,
            "citric acid": citric_acid,
            "residual sugar": residual_sugar,
            "chlorides": chlorides,
            "free sulfur dioxide": free_sulfur_dioxide,
            "total sulfur dioxide": total_sulfur_dioxide,
            "density": density,
            "pH": pH,
            "sulphates": sulphates,
            "alcohol": alcohol
        }
        input_df = pd.DataFrame([user_input])
        input_df = input_df.reindex(columns=model_columns, fill_value=0)
        prediction = model.predict(input_df)[0]
        score = round(prediction, 2)

        if prediction >= 7:
            st.markdown(f"""
            <div class="result-wrap tier-ex">
                <div class="result-lbl">Quality Score</div>
                <div class="result-num">{score}</div>
                <div class="result-badge">✦ Excellent Quality</div>
                <p class="result-desc">A premium wine with exceptional characteristics — a pleasure worth savoring.</p>
            </div>""", unsafe_allow_html=True)
        elif prediction >= 5:
            st.markdown(f"""
            <div class="result-wrap tier-av">
                <div class="result-lbl">Quality Score</div>
                <div class="result-num">{score}</div>
                <div class="result-badge">◈ Average Quality</div>
                <p class="result-desc">A well-balanced wine — enjoyable for everyday drinking occasions.</p>
            </div>""", unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="result-wrap tier-lo">
                <div class="result-lbl">Quality Score</div>
                <div class="result-num">{score}</div>
                <div class="result-badge">◇ Below Average</div>
                <p class="result-desc">This wine falls below standard — its chemical balance may need refinement.</p>
            </div>""", unsafe_allow_html=True)

# ════════════════════════════════
# FOOTER
# ════════════════════════════════
st.markdown("""
<div class="footer">
    <p class="footer-tagline">I make predictions, not spoilers.</p>
    <p class="footer-main">Join my journey and let's <span class="red">explore together.</span></p>
    <div class="social-row">
        <a class="social-btn" href="https://www.linkedin.com/in/vishal-singh-here/" target="_blank">
            <svg viewBox="0 0 24 24"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 0 1-2.063-2.065 2.064 2.064 0 1 1 2.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
            LinkedIn
        </a>
        <a class="social-btn" href="https://x.com/vishalindev" target="_blank">
            <svg viewBox="0 0 24 24"><path d="M18.901 1.153h3.68l-8.04 9.19L24 22.846h-7.406l-5.8-7.584-6.638 7.584H.474l8.6-9.83L0 1.154h7.594l5.243 6.932ZM17.61 20.644h2.039L6.486 3.24H4.298Z"/></svg>
            X (Twitter)
        </a>
        <a class="social-btn" href="https://github.com/VishalIndevp" target="_blank">
            <svg viewBox="0 0 24 24"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg>
            GitHub
        </a>
        <a class="social-btn" href="https://www.instagram.com/vishalindev?igsh=dW9vbWk3Z28xb2U=" target="_blank">
            <svg viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 1 0 0 12.324 6.162 6.162 0 0 0 0-12.324zM12 16a4 4 0 1 1 0-8 4 4 0 0 1 0 8zm6.406-11.845a1.44 1.44 0 1 0 0 2.881 1.44 1.44 0 0 0 0-2.881z"/></svg>
            Instagram
        </a>
    </div>
</div>
""", unsafe_allow_html=True)