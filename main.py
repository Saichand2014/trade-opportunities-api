
from fastapi import FastAPI, Depends, HTTPException, Request
from services import get_market_data, analyze_with_ai
from auth import verify_token
from rate_limiter import rate_limit

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Trade Opportunities API running"}

@app.get("/analyze/{sector}")
async def analyze_sector(sector: str, request: Request, token: str = Depends(verify_token)):

    # Rate limit per IP
    rate_limit(request.client.host)

    # Input validation
    if not sector.isalpha():
        raise HTTPException(status_code=400, detail="Invalid sector name")

    try:
        data = await get_market_data(sector)
        report = await analyze_with_ai(data, sector)
    except Exception:
        raise HTTPException(status_code=500, detail="Processing failed")

    return {"report": report}
