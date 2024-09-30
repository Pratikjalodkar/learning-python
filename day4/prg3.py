import random

test_seed = int(input("Enter a seed number:"))
random.seed(test_seed)

nameAsCSV = input("Give me everyone's name seperated by comma: ")
names = nameAsCSV.split(", ")

# num_items = len(names)
# random_choice = random.randint(0, num_items-1)
# person_who_pay = names[random_choice]
# print(person_who_pay+ " will pay the bill")



person_who_pay = random.choice(names)
print(person_who_pay+ " will pay the bill")