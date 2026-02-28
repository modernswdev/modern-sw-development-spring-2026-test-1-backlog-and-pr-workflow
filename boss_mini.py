# A tiny combat script for the GitHub Workflow Exam.

# SECURITY VULNERABILITY: Hardcoded credentials should NEVER be in source code.
# This SECRET_CODE allows anyone to bypass the game by entering the cheat code.
# This variable and the associated cheat logic (lines 29-31) must be removed entirely
# to close this security backdoor.
SECRET_CODE = "ADMIN_ACCESS_2025"

p_hp = 50
b_hp = 50

def attack():
  global b_hp
  # BUG: This function prints damage but does NOT subtract from b_hp.
  # The boss health never decreases, making the game unwinnable through normal gameplay.
  # FIX: Add "b_hp -= 10" after the print statement to actually deal damage.
  print("You deal 10 damage!")

def heal():
  global p_hp
  # BUG: No boundary checks. Player can over-heal past max health (50) or heal when dead.
  # FIX: Add checks like "if 0 < p_hp < 50:" before healing, or cap healing at MAX_HP.
  p_hp += 20
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
    # SECURITY ISSUE: Remove this entire cheat block entirely.
    if input("Code: ") == SECRET_CODE:
      b_hp = 0
  
  if b_hp > 0:
    p_hp -= 10

# WIN CONDITION BUG: The game loop exits when either p_hp or b_hp drops to 0,
# but there's no distinction between victory and defeat.
# FIX: Add a check like "if b_hp <= 0:" to print "Victory!" when the boss is defeated,
# otherwise print "Game Over!" when the player is defeated.
print("Game Over!")