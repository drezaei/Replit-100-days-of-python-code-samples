# Create a dictionary that stores the following information about a website: name, URL, description and a star rating (out of 5).
# Use a loop to output the names of the keys, ask the user to type in the details and store the input in the dictionary.
# Finally, output the whole dictionary (keys and values).

# When creating your dictionary, you will need to use example = { "MyValue": none} to show a key name and no value.
# Use a loop to print the entire dictionary.
# Make sure you include both variables (name and value) in your loop and your print statement.

# Extra points for getting all the inputs with just one input command and the split function.


import os

os.system("cls")

def inputs():
    website=input("Type in the website name:        ").strip().capitalize()
    domainName=input("Type in the top level domain name of the website:     ").strip().lower()
    description=input("Describe the website:        ").strip().capitalize()
    rates=input("What do you give the website out of 5, with 1 being the lowest, and 5 the best rating: ")
    rating = f"{rates}/5"
    review=input("Give the website a short review:      ").strip().capitalize()
    return website, domainName, description, rating, review

def wobsite(website, domainName, description, rating, review):
    os.system("cls")
    myWebsite = {"Website":website,"URL Address":domainName,"Description":description,"Rating":rating,"Review":review}

    for name, value in myWebsite.items():
        print(f"{name}  :   {value}")
         
website, domain_name, description, rating, review = inputs()

wobsite(website, domain_name, description, rating, review)



#myDictionary = {"name" : "David the Mildy Terrifying", "health": 186, "strength": 4, "equipped":"l33t haxx0r p0werz"}

#for name, value in myDictionary.items():
#print(f"{name}: {value}")

#if (name == "strength"): 
#if value > 100: # This nested if wasn't indented properly
#  print("Whoa, SO STRONG")
#else:
#  print("Looks like you skipped leg day, arm day, chest day and, well, gym day entirely bro!")