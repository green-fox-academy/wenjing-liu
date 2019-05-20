### Hero battle

You are going to simulate a fight between Superheroes.

#### Hero

- It must have a name.
- It must have a motivation: a number represents how much the hero wants to save the world
- It must set the motivation and name when creating an instance.
- It must have a `getMotivationLevel` method which returns a number between 0 and 2
  - 0 if the motivation below 25
  - 1 if the motivation between 25 and 40
  - 2 if motivation is above 40
- It must have a `punch` method which is take a damage on the **other hero** by using his/her `bePunched` function
  - damage = the puncher hero's motivation / 1.5
  - the hero punches other heroes only if his/her motivation level is at least 1
- It must have a `bePunched` method which takes a `damage` as a parameter
  - bePunched: the hero suffers damage, so his/her motivation decreases 
  - motivation = motivation - (damage / motivation)
- toString: returns a string status report about the hero
  - if the hero's motivation level is 0: {name} is not motivated anymore.
  - if the hero's motivation level is 1: {name} is motivated.
  - if the hero's motivation level is 2: {name} is well motivated.

##### DCHero

**`DCHero` is a `Hero`**
- It must have a default motivation 45 if the name is provided only.
- A DCHero shouldn't be able to punch another DCHero.

##### MarvelHero 

**`MarvelHero` is a `Hero`**
- It must have a default motivation 40 if the name is provided only.
- A MarvelHero shouldn't be able to punch another MarvelHero. 

**LET'S FIGHT BETWEEN THE SUPERHEROES**