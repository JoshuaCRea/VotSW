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

combat_cards = get_combat_cards()
random.shuffle(combat_cards)
round_one_hand = combat_cards[0:5]
round_two_hand = combat_cards[5:10]

i = 0
while player_hp > 0 and kos_hp > 0:
    current_hand = round_one_hand
    if len(round_one_hand) == 0:
        current_hand = round_two_hand
    print("\nAvailable Player Combat Cards:")
    i = 1
    for card in current_hand:
        print(f'{i}: {card}')
        i += 1

    selected_card_number = int(input(f'\nPlayer, please select a card [1-{len(current_hand)}]: '))
    print(f'You chose card # {selected_card_number}')
    selected_card_index = selected_card_number - 1
    selected_card = current_hand[selected_card_index]
    print(f'...which is this card: {selected_card}')

    player_atk = selected_card.attack
    player_blk = selected_card.block
    current_hand.pop(selected_card_index)

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