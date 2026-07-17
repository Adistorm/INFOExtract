# 🎬 CineSage - AI Information Extractor

CineSage is an AI-powered information extraction application built using **LangChain**, **Mistral AI**, and **Streamlit**. It analyzes any paragraph, identifies the type of content, extracts the most relevant information, and generates a concise summary.

Whether the input is about a movie, book, company, product, person, or event, CineSage intelligently extracts the key details in a clean, human-readable format.

---

## ✨ Features

- 📄 Extracts key information from any paragraph
- 🎯 Automatically identifies the content type
- 📝 Generates a quick summary
- 📌 Highlights important facts and entities
- 🤖 Powered by Mistral AI via LangChain
- 🌐 Simple and responsive Streamlit interface

---

## 🛠️ Tech Stack

- Python
- LangChain
- Mistral AI
- Streamlit
- Python Dotenv

---

## 📂 Project Structure

```
CineSage/
│── app.py               # Streamlit UI
│── requirements.txt     # Project dependencies
│── .env                 # API Keys
│── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/Adistorm/CineSage.git

cd CineSage
```

### Create a virtual environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
MISTRAL_API_KEY=your_api_key_here
```
## ▶️ Run the Application
```bash
streamlit run app.py
```
The application will be available at
```
http://localhost:8501
```
## 📖 Example Input
```
Interstellar is a visually stunning science fiction epic directed by Christopher Nolan. Released in 2014, the film stars Matthew McConaughey, Anne Hathaway, Jessica Chastain, and Michael Caine. The story revolves around astronauts traveling through a wormhole near Saturn in search of a new home for humanity.
```

## 📌 Example Output

### Content Type

Movie

### Movie Information

- Movie Name: Interstellar
- Director: Christopher Nolan
- Release Year: 2014
- Genre: Science Fiction
- Cast:
  - Matthew McConaughey
  - Anne Hathaway
  - Jessica Chastain
  - Michael Caine

### Summary

Interstellar is a science fiction film directed by Christopher Nolan. The story follows astronauts searching for a new home for humanity through a wormhole near Saturn. The movie is known for its emotional storytelling and scientific accuracy.

---

## 📦 Requirements

- Python 3.10+
- Streamlit
- LangChain
- LangChain-MistralAI
- Python Dotenv

---

## 🚀 Future Improvements

- PDF Information Extraction
- Website Content Extraction
- OCR Support for Images
- Structured JSON Output
- Export Results as PDF
- Save Extraction History

---

## 👨‍💻 Author

**Aditya Petewar**

GitHub: https://github.com/Adistorm

---

## 📄 License

This project is licensed under the MIT License.
