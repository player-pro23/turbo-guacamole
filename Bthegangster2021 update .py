


print("Welcome to B the gangster")
print("Will you help me find b the gangster and his team if yes carry on ")
print("there is are many numbers to reach b")
print("will you guess them  yes boss")
print("i am leaving you to b team mate we have areested just now he will tell you the informaion on those numbers with some the number will be beetwen 1- 100  ")
import random 
secret = random.randint(1, 100)
guess = 0


print("AHOY! I'm the  Roberts, and I have a secret of my boss!")
print("It is a number from 1 to 100. I'll give you 6 tries.")

while guess != secret and tries < 6 :
  guess = int(input("What's yer guess? "))
  print(guess)
  
  if guess < secret: 
    print("Too low, ye scurvy dog!")
  elif guess > secret:
    print("Too high, landlubber!")
  

tries = tries + 1
if guess == secret:
  print("Avast! Ye got it! Found my secret, ye did!")
else:
  print("No more guesses! Better luck next time, matey!")
  print("The secret number was", secret)

  
  print("now you won the scecret and b was aressted for life long prison")
print("game ended ")
End 
    
