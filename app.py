from flask import Flask, render_template, request
import csv
import numpy as np

app = Flask(__name__)

# ---------- Profile data ----------
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
}

# ---------- Features used by the ML model ----------
FEATURE_NAMES = [
    "avg_return",
    "volatility",
    "liquidity",
    "risk_score",
    "momentum",
]

# ---------- Portfolio assets (financial) ----------
# Each asset has the same features the model uses
PROJECTS = [
    {
        "title": "Tech Growth ETF",
        "description": "High-growth technology-focused exchange-traded fund.",
        "technologies": ["ETF", "Technology"],  # used by templates
        "github_url": "https://www.example.com/tech-etf-info",
        "avg_return": 14,
        "volatility": 28,
        "liquidity": 9,
        "risk_score": 7,
        "momentum": 8,
    },
    {
        "title": "Blue Chip Dividend Stock",
        "description": "Stable stock with regular dividends and lower volatility.",
        "technologies": ["Stock", "Dividend"],
        "github_url": "https://www.example.com/blue-chip-info",
        "avg_return": 9,
        "volatility": 18,
        "liquidity": 8,
        "risk_score": 4,
        "momentum": 6,
    },
    {
        "title": "Emerging Markets Fund",
        "description": "Diversified fund investing in emerging economies.",
        "technologies": ["Fund", "Emerging Markets"],
        "github_url": "https://www.example.com/em-fund-info",
        "avg_return": 17,
        "volatility": 34,
        "liquidity": 7,
        "risk_score": 8,
        "momentum": 9,
    },
]


# ---------- Data loading + ML model ----------

def load_portfolio_data(path: str = "csv/portfolio_data.csv"):
    """
    Load financial asset data from CSV.
    Returns:
      - dataset: list of dicts with all features + grade
      - X: numpy array of shape (n_samples, n_features)
      - y: numpy array of shape (n_samples,)
    """
    dataset = []
    X_rows = []
    y_vals = []

    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            features = {}
            for name in FEATURE_NAMES:
                features[name] = float(row[name])
            grade = float(row["grade"])

            dataset.append({**features, "grade": grade})
            X_rows.append([features[name] for name in FEATURE_NAMES])
            y_vals.append(grade)

    X = np.array(X_rows, dtype=float)
    y = np.array(y_vals, dtype=float)
    return dataset, X, y


def fit_linear_regression(X: np.ndarray, y: np.ndarray):
    """
    Fit a multivariate linear regression model:
        y = bias + w1*x1 + ... + wn*xn
    using the normal equation: theta = (X^T X)^-1 X^T y
    """
    n_samples = X.shape[0]
    X_design = np.hstack([np.ones((n_samples, 1)), X])  # add bias column
    theta = np.linalg.pinv(X_design.T @ X_design) @ X_design.T @ y
    bias = float(theta[0])
    weights = theta[1:]
    return weights, bias


# Train model once at startup
DATASET, X_DATA, Y_DATA = load_portfolio_data()
WEIGHTS, BIAS = fit_linear_regression(X_DATA, Y_DATA)


def predict_grade_from_features(features: dict) -> float:
    """
    Predict a grade given a dict of financial features using the trained model.
    """
    x_vec = np.array([float(features[name]) for name in FEATURE_NAMES], dtype=float)
    return float(BIAS + np.dot(WEIGHTS, x_vec))


# ---------- Routes ----------

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


@app.route("/predict", methods=["GET", "POST"])
def predict():
    """
    ML page:
      - Shows the dataset used to train the model
      - Shows predicted grade for each portfolio asset
      - Lets the user enter custom financial metrics to get a predicted grade
    """
    # 1) Predictions for existing portfolio assets
    portfolio_predictions = []
    for asset in PROJECTS:
        features = {name: asset[name] for name in FEATURE_NAMES}
        predicted = round(predict_grade_from_features(features), 2)
        portfolio_predictions.append({
            "title": asset["title"],
            "features": features,
            "predicted_grade": predicted,
        })

    # 2) User interaction – custom input
    user_features = None
    user_prediction = None
    error = None

    if request.method == "POST":
        user_features = {}
        try:
            for name in FEATURE_NAMES:
                value_str = request.form.get(name, "").strip()
                if not value_str:
                    raise ValueError(f"Missing value for {name}")
                user_features[name] = float(value_str)

            user_prediction = round(predict_grade_from_features(user_features), 2)

        except ValueError as e:
            error = f"Invalid input: {e}"
            user_features = None
            user_prediction = None

    return render_template(
        "predict.html",
        profile=PROFILE,
        feature_names=FEATURE_NAMES,
        dataset=DATASET,
        portfolio_predictions=portfolio_predictions,
        user_features=user_features,
        user_prediction=user_prediction,
        error=error,
    )


# ---------- Run the app ----------
if __name__ == "__main__":
    app.run(debug=True)



