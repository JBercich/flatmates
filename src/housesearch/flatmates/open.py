#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import argparse
import webbrowser

parser: argparse.ArgumentParser = argparse.ArgumentParser()
parser.add_argument("-s", "--start-page", type=int, default=1)
parser.add_argument("-e", "--end-page", type=int, default=25)
parser.add_argument("-m", "--max-amount", type=int, default=500)
target: str = "https://flatmates.com.au/rooms/sydney/males+max-{}+newest+private-room?"

def open() -> None:
    global parser, target
    args: argparse.Namespace = parser.parse_args()
    target = target.format(args.max_amount)
    print("target:", target)
    assert args.max_amount > 0 and args.max_amount < 1000, "invalid max"
    assert args.start_page <= args.end_page, "invalid page range"
    assert args.end_page - args.start_page <= 50, "max page limit of 50"
    print(f"opening pages: {args.start_page} to {args.end_page}")
    for page_num in range(args.start_page, args.end_page + 1):
        webbrowser.open_new_tab(target + f"page={page_num}")

