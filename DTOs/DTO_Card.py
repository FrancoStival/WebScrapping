class Card:
    def __init__(self, name, description, card_sets, archetype, price):
        self.name: str = name
        self.description: str = description
        self.card_sets: list = card_sets
        self.archetype: str = archetype
        self.price: list = price
        
        
