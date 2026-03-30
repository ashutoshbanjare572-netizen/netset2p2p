"""Command line interface for netset2p2p."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .converter import NetsetParseError, convert_netset_text_to_p2p


def build_parser() -> argparse.ArgumentParser:
    """Create and configure the CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="netset2p2p",
        description="Convert netset files to p2p files.",
    )
    parser.add_argument("input", type=Path, help="Path to input .netset file")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="Path to output .p2p file (default: stdout)",
    )
    parser.add_argument(
        "--label",
        default="netset2p2p",
        help="Label prefix for generated p2p entries (default: netset2p2p)",
    )
    parser.add_argument(
        "--allow-ipv6",
        action="store_true",
        help="Include IPv6 entries if present in the input netset",
    )
    parser.add_argument(
        "--skip-invalid",
        action="store_true",
        help="Skip invalid or unsupported lines instead of failing",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """Run the CLI command."""
    parser = build_parser()
    args = parser.parse_args(argv)

    input_text = args.input.read_text(encoding="utf-8")
    try:
        output_text = convert_netset_text_to_p2p(
            input_text,
            label=args.label,
            allow_ipv6=args.allow_ipv6,
            skip_invalid=args.skip_invalid,
        )
    except (NetsetParseError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    if args.output is None:
        print(output_text, end="")
    else:
        args.output.write_text(output_text, encoding="utf-8")

    return 0
