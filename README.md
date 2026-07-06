# 🌟 Dynamic Django Portfolio Web Application

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Version" />
  <img src="https://img.shields.io/badge/Django-6.0-green?style=for-the-badge&logo=django&logoColor=white" alt="Django Version" />
  <img src="https://img.shields.io/badge/Cloudinary-Cloud%20Hosting-lightgrey?style=for-the-badge&logo=cloudinary&logoColor=blue" alt="Cloudinary" />
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License" />
</p>

A premium, modern, and highly responsive portfolio application built using **Python, Django, and Bootstrap**. Designed with beautiful glassmorphism gradients, clean typography, interactive hover cards, and micro-animations to highlight your professional software development achievements.

---

## 🚀 Key Features

* **💼 Project Showcase**: Dynamic rendering of portfolio projects with detail pages, live demos, and GitHub repository links.
* **📄 Resume Management**: Streamlined resume file upload, download, and auto-cleanup mechanism when new versions are uploaded.
* **☁️ Cloudinary Storage Integration**: Real-time asset hosting for both job/project images and raw document storage (PDF resumes).
* **🛠️ Automated Database Clean-up**: Override save triggers on Django models prevent orphaned files on Cloudinary when records are updated/deleted.
* **📱 Responsive Glassmorphic UI**: Fluid web layout powered by Bootstrap, featuring custom CSS variables, gradient text, and radial background glow blobs.
* **⚡ Production Ready**: Complete with a `build.sh` pipeline, PostgreSQL config, and Whitenoise static file handling for seamless deployment on platforms like Render.

---

## 🛠️ Architecture & Tech Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Backend Framework** | Django 6.0 | Modern Python MVC framework for secure & scalable logic. |
| **Styling & Icons** | Bootstrap 5.3 + Bootstrap Icons | Elegant responsive layout & modern components. |
| **Media Storage** | Cloudinary | Asset delivery network for optimized image & file serving. |
| **Static Files** | Whitenoise | Middleware for serving static files efficiently in production. |
| **Database** | SQLite (Dev) / PostgreSQL (Prod) | Robust transactional database engines. |
| **Deployment** | Render Bash Pipeline | Auto-builds, applies migrations, and collects static resources. |

---

## 📂 Project Structure

```
portfolio/
│
├── jobs/                       # Core App for projects & resumes
│   ├── migrations/             # Database schema migrations
│   ├── templates/jobs/         # HTML Templates (home.html, project.html)
│   ├── admin.py                # Admin dashboard configurations
│   ├── models.py               # Models for Job, Resume, and Technology
│   └── views.py                # Route controller actions
│
├── portfolio/                  # Main Project Settings
│   ├── settings.py             # App configurations, middleware & secrets
│   ├── urls.py                 # Core routing configuration
│   └── wsgi.py                 # WSGI entry point
│
├── static/                     # Global static stylesheet assets
├── build.sh                    # Automation shell script for deployments
├── db.sqlite3                  # Local development database
├── requirements.txt            # Project dependencies list
└── manage.py                   # Django CLI executable
```

---

## ⚙️ Storage Configuration (Cloudinary)

The media storage is optimized to save all media files dynamically to Cloudinary:
* **Project Images**: Handled using `CloudinaryField` from the `cloudinary` SDK.
* **Resume Files (PDF)**: Managed via Django's `FileField` combined with `RawMediaCloudinaryStorage`.

### Cloudinary Credentials

Ensure you set the following environment variables in your deployment shell or system environment:

```env
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

> [!NOTE]
> In local development, if environment variables are not found, the configuration falls back gracefully to a `"dummy"` namespace to prevent site rendering crashes.

---

## 💻 Local Development Setup

To run the application locally on your machine, follow these steps:

### 1. Clone the Repository & Navigate in:
```bash
git clone https://github.com/bharathkumarkarri/Portfolio.git
cd Portfolio
```

### 2. Set Up a Virtual Environment & Activate:
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
```

### 3. Install Dependencies:
```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations:
```bash
python3 manage.py migrate
```

### 5. Create a Superuser (for Admin Dashboard Access):
```bash
python3 manage.py createsuperuser
```

### 6. Run the Local Server:
```bash
python3 manage.py runserver
```
Visit the application at: `http://127.0.0.1:8000/`

---

## ☁️ Deployment Guide (Render)

This project contains a pre-configured `build.sh` script specifically crafted for platform hosts like **Render**.

### Setup on Render:
1. Create a new **Web Service** on Render connected to your repository.
2. In the **Environment Settings**, specify the Python Environment version.
3. Add the following **Environment Variables**:
   * `SECRET_KEY`: A production-ready Django secret key.
   * `RENDER`: `True`
   * `DATABASE_URL`: PostgreSQL connection string.
   * `CLOUDINARY_CLOUD_NAME` / `CLOUDINARY_API_KEY` / `CLOUDINARY_API_SECRET`
4. Set the **Build Command** to:
   ```bash
   ./build.sh
   ```
5. Set the **Start Command** to:
   ```bash
   gunicorn portfolio.wsgi:application
   ```

---

## 🎨 UI & Aesthetics Details
* **Typography**: Sleek Google Font `Plus Jakarta Sans` for clean, professional readability.
* **Gradients**: Vibrant linear warm accent gradients (`#8d6e63` to `#ddb892`) used on primary actions and highlight elements.
* **Glassmorphism**: Backdrop blur filtering (`12px`) applied on fixed top navigation header for an ultra-premium layout feel.
* **Micro-animations**: Subtle translation transitions (`translateY(-8px)`) and scaling (`scale(1.08)`) on card hovers to build responsive interaction.
* **Dark Mode accents**: Classic `#080b12` footer background to ground the visual design.

---

## 📄 License

Distributed under the MIT License. See the [LICENSE](file:///Users/pavan/Documents/portfolio/LICENSE) file for more details.

---

## ✉️ Contact & Developer Info

* **Developer**: Karri Bharath Kumar
* **LinkedIn**: [@bharath-kumar-karri](https://www.linkedin.com/in/bharath-kumar-karri/)
* **GitHub**: [@bharathkumarkarri](https://github.com/bharathkumarkarri)
* **Email**: [bharath.karri23@gmail.com](mailto:bharath.karri23@gmail.com)
