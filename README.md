
# 🧾 Paragraph Dashboard

A **Django web application** where users can register, log in, submit paragraphs, and search their content with a clean dashboard UI.

---

## ✨ Features

* 👤 User registration & login
* 📝 Submit and store paragraphs
* 🔍 Search through your submissions
* 🎨 Minimal UI with pure Html and CSS

---

## 📂 Project Structure

```plaintext
paragraph-dashboard/
│
├── manage.py
├── requirements.txt
├── db.sqlite3
│
├── mysite/                  # Django project settings
│   ├── settings.py
│   └── ...
│
├── search/                  # Core app
│   ├── static/search/dashboard_style.css
│   ├── templates/dashboard.html
│   ├── views.py
│   ├── urls.py
│   └── ...
```

---

## ⚡ Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/MariyRajiv/codemonk.git
cd paragraph
```

### 2️⃣ Create a Virtual Environment

**Windows (PowerShell):**

```bash
python -m venv env
.\env\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv env
source env/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install django

python -m django --version
```

### 4️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Start the Server

```bash
python manage.py runserver
```

Now open your browser and go to 👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---


