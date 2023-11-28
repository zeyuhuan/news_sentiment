from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

from news import search_news
from sentiment import append_sentiment

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

with open("resources/tickers.txt", "r") as f:
    tickers_to_name = {}
    for line in f.readlines():
        ticker, name = line.split("|")
        tickers_to_name[ticker] = name.strip()


@app.get("/")
async def read_root():
    return FileResponse("static/index.html")


@app.get("/fetch_tickers")
async def fetch_tickers():
    return JSONResponse(content=list(tickers_to_name.keys()))


@app.get("/check_ticker")
async def check_ticker(ticker: str):
    return append_sentiment(search_news(tickers_to_name[ticker]))
