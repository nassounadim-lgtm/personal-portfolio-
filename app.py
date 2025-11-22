from flask import Flask, render_template

app = Flask(__name__)

# ---------- Data models ----------
PROFILE = {
    "name": "Nasser Lahlou",
    "role": "Software Engineering Student",
    "short_bio": (
        "I am a software engineering student interested in web development, "
        "Python, and building clean, maintainable software."
    ),
    "email": "nassounadim@gmail.com",
    "location": "Barcelona, Spain",
    "github_url": "https://github.com/nassounadim-lgtm",
    "linkedin_url": "https://www.linkedin.com/in/your-profile",
}

PROJECTS = [
    {
        "title": "Portfolio Website",
        "description": "A personal portfolio website built using Python (Flask) and HTML/CSS.",
        "technologies": ["Python", "Flask", "HTML", "CSS"],
        "github_url": "https://github.com/nassounadim-lgtm/personal-portfolio",
    },
    {
        "title": "Sample CLI Tool",
        "description": "A small command-line tool written in Python.",
        "technologies": ["Python"],
        "github_url": "https://github.com/nassounadim-lgtm/sample-cli-tool",
    },
]


@app.route("/")
def index():
    return render_template("index.html", profile=PROFILE, projects=PROJECTS)


@app.route("/projects")
def projects():
    return render_template("projects.html", profile=PROFILE, projects=PROJECTS)


@app.route("/about")
def about():
    return render_template("about.html", profile=PROFILE)


@app.route("/contact")
def contact():
    return render_template("contact.html", profile=PROFILE)


if __name__ == "__main__":
    app.run(debug=True)

