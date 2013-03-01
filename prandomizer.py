#!/usr/bin/env python

#
# A pandas-based lottery ball picker for RedSnake 2013 giveaways
#

import sys
import pandas as pd
import random

FNAME = "Buyer First Name"
LNAME = "Buyer Last Name"


def lottery():
    df = pd.io.parsers.read_csv('names.csv')
    df_eligible = df[[FNAME, LNAME]][df['Refunded'] == 'No']
    df_shuff = pd.DataFrame(random.sample(df_eligible.index, len(df_eligible)))

    try:
        i = 0
        while i < len(df_shuff):
            yield df_eligible.ix[df_shuff[0][i]]
            i += 1

    except GeneratorExit:
        pass


def main():
    try:
        for lucky_winner in lottery():
            sys.stdin.read(1)
            print lucky_winner[FNAME], lucky_winner[LNAME]

    except KeyboardInterrupt:
        pass

    return 0


if __name__ == '__main__':
    sys.exit(main())
