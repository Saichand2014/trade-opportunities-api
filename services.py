
import httpx

async def get_market_data(sector: str):
    url = f"https://api.duckduckgo.com/?q={sector}+industry+India&format=json"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    return response.text[:1000]


async def analyze_with_ai(data, sector):
    return f"""
# {sector.capitalize()} Sector Analysis

## Market Trends
- Growth observed in {sector} sector in India
- Increasing investments and innovation

## Opportunities
- Expansion into rural and global markets
- Government initiatives support

## Risks
- Regulatory challenges
- High competition

## Summary
The {sector} sector shows promising growth with moderate risks.
"""
