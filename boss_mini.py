# boss_mini.py
# A tiny combat script for the GitHub Workflow Exam.

p_hp = 50
b_hp = 50
SECRET_CODE = "ADMIN_ACCESS_2025" # This line of code failed the security audit. The variable and cheat logic must be removed to close the backdoor vulnerability.
MAX_HP = 50

def attack():
    global b_hp
    b_hp -= 10 # This line of code in the attack function now has the correct math that subtracts 10 health from the Boss.
    if b_hp < 0:
        b_hp = 0
    print("You deal 10 damage!")

def heal():
    global p_hp
    if p_hp <= 0: # This line of code in the heal function was corrected to prevent healing when health is 0 or less.
        print("You cannot heal when defeated.")
        return
    p_hp += 20 # This line of code in the heal function was corrected to prevent over-healing (past MAX_HP or over 50)
    if p_hp > MAX_HP:
        p_hp = MAX_HP # This line of code in the heal function was corrected to prevent over-healing (past MAX_HP or over 50)
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
        break # This if statement was corrected to trigger the Victory message and terminate the loop when Boss health reaches 0 or less.

    if b_hp > 0:
        p_hp -= 10

print("Game Over!")
