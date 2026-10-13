import requests
import logging
import json
import os
from constants import CONSTANTS
from Parser.CardParser import CardParser

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log", mode="a", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

def fetch_data(url: str) -> requests.Response:
    logging.debug("Attempting to fetch data")
    response = requests.get(url, headers={})

    if response.status_code == 200:
        logging.info("Data fetched successfully")
        return response.json()
    else:
        response.raise_for_status()

def parse_data(data):
    parser = CardParser()
    cards = []

    for card in data:
        card_name = card.get("name")
        card_type = card.get("type", "")
        logging.debug(f"Processing card: {card_name}")
        
        if card_type == "Skill Card":
            logging.debug(f"Skipping Skill Card: {card_name}")
            continue
        
        if card_type == "Token":
                    logging.debug(f"Skipping Token Card: {card_name}")
                    continue
        
        if ("Monster" in card_type or card_type in ("Spell Card", "Trap Card")) and not card.get("race"):
            logging.warning(f"Skipping card without race: {card_name}")
            continue
        
        parsed_card = parser.parse(card)
        cards.append(parsed_card)

    return cards


if __name__ == "__main__":
    json_path = "cards.json"

    if os.path.exists(json_path):
        logging.info("Loading data from JSON")
        with open(json_path, "r", encoding="utf-8") as file:
            data = json.load(file)
    else:
        logging.info("Fetching data from API")
        url = CONSTANTS["Yu_Gi_Oh_DB"]
        data = fetch_data(url)

        with open(json_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        logging.info("Data saved to JSON")

    cards_data = data["data"] if isinstance(data, dict) else data
    cards : list = parse_data(cards_data)
    logging.info(f"Processed {len(cards)} cards")