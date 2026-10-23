# boss_mini.py
# A tiny combat script for the GitHub Workflow Exam.

p_hp = 50
b_hp = 50
# SECURITY BUG: The hardcoded secret exposes the cheat code to anyone
# who can read the source. Remove this variable and the cheat logic.
SECRET_CODE = "ADMIN_ACCESS_2025"
MAX_HP = 50

# BUG: The boss's health never decreases when attacked.
# FIX: Add b_hp -= 10 so each attack removes 10 boss HP.
def attack():
    global b_hp
    b_hp -= 10
    if b_hp < 0:
        b_hp = 0
    print("You deal 10 damage!")

# BUG: Healing can raise HP above 50 or work when HP is 0 or less.
# FIX: Check that p_hp > 0 and cap the result at 50 HP.
def heal():
    global p_hp
    if p_hp <= 0:
        print("You cannot heal when defeated.")
        return
    p_hp += 20
    if p_hp > MAX_HP:
        p_hp = MAX_HP
    print(f"Healed! HP is now {p_hp}")

# BUG: The game needs to announce victory when the boss is defeated.
# FIX: After the loop, print Victory! if b_hp <= 0; otherwise Game Over!
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

print("Game Over!")
