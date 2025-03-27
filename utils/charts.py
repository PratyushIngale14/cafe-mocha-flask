import pandas as pd
import plotly.express as px
from prophet import Prophet

df = pd.read_csv("data/Cafe_Mocha_Financial_Data.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.drop_duplicates()
df.fillna(method='ffill', inplace=True)

def create_revenue_chart():
    df["Year"] = df["Date"].dt.year
    fig = px.line(df, x="Date", y="Revenue", title="📊 Revenue Over Time", animation_frame="Year")
    return fig.to_html(full_html=False)

def create_profit_chart():
    fig = px.line(df, x="Date", y="Profit", title="📈 Profit Trend Over Time")
    return fig.to_html(full_html=False)

def create_expense_pie_chart():
    latest = df.iloc[-1]
    labels = ["Marketing_Spend", "Food_Costs", "Labor_Costs", "Rent", "Utilities"]
    values = [latest[label] for label in labels]
    fig = px.pie(names=labels, values=values, title="💸 Latest Monthly Expense Breakdown")
    return fig.to_html(full_html=False)

def create_forecast_chart():
    prophet_df = df[["Date", "Revenue"]].rename(columns={"Date": "ds", "Revenue": "y"})
    model = Prophet(yearly_seasonality=True)
    model.fit(prophet_df)
    future = model.make_future_dataframe(periods=36, freq='MS')
    forecast = model.predict(future)
    forecast_fig = px.line(forecast, x="ds", y="yhat", title="📅 Forecasted Revenue (3 Years)")
    return forecast_fig.to_html(full_html=False)
