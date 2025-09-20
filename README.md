<img
  src="./assets/usage.gif"
  alt="OMDb Client — Usage"
  style="width: 100%"
/>

**🎬 OMDb Client** is a web application that allows searching for movies, series, and episodes by title through the **OMDb API**. For each result, it displays the poster, title, year, type, and a reference link to IMDb.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css&logoColor=white)

## 🛠️ Installation and Execution

Developed in **Python 3.12**, using this version is recommended to ensure compatibility. Follow these steps from the project root:

### 1️⃣ Configure Secrets

Create a `.streamlit/secrets.toml` file with:

```toml
OMDB_API_URL = "http://www.omdbapi.com/"
OMDB_API_KEY = "YOUR_OMDB_API_KEY"
IMDB_TITLE_URL = "https://www.imdb.com/title/"
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the App

```bash
streamlit run main.py
```

## 🤝 Donation

If you like this project and want to support it financially, you can contribute via **PayPal** or **Pix** — _aos meus chegados do Brasil_ — by clicking one of the options below:

[![PayPal](https://img.shields.io/badge/PayPal-Donate-1040C1?labelColor=121661&style=for-the-badge&logo=paypal&link=https://www.paypal.com/donate/?hosted_button_id=2P9HPGUP7Z43S)](https://www.paypal.com/donate/?hosted_button_id=2P9HPGUP7Z43S)
[![Pix](https://img.shields.io/badge/Pix-Doar-FBB88A?labelColor=F26722&style=for-the-badge&logo=pix&logoColor=ffffff&link=https://tipa.ai/davidsantana06)](https://tipa.ai/davidsantana06)

## ⚖️ License

This project uses the **MIT License**, allowing you to use and modify the code freely. The only requirement is to give proper credit, recognizing the effort and time invested.
