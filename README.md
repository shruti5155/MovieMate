# 🎬 MovieMate: Personalized Movie Recommendation System

A content-based movie recommendation system that suggests similar movies based on user preferences, leveraging metadata and cosine similarity.

🔗 **Live Demo**: [https://moviemate-vk4e.onrender.com](https://moviemate-vk4e.onrender.com)

---

## 📌 Features

- 🎯 Personalized movie suggestions using **content similarity**
- 🧠 Cosine similarity on movie metadata for accurate recommendations
- 🖼️ High-quality poster display using **TMDB API**
- ⚡ Optimized loading using preprocessed `pickle` files for fast performance
- 🧑‍💻 Simple and clean **Streamlit web interface**

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **Pandas**
- **Pickle**
- **TMDB API (The Movie Database)**

---

## 🚀 Run Locally

```bash
# Clone the repository
git clone https://github.com/shruti5155/moviemate.git
cd moviemate

# (Optional but recommended) Create and activate virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
