# Minecraft Lesson 2, Indigital

# change game time to dusk, set difficulty to normal and display message to player
def begin():
    gameplay.set_difficulty(NORMAL)
    gameplay.time_set(gameplay.time(DUSK))
    player.say("type \"whistle\" at night if you dare")

# if player types stop, restore peaceful game setting
def stop():
    gameplay.set_difficulty(PEACEFUL)
    gameplay.time_set(gameplay.time(DAY))
    loops.pause(300)
    gameplay.set_difficulty(NORMAL)

# hairyman function
def hairyman():
        mobs.spawn(mobs.monster(ZOMBIE), player.position())
        mobs.spawn(mobs.monster(ZOMBIE), player.position())
        mobs.spawn(mobs.monster(ZOMBIE), player.position())


# when the game starts display the messages below to the player       
player.say("The \"Hairyman\" is an infamous creature in Indigenous lore the hairy man is known to attack those who whistle and call it's attention at night  Can you evade the hairy man once you've whistled? To begin the hairyman challenge type \"begin\"")

# when player types in whistle, call the "hairyman" function
player.on_chat("whistle", hairyman)

# when player types begin call begin function
player.on_chat("begin", begin)

# if player types stop, restore peaceful game setting
player.on_chat("stop", stop)
