# app.py

from flask import Flask, render_template, request, redirect, url_for, session
from config import SECRET_KEY, ADMINS

app = Flask(__name__)
app.secret_key = SECRET_KEY

# --- Home Route ---
@app.route("/")
def home():
    return render_template("index.html")

# --- Admin Login (simple auth with ID) ---
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        admin_id = request.form.get("admin_id")
        if admin_id and int(admin_id) in ADMINS:
            session["admin"] = admin_id
            return redirect(url_for("admin"))
        return "❌ Invalid Admin ID!"
    return render_template("login.html")

# --- Admin Panel ---
@app.route("/admin")
def admin():
    if "admin" not in session:
        return redirect(url_for("login"))
    return render_template("admin.html", admin_id=session["admin"])

# --- Logout ---
@app.route("/logout")
def logout():
    session.pop("admin", None)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
