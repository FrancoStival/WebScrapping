from DTOs.DTO_Card import Card
from Enum.TrapEnum import TrapType

class DTO_TrapCard(Card):
    def __init__(self, name, description, card_sets, archetype, price, trap_type):
        super().__init__(name, description, card_sets, archetype, price)
        self.trap_type: TrapType = trap_type