# 📊 Kaggle Datasets Explorer

## 🚀 Project Overview

LINK TO PLOTLY : https://5f8676d2-e954-477e-a11d-8777dc24d4ba.plotly.app/?code=01K9RRDSSB1984RWTTSTTYSYR0&state=VHd77vwt1dvhyjCxthGWXJa3TH1sat3qqdQPe2nDGEc%3D

**Kaggle Datasets Explorer** is a powerful tool designed to automatically collect, analyze, and prepare open datasets from Kaggle for machine learning workflows. It is optimized for **Supervised Machine Learning (SML)** with **multi-class and multi-output classification tasks**.

This project enables users to:

* ⚡ Efficiently fetch thousands of unique Kaggle datasets via the Kaggle API.
* 🧹 Clean and deduplicate datasets to ensure high-quality data.
* 📈 Analyze datasets for feature uniqueness, distribution, and relevance.
* 🤖 Seamlessly prepare datasets for multi-class and multi-output models.

---

## ✨ Key Features

* **🔑 Kaggle API Integration**: Authenticate and download datasets automatically.
* **🗑️ Data Deduplication**: Remove duplicates based on key columns such as `subtitle`.
* **📌 Essential Column Extraction**: Keep only the most relevant columns for analysis.
* **🔍 Unique Value Analysis**: Quantify uniqueness across dataset columns.
* **🤖 SML-Ready Preparation**: Transform datasets for multi-class and multi-output machine learning.
* **💾 CSV Export**: Save cleaned and processed datasets for reuse.

---

## 🛠 Installation

1. Clone the repository:

```bash
git clone https://github.com/username/kaggle-datasets-explorer.git
cd kaggle-datasets-explorer
```

2. (Optional) Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

**📚 Required Libraries:**

* `pandas`
* `numpy`
* `kaggle`
* `tqdm`

---

## 🏃 Usage

1. **🔑 Authenticate Kaggle API:**

```python
from kaggle.api.kaggle_api_extended import KaggleApi
api = setup_kaggle_api()  # Set up with your Kaggle token
```

2. **📦 Fetch datasets:**

```python
data = fetch_unique_datasets(api, total=8000)  # Fetch 8000 unique datasets
```

3. **💾 Save to CSV:**

```python
save_to_csv(data, filename='kaggle_unique_datasets.csv')
```

4. **🧹 Remove duplicate rows:**

```python
df_filtered = df.drop_duplicates(subset=['subtitle']).reset_index(drop=True)
```

5. **📌 Keep essential columns:**

```python
essential_columns = ['subtitle', 'creatorname', 'totalbytes', 'downloadcount', 'lastupdated', 'tags', 'url']
df_filtered = df_filtered[essential_columns]
```

6. **🤖 Prepare for multi-class / multi-output models:**

```python
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df_filtered['subtitle_encoded'] = le.fit_transform(df_filtered['subtitle'])
```

---

## 📊 Machine Learning Example

```python
from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier

X = df_filtered.drop(columns=['subtitle_encoded'])
y = df_filtered['subtitle_encoded']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = MultiOutputClassifier(RandomForestClassifier(n_estimators=100, random_state=42))
model.fit(X_train, y_train)

score = model.score(X_test, y_test)
print(f"Model Accuracy: {score:.4f}")
```

---

## 🤝 Contribution

* Pull requests and issues are welcome.
* ✨ Write clean, modular code with clear documentation.
* 🔄 Ensure reproducibility when working with datasets and models.

---

## 📜 License

MIT License © [Your Name]

---

This project empowers data scientists to efficiently explore Kaggle datasets and build robust multi-class and multi-output machine learning models, providing a complete end-to-end workflow from data collection to model evaluation. 🌟
