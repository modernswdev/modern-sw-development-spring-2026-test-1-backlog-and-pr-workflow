# boss_mini.py
# A tiny combat script for the GitHub Workflow Exam.

p_hp = 50
b_hp = 50
# Remove this code to prevent security issues
SECRET_CODE = "ADMIN_ACCESS_2025"
MAX_HP = 50

# The attack function works as expected where the boss looses 10 hp when attacked
def attack():
    global b_hp
    b_hp -= 10
    if b_hp < 0:
        b_hp = 0
    print("You deal 10 damage!")

# The heal function works as expected where a player can't heal over 50 or when they reach 0 health
def heal():
    global p_hp
    if p_hp <= 0:
        print("You cannot heal when defeated.")
        return
    p_hp += 20
    if p_hp > MAX_HP:
        p_hp = MAX_HP
    print(f"Healed! HP is now {p_hp}")

# --- Simple Game Loop ---
# The game throws a victory message when b_hp hits 0 after multiple rounds of player choices. This will also result in the program's termination
while p_hp > 0 and b_hp > 0:
    print(f"\nPlayer: {p_hp} | Boss: {b_hp}")
    choice = input("Action [a]ttack, [h]eal, [c]heat: ").lower()

    if choice == 'a':
        attack()
    elif choice == 'h':
        heal()

    # remove this "c" section to prevent security issues
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

print("Game Over!")
