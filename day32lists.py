import random

print("RANDOM INSULT PICKER")
print("--------------------")
print("")

phrases=["Up yours, and the horse you rode in on", 
         "Eres más lento que una tortuga bailando ballet.", 
         "Tu as le charme d'une endive.", 
         "Sei più lento di un bradipo caffeinato.", 
         "Du hast den Witz eines leeren Bierkruges.", 
         "Jij hebt het inzicht van een pinda.", 
         "Du har humor som en grå fisk.", 
         "Você é mais perdido que cego em tiroteio."]

number_of_phrases = len(phrases)

random_phrase = random.choice(phrases)

print(random_phrase)