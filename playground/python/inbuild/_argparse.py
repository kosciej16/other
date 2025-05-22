import functools
import argparse
import textwrap


def epilog():
    parser = argparse.ArgumentParser(
        prog="ProgramName",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(
            """\
             additional information:
                 I have indented it
                 exactly the way
                 I want it
             """
        ),
    )
    parser.add_argument("--foo", nargs="?", help="foo help")
    parser.add_argument("bar", nargs="+", help="bar help")
    parser.add_argument("--som", default=None, action="store_true", help="bar help")
    parsed = parser.parse_args()
    print(parsed)
    parser.print_help()


def _custom_format(s):
    return s.replace("u", "a")


class CustomHelpFormatter(argparse.HelpFormatter):
    def _format_usage(self, usage, actions, groups, prefix) -> str:
        # usage = super()._format_usage(None, [], [], "")
        usage = super()._format_usage(None, actions, [], "")
        # print(actions, groups, prefix)
        return usage.replace("a", "b")


# Use the custom formatter in the parser
# parser = argparse.ArgumentParser(formatter_class=CustomHelpFormatter)


def nargs():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        "echo",
        help="""
                        echo
                        echo2""",
    )
    # parser.add_argument("--a", nargs="*", help="a")
    # subparsers = parser.add_subparsers(help="types of A")
    # a_parser = subparsers.add_parser("A", add_help=False, formatter_class=CustomHelpFormatter)
    # a_parser = subparsers.add_parser("A", formatter_class=CustomHelpFormatter)
    # a_parser = subparsers.add_parser("A")
    # b_parser = subparsers.add_parser("B")
    # a_parser.add_argument("something", choices=["a1", "a2"])
    # a_parser.format_usage = functools.partial(_custom_format, s=a_parser.format_usage())
    # print(a_parser.format_help())
    # print(a_parser.format_usage())
    # print(a_parser.format_help())

    # print(parser.format_usage())
    # args = parser.parse_args()
    # print()
    # print(args.echo)
    return parser


# p = nargs()
# p.parse_args()

parser = argparse.ArgumentParser()

# Three common approaches:

# 1. Store true/false with default None
parser.add_argument("--flag1", action="store_true")
parser.add_argument("--no-flag1", action="store_false", dest="flag1")

# 2. Using type=bool (not recommended, harder to use)
parser.add_argument("--flag2", type=bool, default=None)

# 3. Best practice: Using explicit choices
parser.add_argument("--flag3", choices=["true", "false"], default=None)

args = parser.parse_args()
print(f"flag1: {args.flag1}")  # None if not specified
print(f"flag2: {args.flag2}")  # None if not specified
print(f"flag3: {args.flag3}")  # None if not specified
