import time
name = input("Hello, what's your name? \n")
print(name+" is a very nice name! It's nice to meet you.")
time.sleep(3)
Q1 = input("Would you like to get to know each other a bit better? Y or N? \n")
if Q1 == "N":
  print("Aw, okay. Goodbye now.")
if Q1 == "Y":
  print("Great! Please answer with A, B, or C for my multiple choice questions, and Y or N for my yes or no questions! This will be so much fun!")
  time.sleep(6)
  Q2 = input(name+", which of these do you prefer? \nA) vibrant colors \nB) muted colors \nC) pastels \n")
  if Q2 == "A":
    print("Me too! I wish everyday were full of rainbows and unicorns! I also like clubs because they have bright, strobbing lights!")
    time.sleep(5)
    Q21 = input("Do you like clubs? \n")
    if Q21 == "Y":
      print("Yay! That means we already have two things in common! I think we are off to a great start!")
    elif Q21 == "N":
      print("Aw, I guess we won't be going out clubbing together anytime soon. But we both like vibrant colors so at least we have that in common!")
    else:
      "I'm sorry. I only understand Y or N for yes or no questions. But that's okay! Let's keep going!"
      time.sleep(3)
  if Q2 == "B":
    print("Well... I prefer vibrant colors, I think that they make the world a better place! But I understand that some people find flashy colors an eyesore.")
    time.sleep(4)
    Q22 = input(name+", do you find bright colors an eyesore? Y or N? \n")
    if Q22 == "Y":
      print("That's too bad. But let's keep going!")
      time.sleep(2)
    elif Q22 == "N":
      print("Oh, that's good! Now, let's continue!")
      time.sleep(2)
    else:
      print("I'm sorry. I only understand Y or N for yes or no questions. But that's okay! Let's keep going!")
      time.sleep(3)
  if Q2 == "C":
    print("Pastel colors are quite nice, though I prefer vibrant colors! I also like unicorns, which I've seen drawn in both vibrant colors and pastels!")
    time.sleep(4)
    Q23 = input(name+", do you like unicorns, too? Y or N? \n")
    if Q23 == "Y":
      print("Yay! That's great, "+name+"! Now let's continue!")
      time.sleep(2)
    if Q23 == "N":
      print("Well maybe one day you will apreciate these majestic creatures. Let's continue!")
      time.sleep(2)
  print("I already feel like we know each other better!")
  time.sleep(2)
  Q3 = input("Which of these colors do you prefer? \nA) Red \nB) Blue \nC) Yellow \n")
  if Q3 == "A":
    print("Oh, so you like red? I think it's gross. Blue is the only color I like, I wish all the other colors would all just go and die! Haha, I'm kidding... kidding...")
    time.sleep(5)
    print("Um... so moving on...")
    time.sleep(1)
  if Q3 == "B":
    print("YAYYYY! I LOVE the color blue! "+name+", you rock! Let's continue.")
    time.sleep(21)
  if Q3 == "C":
    print("EW! Yellow is gross. Yuck! But I guess favorite colors don't really matter... okay, let's move on.")
    time.sleep(3)