player_hp = 5
combat_stones = 2
rep_rank = 1

#stats
pow = 0
agi = 0
sta = 0
chi = 0
wit = 0

towns = {
    1: "Leap-Creek",
    2: "Blackstone",
    3: "Firefen",
    4: "Undervale",
    5: "Pouch"
}

print("You are a student of kung fu in the Valley of the Star. You were born and raised in one of the five towns of the valley.\n")

def choose_player_character():
    for key, value in towns.items():
        print(f'{key}. {value}')
    chosen_town = int(input("Choose a town from this list to be your home: "))
    return towns[chosen_town]

chosen_town = choose_player_character()
print(f'You chose {chosen_town}.')
