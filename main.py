from npc_combat import get_attack_value, get_blk_value, get_mod_value
from combat_card import get_combat_cards
import random


'''
●   SELECTION PHASE - Combatants select 1 card from hand and place it on the table face down. Each player will then announce how they will play that card by stating the number associated to the Special they intend to use on that particular card.
●  	REVEAL STEP - Both players flip card face up, and immediately place a stone on top if applicable.
●  	REACTION PHASE - Each player may make one reaction, if Specials or Techniques allow for it. This phase is also where Non-Player Adversaries will apply the effects of the White Die, unless otherwise noted. A player who has chosen “stumble” can change his or her special selection during this phase.
●  	CALCULATION STEP - Determine what happened in this clash. Subtract applicable HP.
●  	ACTIVATION PHASE - This is when you activate technique cards that will be played in the next clash. No more than 1 Technique per player may be played in a single clash.
'''

#select card (A-E)
#select special (1, 2, or 3)
#hit enter (play the clash)

def get_mod_message(mod_value):
    if mod_value == "Wolf":
        return "Defense is reversal."
    if mod_value == "Star":
        return "Defense is reversal."
    return "No modification."


def clash(pa, pb, ph, ka, kb, kh):
    if ka != pb:
        ph -= 1
    if pa != kb:
        kh -= 1
    return ph, kh


print("====== START ======\n")

player_hp = 5
kos_hp = 5
print(f'Player HP: {player_hp}')
print(f'Kos HP: {kos_hp}')

print("\nAvailable Player Combat Cards:")
combat_cards = get_combat_cards()
random.shuffle(combat_cards)
round_one_hand = combat_cards[0:5]
for card in round_one_hand:
    print(card)

i = 0
while player_hp > 0 and kos_hp > 0:
    player_atk = combat_cards[0].attack
    player_blk = combat_cards[0].block
    combat_cards.pop(0)
    player_mod = "Normal"
    player_mod_message = get_mod_message(player_mod)

    kos_atk = get_attack_value()
    kos_blk = get_blk_value()
    kos_mod = get_mod_value()
    kos_mod_message = get_mod_message(kos_mod)

    player_hp, kos_hp = clash(player_atk, player_blk, player_hp, kos_atk, kos_blk, kos_hp)
    if player_atk == kos_blk and kos_mod == "Wolf" or kos_mod == "Star":
        player_hp -= 1

    print(f'\n== CLASH {i} ==')
    print(f'\nPlayer atk: {player_atk}')
    print(f'Player blk: {player_blk}')
    print(f'Player mod: {player_mod}')
    print(f'Player mod msg: {player_mod_message}')
    print(f'\nKoS atk: {kos_atk}')
    print(f'KoS blk: {kos_blk}')
    print(f'KoS mod: {kos_mod}')
    print(f'Kos mod msg: {kos_mod_message}')
    print(f'\nPlayer HP: {player_hp}')
    print(f'Kos HP: {kos_hp}')

    if len(combat_cards) == 0:
        break

    i += 1







#Player selects card from hand
#Player selects mod on card, declares it before laying card down
#Player hits 'enter,' which officially 'submits' their selection, and also rolls the 3 dice for the NPC
#Program calculates results and deducts HP if necessary.
#Repeat until someone is defeated (all HP lost)