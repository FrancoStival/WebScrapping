from DTOs.DTO_Card import Card
from Enum.SpellEnum import SpellType

class DTO_SpellCard(Card):
    def __init__(self, name, description, card_sets, archetype, price, spell_type):
        super().__init__(name, description, card_sets, archetype, price)
        self.spell_type: SpellType = spell_type
        
    