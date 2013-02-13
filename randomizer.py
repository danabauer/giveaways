import sys
import numpy as np
import matplotlib.pyplot as plt
import csv

with open('names.csv', 'rb') as csvfile:
  csvreader = csv.DictReader(csvfile)
  people = []
  for row in csvreader:
    if row['Refunded'] == 'No':
      people.append(row)

  x = np.random.permutation(np.arange(0, len(people)))
  i = 0

  print "Ready."

  while i < len(x):
    sys.stdin.read(1)
    winner = people[x[i]]
    print "%s %s" % (winner['Attendee First Name'], winner['Attendee Last Name'])
    i += 1
