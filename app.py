from flask import Flask, render_template
import pandas as pd
from utils.charts import create_revenue_chart, create_profit_chart, create_expense_pie_chart, create_forecast_chart

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/dashboard")
def dashboard():
    revenue_fig = create_revenue_chart()
    profit_fig = create_profit_chart()
    expense_fig = create_expense_pie_chart()
    return render_template("dashboard.html", revenue_fig=revenue_fig, profit_fig=profit_fig, expense_fig=expense_fig)

@app.route("/forecast")
def forecast():
    forecast_fig = create_forecast_chart()
    return render_template("forecast.html", forecast_fig=forecast_fig)

if __name__ == "__main__":
    app.run(debug=True)
