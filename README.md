# ☕ Chai Aur Django - Tweet Application

A responsive, feature-rich Tweet web application built using **Django 6** and styled with a clean custom **Bootstrap 5** dark mode theme. This application allows users to create, view, edit, and delete text tweets with optional media image uploads.

---

## ✨ Features
- 🌗 **Custom Dark Theme**: Fully styled with custom dark layouts using modern Bootstrap 5 utility classes.
- 📝 **Full CRUD Operations**: Users can Create, Read, Update, and Delete individual tweets.
- 🖼️ **Media Support**: Built-in support for uploading and rendering image attachments alongside text tweets.
- 🔒 **Route Protection**: Implements `login_required` route decorators to protect sensitive editing and posting pipelines.
- 📱 **Fully Responsive Layout**: Built with a master base template offering responsive mobile dropdown navigation structures.

---

## 🛠️ Project Structure
```text
django-project/
├── .venv/                  # Python Local Virtual Environment
├── chai_aur_django/        # Main Project Configuration Core Directory
│   ├── settings.py         # Base Project Configuration Framework Settings
│   └── urls.py             # Global Router File Endpoint Mapping Rules
├── tweet/                  # Tweet Feature Application Modular Folder
│   ├── templates/          # Application App View HTML Engine Templates
│   ├── forms.py            # Custom Django Form Model Processing Pipelines
│   ├── models.py           # Database Core Schema Structural Entities
│   ├── urls.py             # App Router Endpoint Path Configurations
│   └── views.py            # Core View Logic Business Controller Rules
├── templates/              # Global Master Structural Template Folder
│   └── layout.html         # Master Global Base HTML Architecture File
├── static/                 # CSS/JS Assets Directory
├── manage.py               # Django Command-Line Utility Script
├── .gitignore              # Local Version Tracking Protection Ignore Configurations
└── requirements.txt        # Frozen Active Application Dependencies Register
```

---

## 🚀 Local Installation & Setup Steps

Follow these execution guidelines inside your system terminal workspace to spin up a local instance:

### 1. Clone & Navigate into the Project Repository
```bash
git clone https://github.com
cd django-project
```

### 2. Configure Your Virtual Environment
```bash
# Create local workspace environment folder
python3 -m venv .venv

# Activate your newly created environment layer
source .venv/bin/activate
```

### 3. Install Active Application Dependencies
```bash
pip install -r requirements.txt
```

### 4. Execute Structural Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Local Administrator Superuser Profile
```bash
python manage.py createsuperuser
```

### 6. Launch the Local Development Server
```bash
python manage.py runserver
```

Open your favorite web browser utility software and navigate to the application endpoint address at:  
👉 **`http://127.0.0`**

---

## 📦 Technologies Used
- **Backend Framework**: Python 3.12 / Django 6.0.6
- **Database Engine**: SQLite 3 (Default Local Datastore Node)
- **Frontend Styles**: HTML5, Vanilla CSS3, Bootstrap 5.3.3 CDN Framework
