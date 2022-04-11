from npc_combat import get_attack_value, get_blk_value, get_mod_value


atk = get_attack_value()
blk = get_blk_value()
mod = get_mod_value()


print(atk)
print(blk)
print(mod)


#Player selects card from hand
#Player selects mod on card, enters before laying it down
#Player hits 'enter,' which officially 'submits' their selection, and also rolls the 3 dice for the NPC
#Program calculates results and deducts HP if necessary.
#Repeat until someone is defeated (all HP lost)