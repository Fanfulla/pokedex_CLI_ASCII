import requests
import json
from rapidfuzz import fuzz, process

def get_pokemon_info(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_all_pokemon_names() -> list[str]:
    url = "https://pokeapi.co/api/v2/pokemon?limit=20000"
    r = requests.get(url, timeout=15)
    r.raise_for_status()
    data = r.json()
    return [item["name"] for item in data.get("results", [])]

def suggest_names(query: str, names: list[str], limit: int = 5, min_score: int = 70) -> list[str]:
    # process.extract return [(match, score, index), etc]
    matches = process.extract(
        query,
        names,
        scorer=fuzz.WRatio,
        limit=limit
    )
    return [m[0] for m in matches if int(m[1]) >= min_score]
