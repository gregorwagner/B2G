import argparse, sys
from itertools import *
from random import *

def main():
  parser = argparse.ArgumentParser(description="Generate automated test script for orangutan")
  parser.add_argument("-s", "--steps", help="Number of steps")
  args = parser.parse_args(sys.argv[1:])

  maxX = 320
  maxY = 520 # The home key is around (44, 515)

  if (args.steps):
    steps = int(args.steps)
  else:
    steps = 10000

  count = 0
  sleepAllowed = 1
  while (count < steps):
    x = choice(['tap', 'sleep', 'drag'])
    if x=='tap':
      # tap [x] [y] [num times]
      print 'tap ', randint(1, maxX), ' ', randint(1, maxY), ' ', randint(1,3)
      sleepAllowed = 1
      count = count + 1
    elif x=='sleep':
      # sleep [duration in msec]
      if (sleepAllowed):
        print 'sleep', randint(100, 3000)
        count = count + 1
        sleepAllowed = 0
    else:
      # drag [start x] [start y] [end x] [end y] [num steps] [duration in msec]
      print 'drag',randint(1, maxX), ' ', randint(1, maxY), ' ' , randint(1, maxX), ' ', randint(1, maxY), ' ', randint(10, 20), ' ', randint(10, 350)
      sleepAllowed = 1
      count = count + 1

if __name__ == "__main__":
  main()