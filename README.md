# Hemihypertrophy Growth Tracker & Predictor

A personal AI-powered tool to track, visualize, and predict asymmetrical growth in children with hemihypertrophy. Built to help parents and caregivers monitor growth over time and support medical discussions with real data.

---

## 🚀 Features

* 📊 Track growth data (height, leg/arm length, weight)
* 📈 Visualize asymmetry trends over time
* 🤖 Predict future asymmetry using machine learning (linear regression)
* 📝 Add notes for medical therapy or milestones
* 🧑‍💻 (Optional) Web interface for easy data entry (via Streamlit)

---

## 📦 Technologies Used

* Python 3.x
* Pandas, NumPy
* scikit-learn (for ML regression)
* Seaborn, Matplotlib (for visualization)
* Streamlit (for optional frontend)

---

## 🧪 Getting Started

### Prerequisites

Install Python libraries:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn streamlit
```

### Run in Console Mode

```bash
python tracker.py
```

### Run with Streamlit (Web Interface)

```bash
streamlit run tracker.py
```

---

## 📝 How to Add Your Data

1. Either:

   * Edit the `load_data()` function in `tracker.py` to hard-code your child's measurements
   * OR keep data in a CSV file (e.g., `growth_data.csv`)
2. If using Streamlit, use the built-in form to enter data, which automatically saves it.

---

## 🧠 About the Predictions

This tool uses a basic linear regression model to forecast future growth trends, such as asymmetry in limb lengths. It's meant for visualization, **not medical diagnosis**.

---

## ⚠️ Disclaimer

This project is a personal tool created by a parent and is **not a substitute for professional medical advice**. Always consult your doctor or therapist for decisions regarding your child’s health.

---

## ❤️ Why I Built This

My child has hemihypertrophy. I built this project to monitor changes over time, track therapies, and help support conversations with healthcare providers using real data and visualizations.

---

## 📬 Contact

Feel free to reach out if you’re a parent, researcher, or developer interested in contributing or learning more.
