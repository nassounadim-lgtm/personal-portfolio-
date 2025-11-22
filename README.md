# Personal Portfolio Website (Software Engineering Project)
This is a personal portfolio website built using **Python** and the **Flask** web framework.  
It was created as part of a Software Engineering class project to demonstrate:

- Basic backend development with Python  
- Use of the Flask web framework  
- Clean project structure (templates, static files, routing)  
- Basic testing using pytest  
- Version control using Git and GitHub  

---

## 🚀 Features

### ✔ Home Page
- Introduces who I am  
- Shows highlighted projects with descriptions and technologies  

### ✔ Projects Page
- Displays all listed projects  
- Includes links to GitHub repositories  

### ✔ About Page
- Provides background information  
- Lists skills and education  

### ✔ Contact Page
- Shows email, GitHub, and LinkedIn links  

---

## 🗂 Project Structure

```
personal-portfolio/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── projects.html
│   ├── about.html
│   └── contact.html
├── static/
│   └── css/
│       └── style.css
└── tests/
    └── test_app.py
```

---

## ▶️ How to Run the Website

### 1. Create and activate a virtual environment (Mac)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Flask application

```bash
python app.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000
```

---

## 🧪 Running Tests

You can run the automated tests using:

```bash
pytest
```

---

## 👤 Author

**Nasser Lahlou**  
GitHub: https://github.com/nassounadim-lgtm
