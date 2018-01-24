# Glosfer Test
#### Problem presentation
the problem to solve is as shown in the image below:
![alt text](https://d2gn4xht817m0g.cloudfront.net/conversation_message_attachment/i/315428-6f8185e7c8629fff8fe77fd25a273fe9-original "")
So, in short we have to find the total count of reachable safe coordinates.

#### Solving approach

To solve the problem, my first reflex was to think and look for known algorithms trying to spot any similarities to find an equation or some sort of optimized algorithm, the latter would drastically reduce the problem complexity. However, I had no luck with this first approach.

So I moved on to the next method, which was to go and try to visualise the coordinates representing the ones with bombs using stars and the safe ones with dashes.

The first thing to notice was that the map would be symmetrical on both the x and the y axises so we could just solve the problem for positive coordinates and then multiply the solution by 4.

Second, we start to visualise the "blocks" of coordinates (each block is defined by a 100x100 surface) to try and find some sort of pattern.
So we start with the first block as shown below, which shows us where the bombs are located, we can clearly see that there are some points that can lead to other blocks, as we can notice that there are some unreachable points in the block itself.

![alt text](https://preview.ibb.co/hGShDb/hycon1.png "")

So, continuing with the same approach we check the next block and we notice a pattern: the transversal line blocking us from accessing some points in the same block moved up a bit, and the pattern of points leading to the next block is being reduced by 1 (at each gate). Below we see the changes clearly from the image:

![alt text](https://preview.ibb.co/d4nkzG/hycon2.png "")
We can predict that from around the 5th block, we will have a no-escape block with the transversal line being the diagonal of the block. So we visualise the block and bingo!!
![alt text](https://preview.ibb.co/gMxqYb/hycon3.png "")

#### Putting it all together
So to get the total number of the safe points to which our dear John can move without being blown away with a mine, we will be looping through blocks and stopping at the ones with x+y=500, also we will be needing to filter off unreachable positions in each block, and suming up all the safe points.
Last we will multiply the result by 4 to cover the whole map.
PS: we also need to avoid readding the safe positions with x=0 or y=0 when doing our x4 multiplication.

#### Running the solution script

To run the solution script, simply make sure that you are in the same folder where the code is.

```
$ python solve.py
```

The code is also self explanatory.
