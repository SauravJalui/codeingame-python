#https://www.codingame.com/training/easy/the-descent

import sys
import math

while True:
    max = 0
    maxIndex = 0
    for i in range(8):
        mountain_h = int(input())  
        if mountain_h > max:
            max = mountain_h
            maxIndex = i

    print(maxIndex)
