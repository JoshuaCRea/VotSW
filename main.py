from npc_combat import get_attack_value, get_blk_value, get_mod_value
from keeper_of_scrolls import KeeperOfScrolls


def get_mod_msg(mod_value):
    if mod_value == "Wolf":
        return "Defense is reversal."
    if mod_value == "Star":
        return "Defense is reversal."
    return "Normal"


player_atk = "Hi"
player_blk = "Lo"
player_mod = "Normal"

kos_atk = get_attack_value()
kos_blk = get_blk_value()
kos_mod = get_mod_value()
kos_mod_msg = get_mod_msg(kos_mod)


print(f'Player atk: {player_atk}')
print(f'Player blk: {player_blk}')
print(f'Player mod: {player_mod}')
print()
print(f'KoS atk: {kos_atk}')
print(f'KoS blk: {kos_blk}')
print(f'KoS mod: {kos_mod}')
print(f'Kos mod msg: {kos_mod_msg}')













#Player selects card from hand
#Player selects mod on card, declares it before laying card down
#Player hits 'enter,' which officially 'submits' their selection, and also rolls the 3 dice for the NPC
#Program calculates results and deducts HP if necessary.
#Repeat until someone is defeated (all HP lost)