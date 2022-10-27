import random 

score = 0
english =("Computer", "Lake", "Food","Radio","Build")
right_anwser = ("Rorohiko", "Roto", "Kai","Reo irirangi","Hanga")
option_1 = ("Aroha", "Hangi", "Kaumatua","Moana","Wahine")
option_2 = ("Waiata", "Pounamu", "Whānau","Hīkoi","Tamariki")

def generate_question(english, right_anwser, option_1, option_2):
  global score
  print("What is the correct word for", english, "in maori")

  random_sequence = random.randint(0,2)

  if(random_sequence == 0):
    print("A", option_1)
    print("B",option_2 )
    print("C", right_anwser)
    anwser = input().lower()
    if anwser == "c":
      score += 1
    else:
      print("incorrect")
  elif(random_sequence == 1):
    print("A", option_1)
    print("B", right_anwser)
    print("C", option_2)
    anwser = input().lower()
    if anwser == "b":
      score += 1
    else:
      print("incorrect")
  elif(random_sequence == 2):
    print("A", right_anwser)
    print("B", option_2)
    print("C", option_1)
    anwser = input().lower()
    if anwser == "a":
      score += 1
    else:
      print("incorrect")
  elif(random_sequence == 3):
    print("A", right_anwser)
    print("B", option_2)
    print("C", option_1)
    anwser = input().lower()
    if anwser == "a":
      score += 1
    else:
      print("incorrect")
  elif(random_sequence == 4):
    print("A", right_anwser)
    print("B", option_2)
    print("C", option_1)
    anwser = input().lower()
    if anwser == "a":
      score += 1
    else:
      print("incorrect")
for i in range (0, 5):
  generate_question(english[i],right_anwser[i],option_1[i],option_2[i])

print(score)