There are still many optimizations that I can do to make this program more space and time efficient, among those being

-   just using an integer counter for counting neighbors instead of storing a list of them. I did it this way originally
    because it allows for room to do interesting things with the neighbor lists in the future, but is not needed as of now

-   Printing only the changes in a grid at each iteration

-   Terminating the program early when there are no changes between iterations

-   Using a boolean or integer array for computations, only converting it into strings when printing

-   Instead of deep copying the 2D array at every iteration, I can use two arrays and swap between the two as needed