
# Problem statement 
You are to find a place to put each baby lizard in a nursery. The baby lizards have very long tongues. They can shoot out their tongue up, down, left, right and diagonally to eat other baby lizards. Their tongues are very long and can reach to the edge of the nursery from any location.
 
<br/> <br/>
![alt text](https://raw.githubusercontent.com/manthan1412/Lizards-problem/master/lizards2.jpg)
Figure (A) the baby lizard can attack any other lizard in a red square. (B) In this example setup, both lizards can eat each other. You need to avoid such cases.

<br />
Moreover, nursery may have some trees planted in it. The lizards cannot shoot their tongues through the trees nor can you move a lizard into the same place as a tree. A tree will block any lizard from eating another lizard if it is in the path.

<br/><br/>
![alt text](https://raw.githubusercontent.com/manthan1412/Lizards-problem/master/lizards2.jpg)
Both nurseries have valid arrangements of baby lizards such that they cannot eat one
another.

# Input format
The file input.txt in the current directory of program should be formatted as follows:

<b>First line</b>: instruction of which algorithm to use: BFS, DFS or SA<br/>
<b>Second line</b>: strictly positive integer n, the width and height of the square nursery<br/>
<b>Third line</b>: strictly positive integer p, the number of baby lizards<br/>
<b>Next n lines</b>: the n x n nursery, one file line per nursery row (to show you where the trees are).
It will have a 0 where there is nothing, and a 2 where there is a tree
