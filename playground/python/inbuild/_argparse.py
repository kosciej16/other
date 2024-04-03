import argparse
import textwrap

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
parser.print_help()
