player_hp = 5
combat_stones = 2
rep_rank = 1

#stats
pow = 0
agi = 0
sta = 0
chi = 0
wit = 0

towns = [Leap-Creek, Blackstone, Firefen, Undervale, Pouch]

print("You are a student of kung fu in the Valley of the Star. You were born and raised in one of the five towns of the valley. They are: Leap-Creek, Blackstone, Pouch, Bloodfen, and Undervale.")

def choose_pc(town):
    town = int(input("Choose a town from this list to be your home: "))
    for town in enumerate(towns):
        town_number = towns.index + 1
        print(f'{town_number}: {town}')


choose_pc(3)

#chosen_origin = input("Choose which town is your home:")