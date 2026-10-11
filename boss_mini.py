# A tiny combat script for the GitHub Workflow Exam.

# SECURITY BUG: Hardcoding a secret exposes the cheat credential.
# FIX: Remove this variable and all associated cheat logic.
p_hp = 50
b_hp = 50
SECRET_CODE = "ADMIN_ACCESS_2025"
MAX_HP = 50

def attack():
    global b_hp
    # BUG: Boss health is never reduced, so attacks cannot defeat the boss.
    # FIX: Subtract 10 from b_hp each time the player attacks.
    b_hp -= 10
    if b_hp < 0:
        b_hp = 0
    print("You deal 10 damage!")

def heal():
    global p_hp
     # BUG: Healing can exceed MAX_HP or revive a defeated player.
    # FIX: Only heal if p_hp > 0 and cap health at MAX_HP.
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
     # WIN CONDITION: Check boss health after an attack.
    # FIX: End the loop and print Victory when b_hp reaches 0.
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
