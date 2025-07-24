from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Load rules from environment variables (or defaults)
MIN_WEAK = int(os.getenv("MIN_WEAK", 6))
MIN_STRONG = int(os.getenv("MIN_STRONG", 10))
SPECIAL_CHARS = os.getenv("SPECIAL_CHARS", "!@#$%^&*")

@app.route("/", methods=["GET", "POST"])
def index():
    strength = None
    if request.method == "POST":
        password = request.form.get("password", "")
        strength = check_strength(password)
    return render_template("index.html", strength=strength)

def check_strength(password):
    if len(password) < MIN_WEAK:
        return "Weak 🚨"
    elif len(password) < MIN_STRONG or not any(c in password for c in SPECIAL_CHARS):
        return "Medium ⚠️"
    else:
        return "Strong ✅"

if __name__ == "__main__":
    app.run()