### Christmas is coming!

Your task is to create a program where Santa can give away gifts to the good kids.

The program should have a `Santa` and a `School` which can store `Kid`s.

#### Kid

```
Properties
- name
- age
- is good
- is happy

Behaviour
- get a gift
  - it should make the Kid happy
- introduce
  - should return information about the kid
  - example 1:  "My name is Bob, I am 10 years old. I am happy!"
  - example 2:  "My name is Alice, I am 12 years old. I am not happy."
```

We should be able to create new Kids by providing the `name`, `age` and whether it is `good`. Every kid is **not happy** by default.

#### Santa

```
Properties
- name
- age
- number of gifts

Behaviour
- introduce
  - should return information about the santa
  - example 1: "My name is Joe, I am 48 years old. I have 20 gifts in my bag."
  - example 2: "My name is Joe, I am 48 years old. I do not have any gifts in my bag."
- assign gifts
  - it should take a list of Kids as parameter
  - it should call each kid's `get a gift` behaviour if the kid is good and if Santa has any gifts left
  - if a gift is given, the `number of gifts` stored in Santa's bag should decrease (this cannot go under 0)
  - it should not do anything with the not good kids
  - in the end return the number of gifts which was given away
```

We should be able to create a new Santa by providing the `name` and `age`. The `number of gifts` should be 100 by default.

#### School

```
Properties
- list of kids

Behaviour
- enroll a new `Kid`
  - it should get a Kid as a parameter
  - add the new Kid to the `list of kids`
  - 

- have Christmas
  - it should get a Santa as a parameter
  - call Santa's `assign gifts` behaviour
```