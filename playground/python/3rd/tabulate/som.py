# from tabulate import tabulate

# table = [
#     ["ziom", "one", "two", "three"],
#     ["ziom", "four", "five", "six"],
#     ["ziom", "seven", "eight", "nine"],
# ]

# s = tabulate(table, headers=["", "a", "b", "c"], tablefmt="html")
# with open("f.html", "w+") as f:
#     f.write(s)

import argparse
import datetime

parser = argparse.ArgumentParser()

parser.add_argument("-d", type=datetime.date.fromisoformat, default=datetime.date.today())
print(parser.parse_args().d)
