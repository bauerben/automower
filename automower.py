#!/usr/bin/env python3
# coding: utf-8

import sys
import os
import re


class Lawn:

    def __init__(self, xsize, ysize):
        self.xsize = xsize
        self.ysize = ysize

    def IsValidPosition(self,x,y):
        if x > self.xsize or y > self.ysize:
            valid_position = False
        else:
            valid_position = True
        return valid_position


class LawnMower:

    def __init__(self, x, y, direction):
        self.x = int(x)
        self.y = int(y)
        self.direction = direction

    def move(self, action):
        if action == 'L':
            # Do the thing
            print("going left")
            new_direction = rotate_left(self.direction)
            self.direction = new_direction
        elif action == 'R':
            # Do the thing
            print("going right")
            new_direction = rotate_right(self.direction)
            self.direction = new_direction
        elif action == 'F':
            # Do the thing
            print("going forward")
            if self.direction == 'N':
                self.y = self.y + 1
            if self.direction == 'W':
                self.x = self.x - 1
            if self.direction == 'S':
                self.y = self.y - 1
            if self.direction == 'E':
                self.x = self.x + 1
        else:
            print("invalid action")
            sys.exit(1)


def rotate_left(current_direction):
    if current_direction == 'N':
        new_direction = 'W'
    elif current_direction == 'W':
        new_direction = 'S'
    elif current_direction == 'S':
        new_direction = 'E'
    elif current_direction =='E':
        new_direction = 'N'
    return new_direction


def rotate_right(current_direction):
    if current_direction == 'N':
        new_direction = 'E'
    elif current_direction == 'E':
        new_direction = 'S'
    elif current_direction == 'S':
        new_direction = 'W'
    elif current_direction == 'W':
        new_direction = 'N'
    return new_direction


def parse_input_file(input_file_path):
    with open(input_file_path, "r") as file:
        lines = [line.rstrip('\n') for line in file]
    file_line_count = len(lines)

    # Checking & retrieving lawn size
    if re.match("(^[0-9]*\s[0-9]*$)", lines[0]):
        lawn_size_line = lines[0].split()
        x_lawn_size = lawn_size_line[0]
        y_lawn_size = lawn_size_line[1]
        if x_lawn_size == y_lawn_size:
            my_garden = Lawn(x_lawn_size, y_lawn_size)
        else:
            print("Lawn is not a square")
            sys.exit(1)
    else:
        print("Incorrect lawn size definition")
        sys.exit(1)

    # Checking and retrieving lawnmower data
    lawnmowers = []
    actions_sequences = []
    i = 1
    while i < len(lines):
        # Checking and retrieving lawnmower initial position
        if re.match("^[0-9]*\s[0-9]*\s(?:N|E|W|S)$", lines[i]):
            print("Getting mower position")
            mower_position_data = lines[i].split()
            x = mower_position_data[0]
            y = mower_position_data[1]
            direction = mower_position_data[2]
            if my_garden.IsValidPosition(x, y):
              lawnmowers.append(LawnMower(x, y, direction))
        else:
            print("Invalid initial mower position, syntax should be : X Y [N,E,W,S]")
            sys.exit(1)
        i += 1
        # Checking and retrieving actions sequences
        if re.match("^(?:L|R|F)*$", lines[i]):
            print("Getting mower actions")
            lawnmower_action_data = lines[i]
            actions_sequences.append(lawnmower_action_data)
        else:
            print("Invalid mower actions (should only include L,R,F commands")
            sys.exit(1)
        i += 1

    return my_garden, lawnmowers, actions_sequences


def main(file_path):
    my_garden, lawnmowers, actions_sequences = parse_input_file(file_path)
    i = 0
    while i < (len(lawnmowers)):
        for action in actions_sequences[i]:
            lawnmowers[i].move(action)
            print(str(lawnmowers[i].x) + " " + str(lawnmowers[i].y) + " " + lawnmowers[i].direction)
        print(str(lawnmowers[i].x)+" "+str(lawnmowers[i].y)+" "+lawnmowers[i].direction)
        i += 1


if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_file_path = sys.argv[1]
        if os.path.isfile(input_file_path):
            main(input_file_path)
    else:
        print("Missing Filename input")
        sys.exit(1)
