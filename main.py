import combat_card
from npc_combat import get_npc_clash_values, get_mod_message, clash
from character import Character


'''
●   SELECTION PHASE - Combatants select 1 card from hand and place it on the table face down. Each player will then announce how they will play that card by stating the number associated to the Special they intend to use on that particular card.
●  	REVEAL STEP - Both players flip card face up, and immediately place a stone on top if applicable.
●  	REACTION PHASE - Each player may make one reaction, if Specials or Techniques allow for it. This phase is also where Non-Player Adversaries will apply the effects of the White Die, unless otherwise noted. A player who has chosen “stumble” can change his or her special selection during this phase.
●  	CALCULATION STEP - Determine what happened in this clash. Subtract applicable HP.
●  	ACTIVATION PHASE - This is when you activate technique cards that will be played in the next clash. No more than 1 Technique per player may be played in a single clash.
'''

def print_card_special_options():
    print(f'\nCard Specials:')
    for key, value in combat_card.card_special_options.items():
        print(f'{key}. {value}')


print("====== START ======\n")

player = Character()
npc = Character()
round_one_hand, round_two_hand = combat_card.get_two_hands()

print(f'Player HP: {player.hp}')
print(f'NPC HP: {npc.hp}')

clash_number = 0
while player.is_alive and npc.is_alive:
    if len(round_two_hand) == 0:
        print("\nIt's a draw. You are evenly matched.")
        break
    # TODO: we really shouldn't need to determine what the current hand is each iteration
    # replace this with A Better Way™
    current_hand = combat_card.get_current_hand(round_one_hand, round_two_hand)
    print("\nAvailable Player Combat Cards:")
    for index, card in enumerate(current_hand):
        card_number = index + 1
        print(f'{card_number}: {card}')
    cards_remaining_in_hand = len(current_hand)
    card_auto_chosen = False

    if cards_remaining_in_hand == 1:
        card_auto_chosen = True
        selected_card_number = 1
        print(f'Auto-choosing card # {selected_card_number}')
        print_card_special_options()
        selected_card_special = combat_card.get_selected_card_special()
    else:
        selected_card_number = combat_card.get_selected_card(cards_remaining_in_hand)
        if selected_card_number not in [x for x in range(1, cards_remaining_in_hand + 1)]:
            print(f'Invalid choice. Please choose a number [1-{cards_remaining_in_hand}]: ')
            continue
        print_card_special_options()
        selected_card_special = combat_card.get_selected_card_special()

    if not card_auto_chosen:
        print(f'You chose card # {selected_card_number}')
    selected_card_index = selected_card_number - 1
    selected_card = current_hand[selected_card_index]
    player_mod_message = combat_card.get_player_mod_message()
    print(f'...which is this card: {selected_card}')
    print(f'Selected card Special: {selected_card_special}')

    player_atk = selected_card.attack
    player_blk = selected_card.block
    current_hand.pop(selected_card_index)

    npc_atk, npc_blk, npc_mod = get_npc_clash_values()
    npc_mod_message = get_mod_message(npc_mod)

    clash(player_atk, player_blk, player, npc_atk, npc_blk, npc_mod, npc)

    clash_number += 1
    print(f'\n== CLASH {clash_number} ==')
    print(f'\nPlayer atk: {player_atk}')
    print(f'Player blk: {player_blk}')
    print(f'Player mod: {selected_card_special} <!! Player mod is not yet factored into clashes. !!>')
    print(f'Player mod msg: {player_mod_message}')
    print(f'\nNPC atk: {npc_atk}')
    print(f'NPC blk: {npc_blk}')
    print(f'NPC mod: {npc_mod}')
    print(f'NPC mod msg: {npc_mod_message}')
    print(f'\nPlayer HP: {player.hp}')
    print(f'NPC HP: {npc.hp}')

print("\n===== GAME OVER =====")
if not player.is_alive:
    if npc.is_alive:
        print("\nYou are injured, and you have lost one rank in reputation.")
    if not npc.is_alive:
        print("\nIt's a draw. You are evenly matched.")
elif not npc.is_alive:
    print("\nYou won! Gain one reputation rank, and collect your reward.")
