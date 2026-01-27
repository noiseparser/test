"""Command-line interface for logsift.

This module wires up the top-level ``logsift`` command and its
subcommands. The actual parsing/filtering/stats logic will live in
dedicated modules; for now the subcommands are stubs that validate
arguments and report that they are not yet implemented.
"""

import argparse
import sys

SUPPORTED_FORMATS = ("apache", "nginx", "json")


def cmd_parse(args):
    """Parse a log file into structured records."""
    print(
        f"parse: format={args.format} path={args.path} "
        "(not yet implemented)",
        file=sys.stderr,
    )
    return 1


def cmd_filter(args):
    """Filter log records by a simple expression."""
    print(
        f"filter: expr={args.expr!r} path={args.path} "
        "(not yet implemented)",
        file=sys.stderr,
    )
    return 1


def cmd_stats(args):
    """Compute summary statistics over a log file."""
    print(
        f"stats: path={args.path} top={args.top} "
        "(not yet implemented)",
        file=sys.stderr,
    )
    return 1


def build_parser():
    """Construct the top-level argument parser."""
    parser = argparse.ArgumentParser(
        prog="logsift",
        description="Parse, filter, and analyze log files.",
    )
    subparsers = parser.add_subparsers(dest="command", metavar="command")
    subparsers.required = True

    p_parse = subparsers.add_parser(
        "parse", help="parse a log file into structured records"
    )
    p_parse.add_argument("path", help="path to the log file")
    p_parse.add_argument(
        "-f",
        "--format",
        choices=SUPPORTED_FORMATS,
        default="apache",
        help="input log format (default: apache)",
    )
    p_parse.set_defaults(func=cmd_parse)

    p_filter = subparsers.add_parser(
        "filter", help="filter log records by an expression"
    )
    p_filter.add_argument("path", help="path to the log file")
    p_filter.add_argument(
        "-e",
        "--expr",
        required=True,
        help="filter expression, e.g. 'status >= 500'",
    )
    p_filter.set_defaults(func=cmd_filter)

    p_stats = subparsers.add_parser(
        "stats", help="compute summary statistics"
    )
    p_stats.add_argument("path", help="path to the log file")
    p_stats.add_argument(
        "-n",
        "--top",
        type=int,
        default=10,
        help="number of top entries to show (default: 10)",
    )
    p_stats.set_defaults(func=cmd_stats)

    return parser


def main(argv=None):
    """Entry point for the ``logsift`` console script."""
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
