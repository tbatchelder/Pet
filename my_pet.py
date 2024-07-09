# A text pet for OOP
# Author: Timothy Batchelder

def main():

  def __init__():
    pet = pPick()
    speech = pSpeak(pet)


  # Pet Selector
  def pPick():
    cValid = False
    while not cValid:
      choice = input("Select a pet: Dog, Cat or Bird: ").lower()
      if choice not in ["dog", "cat", "bird"]:
        print("I don't have that type of pet available.  Please choose one I do have.")
      else:
        cValid = True
        print("You have selected a", choice + ".")
    return choice
  
  # What will the pet speak when commanded
  def pSpeak(p):
    words = {
      "dog": "Bark!",
      "cat": "Meow.",
      "bird": "Tweet."
    }
    return words[p]
  

  
  d = "dog"
  print(pPick())

  return

main()