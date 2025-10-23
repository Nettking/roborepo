#!/usr/bin/env python3
"""Prompt for a book selection and compile it using the Docker LaTeX builder."""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--project",
        default="main",
        help="Name of the LaTeX project (tex file without extension) to compile.",
    )
    parser.add_argument(
        "--image",
        default="latex-builder",
        help="Docker image to run when compiling the selected book.",
    )
    return parser.parse_args()


def discover_books(project: str) -> list[Path]:
    """Return the list of book directories that contain the requested project file."""
    repo_root = Path(__file__).resolve().parent.parent
    books_dir = repo_root / "books"
    if not books_dir.is_dir():
        raise SystemExit(f"Books directory not found at {books_dir}.")

    candidates = []
    for entry in sorted(books_dir.iterdir()):
        if entry.is_dir() and not entry.name.startswith('.'):
            tex_file = entry / f"{project}.tex"
            if tex_file.exists():
                candidates.append(entry)
    return candidates


def prompt_for_book(books: list[Path]) -> Path:
    """Interactively ask the user which book to compile."""
    if not books:
        raise SystemExit("No books with the requested project were found to compile.")

    print("Select a book to compile:\n")
    for index, book in enumerate(books, start=1):
        print(f"  {index}. {book.name}")

    while True:
        try:
            selection = input("\nEnter the number of the book to compile: ").strip()
        except EOFError:  # Handles Ctrl+D or piped execution without input
            raise SystemExit("No selection received; aborting compilation.") from None

        if not selection:
            print("Please enter a number from the list above.")
            continue

        if not selection.isdigit():
            print(f"'{selection}' is not a valid number. Try again.")
            continue

        index = int(selection)
        if not 1 <= index <= len(books):
            print(f"Please choose a number between 1 and {len(books)}.")
            continue

        return books[index - 1]


def compile_book(book: Path, project: str, image: str) -> int:
    """Run the Docker command to compile the selected book."""
    repo_root = Path(__file__).resolve().parent.parent
    working_dir = Path("books") / book.name
    tex_filename = f"{project}.tex"

    command = [
        "docker",
        "run",
        "--rm",
        "-v",
        f"{repo_root}:/data",
        "-w",
        f"/data/{working_dir}",
        image,
        tex_filename,
    ]

    print(f"\nCompiling '{book.name}' using '{tex_filename}'...\n")
    return subprocess.run(command, check=False).returncode


def main() -> int:
    args = parse_args()
    books = discover_books(args.project)
    book = prompt_for_book(books)
    return compile_book(book, args.project, args.image)


if __name__ == "__main__":
    sys.exit(main())
