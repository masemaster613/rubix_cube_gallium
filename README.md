# rubix_cube_galluim

I am trying a couple different implementations of a 2x2x2 rubix cube in python.

v1 is basically my brute force method where i defent what each possible move changes on the cube. Eache square is represented by nested lists giving it three coordinates (which face its on, what row it is in, and which column in that row). The major issues involve not ideal use of global variables and functions.

V2 defines each move using a dictionary that has keys for where each square starts and the value represents where the square is going, Then there is a general move function that takes the cube and the dictionary as inputs.

I am thinking of implementing a v3 where i define a class of cube pieces in teh cube. A 2x2x2 rubix cube has 8 pieces each with three sides, so tracking their position and orientation should give an alternate method of representing the cube.
