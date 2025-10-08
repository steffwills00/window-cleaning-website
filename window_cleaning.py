from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed for flash messages

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/book", methods=["POST"])
def book():
    # Get form data
    name = request.form.get("name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    address = request.form.get("address")
    service = request.form.get("service")
    date = request.form.get("date")
    notes = request.form.get("notes")

    # For now, just print to console (you can replace with database/email logic)
    print("New booking received:")
    print(f"Name: {name}, Email: {email}, Phone: {phone}, Address: {address}")
    print(f"Service: {service}, Date: {date}, Notes: {notes}")

    # Show a simple thank-you message on the same page
    flash("Thank you! Your booking request has been received. We'll contact you shortly.")
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
