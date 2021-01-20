player_health = 0
stamina = 0
boss_health = 1000

done = False 

print("******Game******")

print("Choose your class")

player_class = int(input("Enter 1 for Mage, Enter 2 for Brawler, Enter 3 for Rogue: "))

#Mage Skills
drain_touch = 0
heal = 0
vine_whip = 0
ice_wall = 0
explosion = 0

#Warrior Skills
sasageyo = 0
smack = 0
muda_barrage = 0
block = 0
za_warudo = 0

#Rogue Skills
steal = 0
quick_cut = 0
counter = 0
dash = 0
bladestorm = 0

#player loop mage
while player_class == 1:
  player_health = 0
  stamina = 0
  drain_touch = drain_touch + 1
  heal = heal + 1
  vine_whip = vine_whip + 1
  ice_wall = ice_wall + 1
  explosion = explosion + 1
  player_class = player_class - 1
  turn_count = 1

  #
  while turn_count == 1:
    #takes skill number as input
    if explosion > 10:
      drain_touch = drain_touch + 1
      print("Skill 1: Drain Touch")
      heal = heal + 1
      print("Skill 2: Heal")
      vine_whip = vine_whip + 1
      print("Skill 3: Vine Whip")
      ice_wall = ice_wall + 1
      print("Skill 4: Ice Wall")
      explosion = explosion + 1
      print("Skill 5: EXPLOSION!!!!!!!!!!!")
      player_choice_explosion = int(input("Enter the Skill Number: "))

      #based on skill number it will deal take away a certain amount of boss_health or inflict a status effect. After a skill is played the turn_count will go to zero and the boss loop will play
      if player_choice_explosion == 1:
        print("Boss Health: "+ str(boss_health))
      elif player_choice_explosion == 2:
        print("Boss Health: "+ str(boss_health))
      elif player_choice_explosion == 3:
        print("Boss Health: "+ str(boss_health))
      elif player_choice_explosion == 4:
        print("Boss Health: "+ str(boss_health))
      elif player_choice_explosion == 5:
        print("Boss Health: "+ str(boss_health))
      else:
        print("Invalid")

    #takes skill number as input
    else:
      drain_touch = drain_touch + 1
      print("Skill 1: Drain Touch")
      heal = heal + 1
      print("Skill 2: Heal")
      vine_whip = vine_whip + 1
      print("Skill 3: Vine Whip")
      ice_wall = ice_wall + 1
      print("Skill 4: Ice Wall")
      explosion = explosion + 1
      player_choice = int(input("Enter the Skill Number: "))

      #based on skill number it will deal take away a certain amount of boss_health or inflict a status effect. After a skill is played the turn_count will go to zero and the boss loop will play      #based on skill number it will deal take away a certain amount of boss_health or inflict a status effect. After a skill is played the turn_count will go to zero and the boss loop will play
      if player_choice == 1:
        print("Boss Health: "+ str(boss_health))
      elif player_choice == 2:
        print("Boss Health: "+ str(boss_health))
      elif player_choice == 3:
        print("Boss Health: "+ str(boss_health))
      elif player_choice == 4:
        print("Boss Health: "+ str(boss_health))
      else:
        print("Invalid")


#player loop brawler
while player_class == 2:
  player_health = 0
  stamina = 0
  sasageyo + sasageyo + 1
  smack + smack + 1
  muda_barrage + muda_barrage + 1
  block + block + 1
  za_warudo + za_warudo + 1
  player_class = player_class - 2
  turn_count = 1

  #if turn_count = 1 then player loop starts, if turn_count = 0 then boss loop starts
  while turn_count == 1:

    #takes skill number as input 
    if za_warudo == 10:
      sasageyo + sasageyo + 1
      print("Skill 1: Sasageyo!")
      smack + smack + 1
      print("Skill 2: Smack")
      muda_barrage + muda_barrage + 1
      print("Skill 3: Muda Barrage")
      block + block + 1
      print("Skill 4: Block")
      za_warudo + za_warudo + 1
      print("Skill 5: ZA WARUDO")
      player_choice_za_warudo = int(input("Enter the Skill Number: "))

      #based on skill number it will deal take away a certain amount of boss_health or inflict a status effect. After a skill is played the turn_count will go to zero and the boss loop will play
      if player_choice_za_warudo == 1:
        print("Boss Health: "+ str(boss_health))
      elif player_choice_za_warudo == 2:
        print("Boss Health: "+ str(boss_health))
      elif player_choice_za_warudo == 3:
        print("Boss Health: "+ str(boss_health))
      elif player_choice_za_warudo == 4:
        print("Boss Health: "+ str(boss_health))
      elif player_choice_za_warudo == 5:
        print("Boss Health: "+ str(boss_health))
      else:
        print("Invalid")

    #takes skill number as input    
    else: 
      sasageyo + sasageyo + 1
      print("Skill 1: Sasageyo!")
      smack + smack + 1
      print("Skill 2: Smack")
      muda_barrage + muda_barrage + 1
      print("Skill 3: Muda Barrage")
      block + block + 1
      print("Skill 4: Block")
      za_warudo + za_warudo + 1
      player_choice = int(input("Enter the Skill Number: "))

      #based on skill number it will deal take away a certain amount of boss_health or inflict a status effect. After a skill is played the turn_count will go to zero and the boss loop will play
      if player_choice == 1:
        print("Boss Health: "+ str(boss_health))
      elif player_choice == 2:
        print("Boss Health: "+ str(boss_health))
      elif player_choice == 3:
        print("Boss Health: "+ str(boss_health))
      elif player_choice == 4:
        print("Boss Health: "+ str(boss_health))
      else:
        print("Invalid")

#player loop rogue
while player_class == 3:
  player_health = 0
  stamina = 0
  steal = steal + 1
  quick_cut = quick_cut + 1
  counter = counter + 1
  dash = dash + 1
  bladestorm = bladestorm + 1
  player_class = player_class - 3
  turn_count = 1

  while turn_count == 1:

    #takes skill number as input
    if bladestorm == 10:
      steal = steal + 1
      print("Skill 1: Steal")
      quick_cut = quick_cut + 1
      print("Skill 2: Quick Cut")
      counter = counter + 1
      print("Skill 3: Counter")
      dash = dash + 1
      print("Skill 4: Dash")
      bladestorm = bladestorm + 1
      print("Skill 5: Bladestorm")
      player_choice_bladestorm = int(input("Enter the Skill Number: "))

      #based on skill number it will deal take away a certain amount of boss_health or inflict a status effect. After a skill is played the turn_count will go to zero and the boss loop will play
      if player_choice_bladestorm == 1:
        print("Boss Health: "+ str(boss_health))
      elif player_choice_bladestorm == 2:
        print("Boss Health: "+ str(boss_health))
      elif player_choice_bladestorm == 3:
        print("Boss Health: "+ str(boss_health))
      elif player_choice_bladestorm == 4:
        print("Boss Health: "+ str(boss_health))
      elif player_choice_bladestorm == 5:
        print("Boss Health: "+ str(boss_health))
      else:
        print("Invalid")

    #takes skill number as input
    else: 
      steal = steal + 1
      print("Skill 1: Steal")
      quick_cut = quick_cut + 1
      print("Skill 2: Quick Cut")
      counter = counter + 1
      print("Skill 3: Counter")
      dash = dash + 1
      print("Skill 4: Dash")
      bladestorm = bladestorm + 1
      player_choice = int(input("Enter the Skill Number: "))

      #based on skill number it will deal take away a certain amount of boss_health or inflict a status effect. After a skill is played the turn_count will go to zero and the boss loop will play
      if player_choice == 1 and steal >= 1:
        print("Boss Health: "+ str(boss_health))
      elif player_choice == 2 and quick_cut >= 1:
        print("Boss Health: "+ str(boss_health))
      elif player_choice == 3 and counter >= 1:
        print("Boss Health: "+ str(boss_health))
      elif player_choice == 4 and dash >= 1:
        print("Boss Health: "+ str(boss_health))
      else:
        print("Invalid")


if drain_touch >= 1:
  print("Skill 1: Drain Touch")
elif heal >= 1:
  print("Skill 2: Heal")
elif vine_whip >= 1:
  print("Skill 3: Vine Whip")
elif ice_wall >= 1:
  print("Skill 4: Ice Wall")
elif explosion >= 1:
  print("Skill 5: EXPLOSION!!!!!!!!!!!")

if sasageyo >= 1:
  print("Skill 1: Sasageyo!")
elif smack >= 1:
  print("Skill 2: Smack")
elif muda_barrage >= 1:
  print("Skill 3: Muda Barrage")
elif block >= 1:
  print("Skill 4: Block")
elif za_warudo >= 1:
  print("Skill 5: ZA WARUDO")

if steal >= 1:
  print("Skill 1: Steal")
elif quick_cut >= 1:
  print("Skill 2: Quick Cut")
elif counter >= 1:
  print("Skill 3: Counter")
elif dash >= 1:
  print("Skill 4: Dash")
elif bladestorm >= 1:
  print("Skill 5: Bladestorm")



#when the boss health or your health reaches 0 the game ends
while done == False:
  if boss_health == 0:
    print("You Won!")
    done = True
  elif player_health == 0:
    print("Game Over")
    done = True


