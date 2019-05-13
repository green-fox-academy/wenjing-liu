class Pokemon(object):
    def __init__(self, name, type, effectiveAgainst):
        self.name = name
        self.type = type
        self.effectiveAgainst = effectiveAgainst

    def isEffectiveAgainst(self, anotherPokemon):
        return self.effectiveAgainst == anotherPokemon.type
    
    def __str__(self):
      return f'{self.name}: {self.type} against with {self.effectiveAgainst}'

def initializePokemons():
        pokemon = []

        pokemon.append(Pokemon("Balbasaur", "leaf", "water"))
        pokemon.append(Pokemon("Pikatchu", "electric", "water"))
        pokemon.append(Pokemon("Charizard", "fire", "leaf"))
        pokemon.append(Pokemon("Balbasaur", "water", "fire"))
        pokemon.append(Pokemon("Kingler", "water", "fire"))

        return pokemon

pokemon = initializePokemons()

# Every pokemon has a name and a type.
# Certain types are effective against others, e.g. water is effective against fire.

# Ash has a few pokemon.
# A wild pokemon appeared!

wildPokemon = Pokemon("Oddish", "leaf", "water")

effective_pokemans = []
for poke in pokemon:
  if poke.isEffectiveAgainst(wildPokemon):
    effective_pokemans.append(poke)

# Which pokemon should Ash use?
if len(effective_pokemans):
  print("I choose you, ")
  for poke in effective_pokemans:
    print(poke)


"""
# Pokemon

Every pokemon has a name and a type.
Certain types are effective against others, e.g. water is effective against fire.

You have a `Pokemon` class with a method called `isEffectiveAgainst()`.

Ash has a few pokemon. Help Ash decide which Pokemon to use against the wild one.

You can use the already created pokemon files.
"""