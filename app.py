from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/resume")
def resume():
    return send_file("resume.pdf", as_attachment=True)


from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/projects/met-report")
def met_report():
    return render_template("met_report.html")

@app.route("/projects/upi-fraud-detection")
def upi_fraud_detection():
    return render_template("upi_fraud_detection.html")

@app.route("/projects/daily-news-portal")
def daily_news_portal():
    return render_template("daily_news_portal.html")

if __name__ == "__main__":
    app.run(debug=True)
