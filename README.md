---

# Email Spam Detection

This repository hosts the **Email Spam Detection** project, an interactive web app built using Python and Streamlit. It uses a trained **Machine Learning** model to classify emails as spam or legitimate (ham).

---

## ✨ Features

- **Simple & Sleek UI** — Straightforward for anyone to use.
- **Instant Predictions** — Classify email content in real-time.
- **Machine Learning Powered** — Uses a trained Logistic Regression model.
- **Pretrained Integration** — Includes vectorizer and model loading via `pickle`.

---

## 📋 Table of Contents

1. [Overview](#-overview)
2. [Technologies Used](#-technologies-used)
3. [Setup and Installation](#-setup-and-installation)
4. [Project Workflow](#-project-workflow)
5. [Screenshots](#-screenshots)
6. [Future Enhancements](#-future-enhancements)

---

## 🌟 Overview

The **Email Spam Detection** app provides a real-world example of how Machine Learning can help prevent email spam. Simply paste any email content, and the model instantly predicts whether it's spam or not.

This project was built to combine **ML accuracy** with **real-world usability**, helping users make better decisions on suspicious emails.

---

## 🚀 Technologies Used

- **Python** — Backend and ML logic
- **Streamlit** — Frontend web interface
- **Pickle** — Model/vectorizer serialization
- **Logistic Regression** — For spam/ham classification

---

## 🛠️ Setup and Installation

### Prerequisites:

- Python 3.9+ must be installed

```bash
git clone https://github.com/sruthisoppa/Email-Spam-Detection.git
cd Email-Spam-Detection
```

### Install Dependencies:

```bash
pip install -r requirements.txt
```

### Launch the App:

```bash
streamlit run app.py
```

---

## 📈 Project Workflow

1. **User Input** — Paste email content in the app.
2. **Vectorization** — Text is converted to numerical data using `TfidfVectorizer`.
3. **Prediction** — Logistic Regression model predicts the outcome.
4. **Output** — Displays whether the email is SPAM or NOT SPAM.

---

## 🖼️ Screenshots

### 🏠 Home Page

![home.png](https://ik.imagekit.io/jxtjn4hpqj/Screenshot%202025-05-24%20095612.png?updatedAt=1748060803517)

---

## 🔮 Future Enhancements

- Add **Dark Mode**
- Enable testing with real-time email feeds
- Create a **REST API** version
- Upgrade to ensemble models (Random Forest / SVM)

