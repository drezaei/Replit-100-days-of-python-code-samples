print("Creepy Employee Registrar That Is Overly Friendly")
print("")

fname = input("Enter your first name: ").strip().capitalize()
lname = input("Enter your last name: ").strip()
dob = input("Enter your date of birth (day/month/year format): ").strip()
telephone = input("Enter your contact number: ").strip()
email = input("Enter your email address: ").strip().lower()
address = input("Enter your home address: ").strip().title()
print("")

user = {"name": fname, "last_name": lname, "dmy": dob, "contact": telephone, "email": email, "physical_address": address}

print(f"Hello, {user['name']}\nHow are things in the {user['last_name']} household? You will be getting a birthday phone call from us on your phone number: {user['contact']} on {user['dmy']}. I will also be visiting you to give you your complimentary hug at your home address: {user['physical_address']}. Thank you for your time and I hope you have a wonderful day, WE WILL SPEAK AGAIN!")
