from DTOs.DTO_Card import Card
from Enum.MonsterEnum import *

class DTO_BaseMonsterCard(Card):
    def __init__(self, name, description, card_sets, archetype, price, attack_points, race, attribute, type, effect):
        super().__init__(name, description, card_sets, archetype, price)
        self.attack_points: int = attack_points
        self.race: MonsterRace = race # Warrior, Dragon
        self.attribute: MonsterAttribute = attribute
        self.type: MonsterType = type #Link, Fusion...
        self.effect: bool = effect

class DTO_LinkMonsterCard(DTO_BaseMonsterCard):
    def __init__(self, name, description, card_sets, archetype, price, attack_points, race, attribute, type, effect, link_rating, link_markers):
        super().__init__(name, description, card_sets, archetype, price, attack_points, race, attribute, type, effect)
        self.link_rating: int = link_rating
        self.link_markers: list[LinkMarker] = link_markers
        
class DTO_StandardMonsterCard(DTO_BaseMonsterCard):
    def __init__(self, name, description, card_sets, archetype, price, attack_points, race, attribute, type, effect, defense_points, level):
        super().__init__(name, description, card_sets, archetype, price, attack_points, race, attribute, type, effect)
        self.defense_points: int = defense_points
        self.level: int = level
        
class DTO_PendulumMonsterCard(DTO_StandardMonsterCard):
    def __init__(self, name, description, card_sets, archetype, price, attack_points, race, attribute, type, effect, defense_points, level, pendulum_scale, pendulum_description):
        super().__init__(name, description, card_sets, archetype, price, attack_points, race, attribute, type, effect, defense_points, level)
        self.pendulum_scale: int = pendulum_scale
        self.pendulum_description: str = pendulum_description
        
