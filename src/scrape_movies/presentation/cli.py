"""@brief Command-line entry point that runs the lecture steps."""

import argparse
from collections.abc import Sequence

from scrape_movies.presentation import hacker_news_steps, soup_steps


def build_parser() -> argparse.ArgumentParser:
    """@brief Build the argument parser.

    @return The parser with one sub-command per lecture.
    """
    parser = argparse.ArgumentParser(
        prog="python -m scrape_movies",
        description="Day 45 of 100 Days of Code: web scraping exercises.",
    )
    commands = parser.add_subparsers(dest="command")
    soup = commands.add_parser("soup", help="parse the sample page website.html")
    soup.add_argument("step", choices=list(soup_steps.STEPS))
    news = commands.add_parser("hacker-news", help="scrape the Hacker News front page")
    news.add_argument("step", choices=hacker_news_steps.STEPS)
    news.add_argument(
        "--source",
        choices=hacker_news_steps.SOURCES,
        default="mirror",
        help="the course mirror (default), the live site or the saved copy",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """@brief Run the command given on the command line.

    @param argv The arguments, or None to read `sys.argv`.
    @return The process exit code.
    """
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command == "soup":
        print(soup_steps.render_step(args.step))
        return 0
    if args.command == "hacker-news":
        print(hacker_news_steps.render_step(args.step, args.source))
        return 0
    parser.print_help()
    return 0
