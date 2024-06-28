from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route("/", methods=["GET", "POST"])
def index():
    if "number_to_guess" not in session:
        session["number_to_guess"] = random.randint(1, 100)
        session["attempts"] = 0
    
    message = None
    
    if request.method == "POST":
        try:
            guess = int(request.form["guess"])
            session["attempts"] += 1
            
            if guess < session["number_to_guess"]:
                message = "Your guess is too low. Try again!"
            elif guess > session["number_to_guess"]:
                message = "Your guess is too high. Try again!"
            else:
                message = f"Congratulations! You guessed the number {session['number_to_guess']} in {session['attempts']} attempts."
                session.pop("number_to_guess", None)
                session.pop("attempts", None)
        except ValueError:
            message = "Invalid input. Please enter a valid number."
    
    return render_template("index.html", message=message, attempts=session.get("attempts"))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
