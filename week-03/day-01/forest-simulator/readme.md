### Forest simulator

You are going to model a Forest with rain and a lumberjack who cuts tall trees.

#### Tree

- Trees should have a height.
- We must be able to create trees in two ways:
  - providing `height`
  - not providing `height`, in this case the height will be 0 by default.
- It must have an `irrigate` method which will increase the height of the tree. It must be an abstract method and implementation should depend on the type of the tree.
- It must have a `getHeight` method which returns the tree's height.

##### WhitebarkPine

- This tree type grows by 2 units each time its irrigated.

##### FoxtailPine

- This tree type grows by 1 unit each time its irrigated.

#### Lumberjack

You must be able to create a lumberjack without providing any parameters.

- It must have a `canCut(tree)` method which takes a tree as parameter and returns true if its taller than 4 units.

#### Forest

- It should have a list of trees.
- We should be able to create a forest by providing the trees that live there.
- It must have a `rain` which should iterate through the trees and irrigate them one by one.
- It must have a `cutTrees(lumberjack)` which should remove all the trees which can be cut by the lumberjack. (It calls the `canCut` method on the lumberjack).
- It must have an `isEmpty` method which returns true if there is no tree in the forest.
- It must have a `getStatus` method which returns an array with status reports about each tree in the forest. eg.:

```
[
  'There is a 3 tall WhitebarkPine in the forest.',
  'There is a 2 tall WhitebarkPine in the forest.',
  'There is a 4 tall FoxtailPine in the forest.'
]
```