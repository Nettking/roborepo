# Manuscript Workspace

## Purpose
This repository houses a collection of long-form manuscripts written in LaTeX. Each book lives in its own subdirectory under `books/`, complete with its own `main.tex`, chapter files, and supporting materials so stories can evolve independently while sharing the same build tooling.

## Build Commands
All build automation is provided through the top-level `Makefile` and Docker image defined in the repository.

| Command | Description |
| --- | --- |
| `make build-image` | Builds the local Docker image (`latex-builder`) used for all LaTeX compilation. Run this once before generating PDFs. |
| `make pdf [BOOK=<name>] [PROJECT=main]` | Compiles the selected book inside the Docker container. Defaults to `BOOK=tides_of_marisport` and `PROJECT=main`. |
| `make clean [BOOK=<name>]` | Removes LaTeX auxiliary files for the chosen book. |
| `make clean-all [BOOK=<name>]` | Runs `make clean` and deletes the generated PDF for the selected book. |

> **Tip:** Override `BOOK` to compile an alternate manuscript, e.g. `make pdf BOOK=placeholder_book`.

## Repository Layout
- `books/` – Individual manuscripts and templates. See `books/readme.md` for summaries of each title.
- `Dockerfile` – Minimal image definition used by the Makefile to compile LaTeX safely in Docker.
- `Makefile` – Convenience targets for building and cleaning book outputs.
- `instructions.txt` – Background instructions for future writing tasks.

Happy writing! Explore each book's folder for chapter outlines, dispositions, and development notes.
