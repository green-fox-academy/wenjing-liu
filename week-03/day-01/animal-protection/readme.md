### Animal protection

You are going to create an animal shelter where we can save and take care of Animals.

#### Animal

- It must have `name` and stores it's `healthState` (true or false) and a `healCost`.
- It must have a method named `heal()`, that sets the `isHealthy` field's status to true
- It must have a method named `isAdoptable` that returns a boolean value whether it can be adopted or not     - an animal can be adopted if it is healthy
- It must have a method named `toString()` that represents the Animal in the following format:

```
<name> is not healthy (<heal cost>€), and not adoptable
<name> is healthy, and adoptable
```

*The animal's name is the same as the class name by default, but it can be set trough constructor as well*

##### Cat

**`Cat` is an `Animal`**

-  The healing cost should be a random number between 0 and 6

##### Dog

**`Dog` is an `Animal`**

-  The healing cost should be a random number between 1 and 8

##### Parrot

**`Parrow` is an `Animal`**

-  The healing cost should be a random number between 4 and 10

#### Animal shelter

- It must have a `budget`, an `animals` list, an `adopters` name list
- The shelter starts with 50€ without any Animal and adopter
- It must have a method named `rescue` this method takes an `Animal` as parameter 
  - and add the animal to the shelter's list and return the size of the list
- It must have a method named `heal` this method heals the first not healthy Animal
  - if it is possible by budget, returns the amount of healed animals(0 or 1)
- It must have a method named `addAdopter` this method takes a `name` as parameter 
  - and save it as a potential new owner
- It must have a method named `findNewOwner` 
  - this method pairs a random name with a random adoptable Animal if it is possible
  - and remove both of them from the lists
- It must have a method named `earnDonation` this method takes an `amount` as parameter 
  - and increase the shelter's budget by the parameter's value and returns the current budget
- It must have a method named `toString` that represents the shelter in the following format:

```
Budget: <budget>€, 
There are <animals.count> animal(s) and <potentionalAdopters.count> potential adopter(s)
<name> is not healthy (<heal cost>€), and not adoptable
<name> is healthy, and adoptable
```