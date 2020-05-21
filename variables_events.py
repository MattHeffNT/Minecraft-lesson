## function that then uses player object to display "message" variable in the minecraft chat
def on_chat():
    player.say(message)
    
## message variable that contains our sentence, it uses escape characters "\" to be able to display quotation 
## marks inside the minecraft chat 
message = "To say hello in Luritja we say \"palya\""

## if the player asks how they can say hello in Luritja, call the on_chat function
player.on_chat("How do you say hello in Luritja?", on_chat)
