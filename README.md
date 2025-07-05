# 🧠 Sentiment Analyzer using Transformers

An AI-powered sentiment analysis web application built with Python, Hugging Face Transformers, and Flask. It classifies user-input text into **positive**, **negative**, or **neutral** sentiment in real-time.

---

## 🚀 Features

- 🔍 Real-time sentiment prediction
- 🤖 Transformer-based NLP model (distilBERT)
- 🧪 Easy testing with a web form interface
- 📝 Clean and minimal Flask backend
- 📦 Virtual environment support for easy setup

---

## 🛠️ Technologies Used

- Python 3.x
- [Transformers](https://huggingface.co/transformers/) (Hugging Face)
- Flask
- `torch`
- `sentence-transformers`
- HTML/CSS (for UI)

---

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/Durgadevi161105/sentiment-analyzer.git
cd sentiment-analyzer


2. **Create a virtual environment**

python -m venv sentiment-env


3. **Activate the environment
**
    On Windows:

sentiment-env\Scripts\activate

4. **Install the dependencies
**

pip install -r requirements.txt
   ( If requirements.txt is not created yet, you can generate it with:)

pip freeze > requirements.txt


▶️  **Run The App**

python sentiment_core.py


🧪 **Example**

Enter a sentence like:

I really enjoyed the service today!

And get a response:

Sentiment: Positive 😊





