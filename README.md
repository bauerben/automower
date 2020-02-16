# Automower

This python program has been developed in order to manage several automatic lawnmowers across a square lawn.

Using an input file, mowers can be programmed to go throughout the whole surface :
- Mower's position is represented by coordinates (X,Y) and a characters indicate the orientation according to cardinal
notations (N,E,W,S).
- The lawn is divided in grid to simplify navigation.
- For example, the position can be 0,0,N, meaning the mower is in the lower left of the lawn, and
oriented to the north.
- Each mower move sequentially, meaning that the second mower moves only when the first has
fully performed its series of instructions.
- As the mower moves sequentially, we assume that there is no collision between mowers.

For each mower, the program returns their final position and orientation ( X Y O )

### Prerequisites

python3 is required

### Input file strucuture

In order to program the mower, we need to provide an input file constructed as follows:
- The first line correspond to the coordinate of the upper right corner of the lawn. the bottom left
corner is assumed as (0,0).
- The rest of the file can control multiple mowers deployed on the lawn. Each mower has 2 next
lines :
    - The first line give mower's starting position and orientation as "X Y O". X and Y being the
position and O the orientation.

    - The second line give instructions to the mower to go throughout the lawn. Instructions are
characters without spaces.
Each mower move sequentially, meaning that the second mower moves only when the first has
fully performed its series of instructions.

### Usage

```raw
$> python automower.py <input_file_path>
```
### Output

For each mower, the program returns their final position and orientation ( X Y O )

### Running tests

