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
    print("You are defeated! Cannot heal.")
  elif p_hp >= MAX_HP:
    print("Already at full health!")
  else:
    p_hp += 20
    if p_hp > MAX_HP:
      p_hp = MAX_HP
    print(f"Healed! HP is now {p_hp}")

# --- Simple Game Loop ---
while p_hp > 0 and b_hp > 0:
  print(f"\nPlayer: {p_hp} | Boss: {b_hp}")
  choice = input("Action [a]ttack, [h]eal: ").lower()

  if choice == 'a':
    attack()
  elif choice == 'h':
    heal()
  
  if b_hp > 0:
    p_hp -= 10

if b_hp <= 0:
  print("Victory! You defeated the boss!")
else:
  print("Game Over! You were defeated.")