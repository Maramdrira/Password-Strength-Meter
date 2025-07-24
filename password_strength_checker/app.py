from flask import Flask, render_template, request
import os

def create_app():
    app = Flask(__name__, template_folder='templates')
    
    # Configuration
    app.config['MIN_WEAK'] = int(os.getenv("MIN_WEAK", 6))
    app.config['MIN_STRONG'] = int(os.getenv("MIN_STRONG", 10))
    app.config['SPECIAL_CHARS'] = os.getenv("SPECIAL_CHARS", "!@#$%^&*")

    @app.route("/", methods=["GET", "POST"])
    def index():
        strength = None
        if request.method == "POST":
            password = request.form.get("password", "")
            strength = check_strength(password)
        return render_template("index.html", strength=strength)

    return app

# Make the function available at module level
def check_strength(password):
    """Check password strength against configured rules"""
    if len(password) < app.config['MIN_WEAK']:
        return "Weak 🚨"
    elif len(password) < app.config['MIN_STRONG'] or not any(c in password for c in app.config['SPECIAL_CHARS']):
        return "Medium ⚠️"
    return "Strong ✅"

app = create_app()

if __name__ == "__main__":
    app.run()