# boss_mini.py
# A tiny combat script for the GitHub Workflow Exam.

p_hp = 50
b_hp = 50
# SECURITY BUG: This hardcoded secret code creates a backdoor that
# allows unauthorized access to the cheat functionality.
# FIX: Remove SECRET_CODE and the associated cheat logic.
SECRET_CODE = "ADMIN_ACCESS_2025"
MAX_HP = 50

# BUG: The attack logic must subtract 10 health from the Boss (b_hp).
# FIX: Add b_hp -= 10 so damage is actually applied to the Boss.
def attack():
    global b_hp
    b_hp -= 10
    if b_hp < 0:
        b_hp = 0
    print("You deal 10 damage!")

# BUG: Healing needs boundary checks so the player cannot heal when
    # HP is 0 or less and cannot increase above the maximum of 50 HP.
    # FIX: Check for p_hp <= 0 and cap healing at MAX_HP.
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
# WIN CONDITION: When the Boss's HP reaches 0 or less, the game should
# print "Victory!" and terminate the game loop.
    if b_hp <= 0:
        print("Victory!")
        break

    if b_hp > 0:
        p_hp -= 10

print("Game Over!")
