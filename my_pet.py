# A text pet for OOP
# Author: Timothy Batchelder

# def main():

#   def __init__():
#     pet = pPick()
#     speech = pSpeak(pet)


#   # Pet Selector
#   def pPick():
#     cValid = False
#     while not cValid:
#       choice = input("Select a pet: Dog, Cat or Bird: ").lower()
#       if choice not in ["dog", "cat", "bird"]:
#         print("I don't have that type of pet available.  Please choose one I do have.")
#       else:
#         cValid = True
#         print("You have selected a", choice + ".")
#     return choice
  
#   # What will the pet speak when commanded
#   def pSpeak(p):
#     words = {
#       "dog": "Bark!",
#       "cat": "Meow.",
#       "bird": "Tweet."
#     }
#     return words[p]
  

  
#   d = "dog"
#   print(pPick())

#   return

# main()

def pSpeech(rnd):
  match rnd:
    case 0:
      return ["Woof!", "Woof.", "Woof, woof.", "Woofie, woof, woof!"]
    case 1:
      return ["Bark!", "Bark.", "Bark, bark.", "Barkety, bark, bark!"]
    case 2:
      return ["Yelp!", "Yelp.", "Yelp, yelp.", "Yelpety, yelp, yelp!"]
    case 3:
      return ["Awoo!", "Awoo.", "Aawwooooo", "Aw-aw-wooooooooo!"]

def pColor(rnd):
  colors = ["Brown", "White", "Black", "Marble"]
  return colors[rnd]

def pEyeColor(rnd):
  colors = ["Brown", "Black", "Green", "Blue"]
  return colors[rnd]

def pSize(rnd):
  size = ["Small", "Medium", "Large", "Extra-large"]
  return size[rnd]


print(pSize(3))