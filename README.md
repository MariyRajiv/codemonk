▶️ [Click here to watch the demo](https://www.loom.com/share/4601d93d86884e75910a32276fcfa405?sid=57c14a63-f568-4f58-8363-cf24c06cf0a3)

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

## ⚡ Getting Started (with Docker)

This is the recommended way to run the project.

### ✅ Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running

---

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/MariyRajiv/codemonk.git
cd paragraph
````

---

### 2️⃣ Generate `requirements.txt` (Optional, only if not present)

> If you've already installed packages locally and want to generate `requirements.txt`, run:

```bash
# On Windows PowerShell
.\env\Scripts\activate
pip freeze > requirements.txt
```

---

### 3️⃣ Build Docker Image

```bash
docker-compose build --no-cache
```

🔍 **What this does:**

* Builds a Docker image using the `Dockerfile`
* Installs all Python dependencies listed in `requirements.txt`

---

### 4️⃣ Start the Django Application

```bash
docker-compose up
```

🔍 **What this does:**

* Starts the Django development server inside a Docker container
* Binds the app to `localhost:8000` on your machine

Once you see:

```
Starting development server at http://0.0.0.0:8000/
```

➡️ Open your browser and go to: [http://localhost:8000/](http://localhost:8000/)

---

### 5️⃣ Run Migrations (in a new terminal tab)

```bash
docker-compose exec web python manage.py migrate
```

🔍 **What this does:**

* Applies all database migrations to set up the initial schema (creates `db.sqlite3`)

---

### 6️⃣ Create Superuser (Optional but recommended)

```bash
docker-compose exec web python manage.py createsuperuser
```

🔍 **What this does:**

* Prompts you to create an admin user for accessing the Django admin panel at `/admin/`

---

## 🛠️ Useful Commands

| Command                             | Purpose                                    |
| ----------------------------------- | ------------------------------------------ |
| `docker-compose build`              | Build or rebuild the Docker image          |
| `docker-compose up`                 | Start the app and its services             |
| `docker-compose down`               | Stop and remove containers                 |
| `docker-compose exec web <command>` | Run a command inside the running container |

---


Now open your browser and go to 👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 👨‍💻 Development (Without Docker - Optional)

If you want to run the project locally using Python and virtualenv:

### 1️⃣ Create a Virtual Environment

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

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4️⃣ Start the Server

```bash
python manage.py runserver
```

Then visit 👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## ✅ You're All Set!

If you're using Docker, you never need to install Python or Django locally — it's all handled inside the container. Happy coding! 🚀

```


