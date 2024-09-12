pets =['dog', 'cat', 'fish', 'bird', 'rabbit', 'hamster', 'snake','cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)


def describe_pet(animal_type, pet_name):
     print(f"\nI have a {animal_type}")
     print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet('hamster', 'harry')
describe_pet(pet_name='harry',animal_type='hamster')