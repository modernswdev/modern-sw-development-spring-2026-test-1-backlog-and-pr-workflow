# boss_mini.py
# A tiny combat script for the GitHub Workflow Exam.


# SECURITY ISSUE:
# The following hardcoded credential creates a backdoor vulnerability.
# It allows players to bypass normal gameplay. It has been commented out
# to prevent unauthorized access while keeping it visible for audit purposes.

# SECRET_CODE = "ADMIN_ACCESS_2025"


p_hp = 50
b_hp = 50


# ATTACK LOGIC FIX:
# The original version did not subtract damage from the boss.
# Added logic to reduce boss HP by 10 each time attack() is called.
def attack():
    global b_hp
    b_hp -= 10
    print("You deal 10 damage!")


# HEALING GUARDRAILS:
# Added checks to prevent healing past 50 HP
# and to prevent healing when player HP is 0 or below.
def heal():
    global p_hp

    if p_hp <= 0:
        print("You can't heal when you're down!")
        return

    if p_hp >= 50:
        print("HP is already full!")
        return

    p_hp += 20

    if p_hp > 50:
        p_hp = 50

    print(f"Healed! HP is now {p_hp}")


# --- Simple Game Loop ---
# WIN CONDITION:
# Added logic to trigger a Victory message and end the loop
# when the boss's HP reaches 0.
#
# DEFEAT CONDITION:
# Added logic to trigger a defeat message and end the loop
# when the player's HP reaches 0.

while p_hp > 0 and b_hp > 0:
    print(f"\nPlayer: {p_hp} | Boss: {b_hp}")
    choice = input("Action [a]ttack, [h]eal: ").lower()

    if choice == 'a':
        attack()
    elif choice == 'h':
        heal()
    # Cheat logic commented out to remove backdoor vulnerability
    # elif choice == 'c':
    #     if input("Code: ") == SECRET_CODE:
    #         b_hp = 0
    else:
        print("Invalid choice! Please choose 'a' or 'h'.")

    # Boss attacks back if still alive
    if b_hp > 0:
        p_hp -= 10

    if b_hp <= 0:
        print("Victory! You defeated the boss!")
        break

    if p_hp <= 0:
        print("You have been defeated!")
        break


print("Game Over!")
