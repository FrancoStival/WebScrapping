from DTOs.DTO_MonsterCards import DTO_LinkMonsterCard, DTO_StandardMonsterCard, DTO_PendulumMonsterCard, DTO_BaseMonsterCard
from DTOs.DTO_SpellCards import DTO_SpellCard
from DTOs.DTO_TrapCards import DTO_TrapCard
from DTOs.DTO_Card import Card

from Enum.MonsterEnum import MonsterRace, MonsterAttribute, MonsterType, LinkMarker
from Enum.SpellEnum import SpellType
from Enum.TrapEnum import TrapType

class CardParser:
    def parse(self, data: dict) -> Card:
        card_type = data.get("type", "")
        
        if card_type == "Spell Card":
            return self._parse_spell(data)
        
        if card_type == "Trap Card":
            return self._parse_trap(data)
        
        if "Monster" in card_type:
            return self._parse_monster(data)
            
        raise ValueError(f"Unknown card type: {card_type}")
    
    def _parse_monster(self, data: dict) -> DTO_BaseMonsterCard:
        typeline = data.get("typeline", [])

        types = [
            MonsterType(value)
            for value in typeline
            if value in MonsterType._value2member_map_
        ]

        common_data = {
            "name": data["name"],
            "description": data["desc"],
            "card_sets": data.get("card_sets", []),
            "price": data.get("card_prices", []),
            "attack_points": data["atk"],
            "race": MonsterRace(data["race"]),
            "attribute": MonsterAttribute(data["attribute"]),
            "type": types,
            "effect": data.get("monster_desc", data["desc"]),
            "archetype": data.get("archetype")
        }

        if MonsterType.LINK in types:
            return DTO_LinkMonsterCard(
                **common_data,
                link_rating=data["linkval"],
                link_markers=[
                    LinkMarker(marker)
                    for marker in data["linkmarkers"]
                ]
            )

        if MonsterType.PENDULUM in types:
            return DTO_PendulumMonsterCard(
                **common_data,
                defense_points=data.get("def"),
                level=data.get("level"),
                pendulum_scale=data["scale"],
                pendulum_description=data.get("pend_desc", "")
            )

        return DTO_StandardMonsterCard(
            **common_data,
            defense_points=data.get("def"),
            level=data.get("level")
        )

    def _parse_spell(self, data: dict) -> DTO_SpellCard:
        return DTO_SpellCard(
            name=data["name"],
            description=data["desc"],
            card_sets=data.get("card_sets", []),
            price=data.get("card_prices", []),
            spell_type=SpellType(data["race"]),
            archetype=data.get("archetype")
        )

    def _parse_trap(self, data: dict) -> DTO_TrapCard:
        return DTO_TrapCard(
            name=data["name"],
            description=data["desc"],
            card_sets=data.get("card_sets", []),
            price=data.get("card_prices", []),
            trap_type=TrapType(data["race"]),
            archetype=data.get("archetype")
        )