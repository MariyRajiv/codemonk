<<<<<<< HEAD
# codemonk
=======
# 🧾 Paragraph Dashboard (Django Web App)

A simple Django-based web application to **submit**, **search**, and **manage paragraphs** with user login and a clean, modern UI.

---

## 📦 Features

- 🧑‍💻 User registration & login system
- 📝 Submit paragraphs
- 🔍 Search your submitted content
- 📋 Flash messages for feedback
- 🌐 Stylish dashboard UI with pure CSS (no JS)
- 💡 Built using Django, HTML, and CSS

---

## 🚀 Getting Started

Follow these steps to set up the project on your local machine.



## 🧾 Project Structure

```plaintext
paragraph-dashboard/
│
├── manage.py
├── requirements.txt
├── db.sqlite3
│
├── mysite/                # Django project settings
│   ├── settings.py
│   └── ...
│
├── search/                # Core app: views, templates, static
│   ├── static/
│   │   └── search/
│   │       └── dashboard_style.css
│   ├── templates/
│   │   └── dashboard.html
│   ├── views.py
│   ├── urls.py
│   └── ...
└── ...
```

---

## 🧱 Prerequisites

- ✅ [Python 3.8+](https://www.python.org/downloads/)
- ✅ [Git](https://git-scm.com/)
- ✅ Terminal (PowerShell, CMD, or Bash)

---

## 🔄 Clone the Repository

```bash
git clone https://github.com/yourusername/paragraph-dashboard.git
cd paragraph-dashboard
````

> Replace `yourusername` with your actual GitHub username.

---

## 🧪 Create and Activate Virtual Environment

### ▶️ Windows (PowerShell)

```bash
python -m venv env
.\env\Scripts\Activate
```

### ▶️ macOS/Linux

```bash
python3 -m venv env
source env/bin/activate
```

---

## 📦 Install Dependencies

```bash
pip install django

python -m django --version

```

---

## ⚙️ Django Project Setup

### Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## ▶️ Run the Development Server

```bash
python manage.py runserver
```

Then open your browser and visit:

```
http://127.0.0.1:8000/
```

---




>>>>>>> f9c0488 (Initial commit)
