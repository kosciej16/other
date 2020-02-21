import argparse
import json
import sys
from functools import partial
from itertools import groupby


def get_key(data, key_name):
    return data.get(key_name)


def delete_key_from_dicts(key_name, iterate_of_dicts):
    result = list(iterate_of_dicts)
    for d in result:
        d.pop(key_name)
    return result


def nest_dict(data, levels):
    if not levels:
        return data
    return nest_levels(levels, data)


def nest_levels(levels, data):
    dic = {}
    if not levels:
        return data
    key_name = levels[0]
    for key, group in groupby(data, partial(get_key, key_name=key_name)):
        dic[key] = delete_key_from_dicts(key_name, group)
        dic[key] = nest_levels(levels[1:], dic[key])
    return dic


def configure_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("levels", metavar="N", type=str, nargs="*", help="level names of nesting")
    return parser.parse_args()


if __name__ == "__main__":
    data = sys.stdin.read()
    args = configure_parser()
    dic = nest_dict(json.loads(data), args.levels)
    print(json.dumps(dic, indent=4, sort_keys=True))
