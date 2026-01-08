"""Convert the original semicolon-separated TXT dataset to CSV."""

from __future__ import annotations

import argparse

import pandas as pd


def main() -> None:
    parser = argparse.ArgumentParser(description="TXT (;) -> CSV converter")
    parser.add_argument("--input", required=True, help="Path to input .txt file")
    parser.add_argument("--output", required=True, help="Path to output .csv file")
    args = parser.parse_args()

    df = pd.read_csv(args.input, sep=";", engine="python")
    df.to_csv(args.output, index=False)
    print(f"Wrote {len(df):,} rows x {len(df.columns):,} columns to {args.output}")


if __name__ == "__main__":
    main()
