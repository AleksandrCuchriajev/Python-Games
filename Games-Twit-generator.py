# Let's create a twit generator to have some fun
# We have 4 lists in this game but you can add more
import random

part1 = ["Biden,", "Ukraine,", "Putin", "CNN,", "Mexico,", "Zelenckij", "Obama"]
part2 = ["no mercy,", "on the way up,", "really poor situation,", "said nasty words,", "looking like a fool,",
         "bad attitude,"]
part3 = ["got destroyed by my ratings.", "let's surrender.", "had a much smaller crowd.", "will pay for the fake."]
part4 = ["So bad", "Apologize", "So true", "Fake news won't report", "Big trouble", "Fantastic job", "Stay with me"]

all_parts = [part1, part2, part3, part4]

sentence = []
# Add randomly generated parts in the sentence list
for part in all_parts:
    random_number = random.randint(0, len(all_parts) - 1)
    sentence.append(part[random_number])
# prints the message, conversion from list to string
print(" ".join(sentence) + "!")
