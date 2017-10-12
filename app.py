from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/pricing")
def pricing():
    return render_template("pricing.html")

@app.route("/location")
def location():
    return render_template("location.html")

@app.route("/faqs")
def faqs():
    return render_template("faqs.html")

@app.route("/terms")
def terms():
    return render_template("terms.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=4000)