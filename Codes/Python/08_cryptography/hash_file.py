#!/usr/bin/env python3
"""
Phase-2 · Stage 8 — Compute file hashes (integrity demo)
"""
from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


def hash_file(path: Path, algo: str = "sha256") -> str:
    h = hashlib.new(algo)
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute cryptographic hashes of a file.")
    parser.add_argument("file", type=Path, help="File to hash")
    parser.add_argument(
        "-a",
        "--algo",
        default="sha256",
        choices=["md5", "sha1", "sha256", "sha512"],
        help="Hash algorithm (default sha256; md5/sha1 for demo only)",
    )
    args = parser.parse_args()

    if not args.file.is_file():
        print(f"Not a file: {args.file}")
        return

    digest = hash_file(args.file, args.algo)
    print(f"{args.algo.upper()} ({args.file}) = {digest}")
    if args.algo in ("md5", "sha1"):
        print("Note: MD5/SHA-1 are not recommended for security-sensitive integrity checks.")


if __name__ == "__main__":
    main()
