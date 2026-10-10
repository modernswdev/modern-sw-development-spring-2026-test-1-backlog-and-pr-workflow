# boss_mini.py
# A tiny combat script for the GitHub Workflow Exam.

p_hp = 50
b_hp = 50
MAX_HP = 50

def attack():
    global b_hp
    b_hp -= 10
    print("You deal 10 damage!")

def heal():
    global p_hp
    if p_hp <= 0:
        print("You cannot heal when defeated.")
        return
     if p_hp >= MAX_HP:
    print("HP is full!")
    return

# --- Simple Game Loop ---

while p_hp > 0 and b_hp > 0:
  print(f"\nPlayer: {p_hp} | Boss: {b_hp}")
  choice = input("Action [a]ttack, [h]eal, [c]heat: ").lower()

  if choice == 'a':
    attack()
  elif choice == 'h':
    heal()

  if b_hp > 0:
    p_hp -= 10


if b_hp <= 0:
  print("Victory!")
else:
  print("Game Over!")
