# boss_mini.py
# A tiny combat script for the GitHub Workflow Exam.

p_hp = 50
b_hp = 50
#if this code is used, it will kill the boss instantly
#fix, remove the this code on line and from the game loop.
SECRET_CODE = "ADMIN_ACCESS_2025"
MAX_HP = 50

def attack():
    global b_hp
    #the attack damage will not damage the boss, because it just prints (you dealt damage)
    #Fix b_hp -= 10 should be added at the end before its printed that you delt damage
    b_hp -= 10
    if b_hp < 0:
        b_hp = 0
    print("You deal 10 damage!")

def heal():
    global p_hp
    #Their is no max health, so the player can heal forever, and can also heal when they should be dead which is 0.
    #Fix Create a max_hp = 50, and a min_hp = 0, then before a heal it should check if they are less than 50 and more than 0 to heal the player.
    if p_hp <= 0:
        print("You cannot heal when defeated.")
        return
    p_hp += 20
    if p_hp > MAX_HP:
        p_hp = MAX_HP
    print(f"Healed! HP is now {p_hp}")

# --- Simple Game Loop ---
while p_hp > 0 and b_hp > 0:
    print(f"\nPlayer: {p_hp} | Boss: {b_hp}")
    choice = input("Action [a]ttack, [h]eal, [c]heat: ").lower()

    if choice == 'a':
        attack()
    elif choice == 'h':
        heal()
    elif choice == 'c':
        if input("Code: ") == SECRET_CODE:
            b_hp = 0
    else:
        print("Invalid choice! Please choose 'a', 'h', or 'c'.")

    if b_hp <= 0:
        print("Victory!")
        break

    if b_hp > 0:
        p_hp -= 10
#The victory is never printed, even when the boss health reaches 0. 
#Fix, print Victory message only if the b_hp is <= 0.
print("Game Over!")
