from enum import Enum, auto, unique


@unique
class TownName(Enum):
    BLACKSTONE = auto()
    LEAP_CREEK = auto()
    POUCH = auto()
    FIREFEN = auto()
    UNDERCLAW = auto()


@unique
class TownKeyword(Enum):
    ENDURE = auto()
    REVERSAL = auto()
    STUMBLE = auto()
    UNKNOWN_TBD = auto()
    OVERWHELM = auto()


@unique
class CombatStat(Enum):
    POWER = auto()
    AGILITY = auto()
    STAMINA = auto()
    CHI = auto()
    WIT = auto()


town_info = {
    TownName.BLACKSTONE: {
        "keyword": TownKeyword.ENDURE,
        "primary_stat": CombatStat.STAMINA,
        "secondary_stat": CombatStat.WIT
    },
    TownName.LEAP_CREEK: {
        "keyword": TownKeyword.REVERSAL,
        "primary_stat": CombatStat.CHI,
        "secondary_stat": CombatStat.AGILITY
    },
    TownName.POUCH: {
        "keyword": TownKeyword.STUMBLE,
        "primary_stat": CombatStat.WIT,
        "secondary_stat": CombatStat.CHI
    },
    TownName.FIREFEN: {
        "keyword": TownKeyword.UNKNOWN_TBD, # TODO: determine keyword
        "primary_stat": CombatStat.POWER,
        "secondary_stat": CombatStat.STAMINA
    },
    TownName.UNDERCLAW: {
        "keyword": TownKeyword.OVERWHELM,
        "primary_stat": CombatStat.AGILITY,
        "secondary_stat": CombatStat.POWER
    }
}
