A Streamlit-based Text-to-Speech (TTS) application that detects the input language, translates it into a target language, and generates speech output.
Supports English, Hindi, Telugu, Tamil, and Kannada.

📌 Features

Language Detection – Automatically detects the input text language.

Translation – Translates input text into the selected target language.

Automatic Model Selection – Chooses the appropriate model (LSTM, GRU, CNN) based on the target language.

Speech Generation – Converts text into audio using Google TTS (gTTS).

Audio Playback – Plays generated speech directly in the browser.

Multi-language Support – Works with English, Hindi, Telugu, Tamil, and Kannada.

🚀 Tech Stack

Frontend: Streamlit

Translation: googletrans

Language Detection: langdetect

Text-to-Speech: gTTS

Backend Logic: Python

📂 Project Structure
.
├── Final_TTS.ipynb        # Jupyter notebook with experiments
├── tts_app.py             # Main Streamlit application
├── train.csv              # Training dataset
├── test.csv               # Test dataset
├── validation.csv         # Validation dataset
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
Installation

Clone this repository

git clone https://github.com/your-username/tts-multilingual.git
cd tts-multilingual


Create a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate


Install dependencies

pip install -r requirements.txt

▶️ Usage

Run the Streamlit app:

streamlit run tts_app.py


Then, open the provided local URL in your browser.

📊 Model Selection Logic
Language	Code	Model
English	en	LSTM
Hindi	hi	GRU
Telugu	te	CNN
Tamil	ta	LSTM
Kannada	kn	GRU
📌 Example

Enter a sentence in any supported language.

Choose your target language from the dropdown.

Click Generate Speech.

Listen to the generated audio directly on the webpage.
