import random

#note: at turn 10 an ultimate skill will be available 

boss_health = 1500
turn_count = 1
done = False 

print("******Attack on Virus******")

print("Tips:")
print("- REMEMBER THERE ARE COOLDOWNS")
print("Explore the different classes, some mechanics I added include damage based on health lost, stun,etc.")
print("- Block, stun, and extremely high damage skills have a cooldown of 3 or more turns so don't use them at the start of the game and don't go spamming them...")
print("- At turn 10 or by using specific skills an ultimate skill will be available. It will appear in the skill list.")
print("- USE SKILL 1 FOR A FEW TURNS UNTIL THE REST OF THE COOLDOWNS FOR SKILLS 2-5 ARE GONE!!!!!")
print("- It's a fast moving text game make to read it all to avoid confusion")

print("CHOOSE YOUR CLASS")
player_class = int(input("Enter 1 for Mage, Enter 2 for Brawler, Enter 3 for Rogue: "))


#Mage Skills
drain_touch = 1
heal = 1
vine_whip = 1
ice_wall = 1
explosion = 1

#Warrior Skills
sasageyo = 1
smack = 1
muda_barrage = 1
block = 1
za_warudo = 1

#Rogue Skills
steal = 1
quick_cut = 1
counter = 1
dash = 1
bladestorm = 1



#player loop mage
if player_class == 1:
  player_health = 700
  player_class = player_class - 1

  while done == False:


    #if turn_count = 1 then player loop starts, if turn_count = 0 then boss loop starts
    while turn_count >= 1:
      #takes skill number as input
      if explosion > 10:
        drain_touch = drain_touch + 1
        print("Skill 1: Drain Touch")
        print("Skill 2: Heal")
        print("Skill 3: Vine Whip")
        print("Skill 4: Ice Wall")
        print("Skill 5: EXPLOSION!!!!!!!!!!!")
        player_choice_explosion = int(input("Enter the Skill Number: "))



        #based on skill number it will deal take away a certain amount of boss_health or inflict a status effect. After a skill is played the turn_count will go to zero and the boss loop will play
        if player_choice_explosion == 1 and drain_touch >= 1:
          boss_health = boss_health - 25
          player_health = player_health + 25
          print("You drained the virus of some health")
          print("You healed 25 healed and dealt 25 damage") 
          print("Boss Health: "+ str(boss_health))
          print("Player Health: "+ str(player_health))
          drain_touch = drain_touch - drain_touch
          turn_count = turn_count - 1



        elif player_choice_explosion == 2 and heal >= 3:
          print("You healed 50 health!!!")
          player_health = player_health + 50
          print("Player Health: "+ str(player_health))
          heal = heal - heal
          turn_count = turn_count - 1



        elif player_choice_explosion == 3 and vine_whip >= 4:
          print("You snared the virus.")
          print("You dealt 50 damage and got an extra turn")
          boss_health = boss_health - 50
          print("Boss Health: "+ str(boss_health))
          vine_whip = vine_whip - vine_whip
          turn_count = turn_count + 1



        elif player_choice_explosion == 4 and ice_wall >= 5:
          print("You block the next two attacks and your turn is repeated twice")
          print("Use these turns wisely the wall will melt soon")
          print("Boss Health: "+ str(boss_health))
          ice_wall = ice_wall - ice_wall
          turn_count = turn_count + 2




        elif player_choice_explosion == 5 and explosion >= 10:
          print("EXPLOSIONNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
          print("You dealt 500 DAMAGE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
          print("Oh no you are extremely tired")
          print("You lose FIVE turns!!!!!!!!")
          boss_health = boss_health - 500
          print("Boss Health: "+ str(boss_health))
          turn_count = turn_count - 5


        else:
          print("You might have put an invalid number")
          print("If you are on skill cooldown STOP SPAMMING THE SAME SKILLS THERE ARE COOLDOWNS")
          print("You did zero damage and are on a turn cooldown")
          turn_count = turn_count - 3


      #takes skill number as input
      else:
        print("Skill 1: Drain Touch")
        print("Skill 2: Heal")
        print("Skill 3: Vine Whip")
        print("Skill 4: Ice Wall")
        player_choice = int(input("Enter the Skill Number: "))


        #based on skill number it will deal take away a certain amount of boss_health or inflict a status effect. After a skill is played the turn_count will go to zero and the boss loop will play
        if player_choice == 1 and drain_touch >= 1:
          boss_health = boss_health - 25
          player_health = player_health + 25
          print("You drained the virus of some health")
          print("You healed 25 healed and dealt 25 damage") 
          print("Boss Health: "+ str(boss_health))
          print("Player Health: "+ str(player_health))
          drain_touch = drain_touch - drain_touch
          turn_count = turn_count - 1



        elif player_choice == 2 and heal >= 3:
          print("You healed 50 health!!!")
          player_health = player_health + 50
          print("Player Health: "+ str(player_health))
          heal = heal - heal
          turn_count = turn_count - 1



        elif player_choice == 3 and vine_whip >= 4:
          print("You snared the virus.")
          print("You dealt 50 damage and got an extra turn")
          boss_health = boss_health - 50
          print("Boss Health: "+ str(boss_health))
          vine_whip = vine_whip - vine_whip
          turn_count = turn_count + 1



        elif player_choice == 4 and ice_wall >= 5:
          print("You block the next two attacks and your turn is repeated twice")
          print("Use these turns wisely the wall will melt soon")
          print("Boss Health: "+ str(boss_health))
          ice_wall = ice_wall - ice_wall
          turn_count = turn_count + 2



        else:
          print("You might have put an invalid number")
          print("If you are on skill cooldown STOP SPAMMING THE SAME SKILLS THERE ARE COOLDOWNS")
          print("You did zero damage and are on a turn cooldown")
          turn_count = turn_count - 3



    
    #The boss loop will randomly choose a skill and it will carry out the skill. After it will return the turn_count to 1 and the player loop will begin
    while turn_count <= 0:

      #Reduce the skill cooldown to make the skills usable
      drain_touch = drain_touch + 1
      heal = heal + 1
      vine_whip = vine_whip + 1
      ice_wall = ice_wall + 1
      explosion = explosion + 1

      #picks random skill
      boss_skill = random.randint(1,5)

      if boss_skill == 1:
        print("The virus used worm and is eating at your files")
        player_health = player_health - 25
        for i in range(25):
          print("1 damage")
        print("Player Health: "+ str(player_health))
        turn_count = turn_count + 1



      elif boss_skill == 2:
        print("The virus used Trojan and is taking over your computer")
        print("Your information isn't safe anymore!!!")
        player_health = player_health - 50
        print("50 DAMAGE")
        print("Player Health: "+ str(player_health))
        turn_count = turn_count + 1



      elif boss_skill == 3:
        print("The virus used Ransomware and is forcing you pay for access to your files")
        print("You're forced to pay!!!")
        explosion = explosion - 3
        print("Your ultimate skill cooldown is increased by 3 turns :(")
        print("Player Health: "+ str(player_health))
        turn_count = turn_count + 1



      elif boss_skill == 4:
        print("The virus used adware and is collecting your information")
        print("Ads are being spammed on your screen!!!")
        for i in range(10):
          print("BRUH")
        player_health = player_health - 10
        print("10 damage")
        print("Player Health: "+ str(player_health))
        turn_count = turn_count + 1



      elif boss_skill == 5:
        print("The virus used Spyware and predicts your next two attacks")
        print("You lose two turns!!!")
        turn_count = turn_count - 2
        print("Player Health: "+ str(player_health))
        turn_count = turn_count + 1
    

    #when the boss health or your health reaches 0 the game ends
    if boss_health <= 0:
      print("You Won!")
      done = True
    elif player_health <= 0:
      print("Game Over!!!!!!!!!!!!!!!!!")
      done = True

  

#player loop brawler
elif player_class == 2:
  player_health = 650
  player_class = player_class - 2

  while done == False:

    #if turn_count = 1 then player loop starts, if turn_count = 0 then boss loop starts
    while turn_count >= 1:

      #takes skill number as input 
      if za_warudo >= 10:
        print("Skill 1: Sasageyo!")
        print("Skill 2: Smack")
        print("Skill 3: Muda Barrage")
        print("Skill 4: Block")
        print("Skill 5: ZA WARUDO")
        player_choice_za_warudo = int(input("Enter the Skill Number: "))


        #based on skill number it will deal take away a certain amount of boss_health or inflict a status effect. After a skill is played the turn_count will go to zero and the boss loop will play.
        if player_choice_za_warudo == 1 and sasageyo >= 1:
          print("Sasageyo! sasageyo! shinzou wo sasageyo!")
          print("You gained reduced ultimate skill cooldown by one")
          za_warudo = za_warudo + 1
          print("Boss Health: "+ str(boss_health))
          sasageyo = sasageyo - sasageyo
          turn_count = turn_count - 1



        elif player_choice_za_warudo == 2 and smack >= 4:
          print("Ow that hurt!")
          print("You slapped the virus HARD!")
          print("You dealt 35 damage and got an extra turn")
          boss_health = boss_health - 50
          print("Boss Health: "+ str(boss_health))
          smack = smack - smack
          turn_count = turn_count + 1


        elif player_choice_za_warudo == 3 and muda_barrage >= 4:
          for i in range(50):
            print("MUDA!!!")
            print("2 DAMAGE")
          print("MUDAAAAAAAAA!!!!!!")
          print("50 DAMAGE!!!!!!!!!")
          print("You senselessly beat the virus with your fists while screaming")
          print("You did a total of 100 DAMAGE!!!!!!")
          boss_health = boss_health - 100
          print("Boss Health: "+ str(boss_health))
          muda_barrage = muda_barrage - muda_barrage
          turn_count = turn_count - 1



        elif player_choice_za_warudo == 4 and block >= 5:
          print("You block the next two attacks and your turn is repeated twice")
          print("Make the most of these two turns you can't withstand more than two attacks")
          print("Boss Health: "+ str(boss_health))
          block = block - block
          turn_count = turn_count + 2



        elif player_choice_za_warudo == 5 and za_warudo >= 10:
          print("ZA WARUDO TOKI WO TOMARE")
          print("You stopped time and gained 3 extra turns")
          print("Boss Health: "+ str(boss_health))
          za_warudo = za_warudo - za_warudo
          turn_count = turn_count + 3



        else:
          print("You might have put an invalid number")
          print("If you are on skill cooldown STOP SPAMMING THE SAME SKILLS THERE ARE COOLDOWNS")
          print("You did zero damage and are on a turn cooldown")
          turn_count = turn_count - 3


      #takes skill number as input    
      else: 
        print("Skill 1: Sasageyo!")
        print("Skill 2: Smack")
        print("Skill 3: Muda Barrage")
        print("Skill 4: Block")
        player_choice = int(input("Enter the Skill Number: "))


        #based on skill number it will deal take away a certain amount of boss_health or inflict a status effect. After a skill is played the turn_count will go to zero and the boss loop will play
        if player_choice == 1 and sasageyo >= 1:
          print("Sasageyo! sasageyo! shinzou wo sasageyo!")
          print("You gained reduced ultimate skill cooldown by one")
          za_warudo = za_warudo + 1
          print("Boss Health: "+ str(boss_health))
          turn_count = turn_count - 1


        elif player_choice == 2 and smack >= 4:
          print("Ow that hurt!")
          print("You slapped the virus HARD!")
          print("You dealt 35 damage and got an extra turn")
          boss_health = boss_health - 50
          print("Boss Health: "+ str(boss_health))
          smack = smack - smack
          turn_count = turn_count + 1


        elif player_choice == 3 and muda_barrage >= 4:
          for i in range(50):
            print("MUDA!!!")
            print("2 DAMAGE")
          print("MUDAAAAAAAAA!!!!!!")
          print("50 DAMAGE!!!!!!!!!")
          print("You senselessly beat the virus with your fists while screaming")
          print("You did a total of 100 DAMAGE!!!!!!")
          boss_health = boss_health - 100
          print("Boss Health: "+ str(boss_health))
          muda_barrage = muda_barrage - muda_barrage
          turn_count = turn_count - 1



        elif player_choice == 4 and block >= 5:
          print("You block the next two attacks and your turn is repeated twice")
          print("Make the most of these two turns you can't withstand more than two attacks")
          print("Boss Health: "+ str(boss_health))
          block = block - block
          turn_count = turn_count + 2


        else:
          print("You might have put an invalid number")
          print("If you are on skill cooldown STOP SPAMMING THE SAME SKILLS THERE ARE COOLDOWNS")
          print("You did zero damage and are on a turn cooldown")
          turn_count = turn_count - 3


    #The boss loop will randomly choose a skill and it will carry out the skill. After it will return the turn_count to 1 and the player loop will begin
    while turn_count <= 0:

      #Reduce the skill cooldown to make the skills usable
      sasageyo = sasageyo + 1
      smack = smack + 1
      muda_barrage = muda_barrage + 1
      block = block + 1
      za_warudo = za_warudo + 1


      #picks random skill
      boss_skill = random.randint(1,5)

      if boss_skill == 1:
        print("The virus used worm and is eating at your files")
        player_health = player_health - 25
        for i in range(25):
          print("1 damage")
        print("Player Health: "+ str(player_health))
        turn_count = turn_count + 1



      elif boss_skill == 2:
        print("The virus used Trojan and is taking over your computer")
        print("Your information isn't safe anymore!!!")
        player_health = player_health - 50
        print("50 DAMAGE")
        print("Player Health: "+ str(player_health))
        turn_count = turn_count + 1



      elif boss_skill == 3:
        print("The virus used Ransomware and is forcing you pay for access to your files")
        print("You're forced to pay!!!")
        explosion = explosion - 3
        print("Your ultimate skill cooldown is increased by 3 turns :(")
        print("Player Health: "+ str(player_health))
        turn_count = turn_count + 1



      elif boss_skill == 4:
        print("The virus used adware and is collecting your information")
        print("Ads are being spammed on your screen!!!")
        for i in range(10):
          print("BRUH")
        player_health = player_health - 10
        print("10 damage")
        print("Player Health: "+ str(player_health))
        turn_count = turn_count + 1



      elif boss_skill == 5:
        print("The virus used Spyware and predicts your next two attacks")
        print("You lose two turns!!!")
        turn_count = turn_count - 2
        print("Player Health: "+ str(player_health))
        turn_count = turn_count + 1

    


    #when the boss health or your health reaches 0 the game ends
    if boss_health <= 0:
      print("You Won!")
      done = True
    elif player_health <= 0:
      print("Game Over!!!!!!!!!!!!!!!!!")
      done = True
    


#player loop rogue
elif player_class == 3:
  player_health = 600
  player_class = player_class - 3

  while done == False:

    #if turn_count = 1 then player loop starts, if turn_count = 0 then boss loop starts
    while turn_count >= 1:

      #takes skill number as input
      if bladestorm >= 10:
        print("Skill 1: Steal")
        print("Skill 2: Quick Cut")
        print("Skill 3: Counter")
        print("Skill 4: Dash")
        print("Skill 5: Bladestorm")
        player_choice_bladestorm = int(input("Enter the Skill Number: "))


        #based on skill number it will deal take away a certain amount of boss_health or inflict a status effect. After a skill is played the turn_count will go to zero and the boss loop will play
        if player_choice_bladestorm == 1 and steal >= 1:
          print("STEAL!")
          print("You gained reduced ultimate skill cooldown by one")
          bladestorm = bladestorm + 1
          print("Boss Health: "+ str(boss_health))
          steal = steal - steal
          turn_count = turn_count - 1

          
        elif player_choice_bladestorm == 2 and quick_cut >= 4:
          print("You slashed the virus with extreme speed")
          print("You did 100 damage!!!")
          print("Boss Health: "+ str(boss_health))
          quick_cut = quick_cut - quick_cut
          turn_count = turn_count - 1



        elif player_choice_bladestorm == 3 and counter >= 4:
          print("You countered all of the virus's attacks")
          print("Health lost = Damage dealt")
          print("Boss Health: "+ str(boss_health))
          counter = counter - counter
          turn_count = turn_count - 1



        elif player_choice_bladestorm == 4 and dash >= 5:
          print("You dashed straight at the virus catching it off guard!")
          print("You got ahead of the virus and have gained 3 extra turns!")
          print("Boss Health: "+ str(boss_health))
          dash = dash - dash
          turn_count = turn_count + 3



        elif player_choice_bladestorm == 5 and bladestorm >= 10:
          for i in range(10):
            print("30 damage")
            print("ow!")
          print("You cut down the virus with a flurry of slashes!")
          print("You dealt a total of 300 damage!!!")
          boss_health = boss_health - 300
          print("Boss Health: "+ str(boss_health))
          bladestorm = bladestorm - bladestorm
          turn_count = turn_count - 1



        else:
          print("You might have put an invalid number")
          print("If you are on skill cooldown STOP SPAMMING THE SAME SKILLS THERE ARE COOLDOWNS")
          print("You did zero damage and are on a turn cooldown")
          turn_count = turn_count - 3


      #takes skill number as input
      else: 
        print("Skill 1: Steal")
        print("Skill 2: Quick Cut")
        print("Skill 3: Counter")
        print("Skill 4: Dash")
        player_choice = int(input("Enter the Skill Number: "))


        #based on skill number it will deal take away a certain amount of boss_health or inflict a status effect. After a skill is played the turn_count will go to zero and the boss loop will play.
        if player_choice == 1 and steal >= 1:
          print("STEAL!")
          print("You gained reduced ultimate skill cooldown by one")
          bladestorm = bladestorm + 1
          print("Boss Health: "+ str(boss_health))
          turn_count = turn_count - 1



        elif player_choice == 2 and quick_cut >= 4:
          print("You slashed the virus with extreme speed")
          print("You did 100 damage!!!")
          print("Boss Health: "+ str(boss_health))
          quick_cut = quick_cut - quick_cut
          turn_count = turn_count - 1



        elif player_choice == 3 and counter >= 4:
          print("You countered all of the virus's attacks")
          print("Health lost = Damage dealt")
          print("Boss Health: "+ str(boss_health))
          counter = counter - counter
          turn_count = turn_count - 1



        elif player_choice == 4 and dash >= 5:
          print("You dashed straight at the virus catching it off guard!")
          print("You got ahead of the virus and have gained 3 extra turns!")
          print("Boss Health: "+ str(boss_health))
          dash = dash - dash
          turn_count = turn_count + 3



        else:
          print("You might have put an invalid number")
          print("If you are on skill cooldown STOP SPAMMING THE SAME SKILLS THERE ARE COOLDOWNS")
          print("You did zero damage and are on a turn cooldown")
          turn_count = turn_count - 3




    #The boss loop will randomly choose a skill and it will carry out the skill. After it will return the turn_count to 1 and the player loop will begin
    while turn_count <= 0:

      #Reduce the skill cooldown to make the skills usable
      steal = steal + 1
      quick_cut = quick_cut + 1
      counter = counter + 1
      dash = dash + 1
      bladestorm = bladestorm + 1

      #picks random skill
      boss_skill = random.randint(1,5)

      if boss_skill == 1:
        print("The virus used worm and is eating at your files")
        player_health = player_health - 25
        for i in range(25):
          print("1 damage")
        print("Player Health: "+ str(player_health))
        turn_count = turn_count + 1



      elif boss_skill == 2:
        print("The virus used Trojan and is taking over your computer")
        print("Your information isn't safe anymore!!!")
        player_health = player_health - 50
        print("50 DAMAGE")
        print("Player Health: "+ str(player_health))
        turn_count = turn_count + 1



      elif boss_skill == 3:
        print("The virus used Ransomware and is forcing you pay for access to your files")
        print("You're forced to pay!!!")
        bladestorm = bladestorm - 3
        print("Your ultimate skill cooldown is increased by 3 turns :(")
        print("Player Health: "+ str(player_health))
        turn_count = turn_count + 1



      elif boss_skill == 4:
        print("The virus used adware and is collecting your information")
        print("Ads are being spammed on your screen!!!")
        for i in range(10):
          print("BRUH")
        player_health = player_health - 10
        print("10 damage")
        print("Player Health: "+ str(player_health))
        turn_count = turn_count + 1



      elif boss_skill == 5:
        print("The virus used Spyware and predicts your next two attacks")
        print("You lose two turns!!!")
        turn_count = turn_count - 2
        print("Player Health: "+ str(player_health))
        turn_count = turn_count + 1
    

    #when the boss health or your health reaches 0 the game ends
    if boss_health <= 0:
      print("You Won!")
      done = True
    elif player_health <= 0:
      print("Game Over!!!!!!!!!!!!!!!!!")
      done = True


else:
  print("Invalid")
  print("You Failed")






