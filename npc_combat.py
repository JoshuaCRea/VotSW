import random


def roll_for_clash_value(num):
    if num == 1 or num == 6:
        return "Hi"
    elif num == 2 or num == 5:
        return "Mid"
    elif num == 3 or num == 4:
        return "Lo"


def get_mod_value(num):
    if num == 1:
        return "Wolf"
    elif num == 6:
        return "Star"
    else:
        return "Normal"


def get_mod_message(mod_value):
    if mod_value == "Wolf":
        return "Defense is reversal."
    if mod_value == "Star":
        return "Defense is reversal."
    return "No modification."


def get_npc_clash_values():
    atk = roll_for_clash_value(random.randint(1, 6))
    blk = roll_for_clash_value(random.randint(1, 6))
    mod = get_mod_value(random.randint(1, 6))
    return atk, blk, mod


def clash(player_atk, player_blk, player_mod, player, npc_atk, npc_blk, npc_mod, npc):
    player_hits_npc = player_atk != npc_blk
    npc_hits_player = npc_atk != player_blk

    if npc_hits_player:
        if player_mod != "Overwhelm":
            player.receive_damage(1)
    elif player_mod == "Reversal":
        npc.receive_damage(1)
    
    if player_hits_npc:
        npc.receive_damage(1)
    elif npc_mod == "Wolf" or npc_mod == "Star":
        player.receive_damage(1)    
