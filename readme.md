# Project Overview

This repository now organizes each LaTeX book inside the `books/` directory. Every book contains its own `main.tex`, chapter files, and supporting material so they can be managed independently.

## Available Books

- **tides_of_marisport** – The existing fantasy manuscript with ten chapters and supporting front matter. Its entry point is `books/tides_of_marisport/main.tex`.
- **placeholder_book** – A blank template ready for new content, located at `books/placeholder_book/main.tex`.

## Building a PDF

Use the `BOOK` variable with the provided `Makefile` to choose which book to compile:

```bash
make pdf                 # builds books/tides_of_marisport/main.tex by default
make pdf BOOK=placeholder_book
```

The generated PDF and auxiliary files are stored next to the selected book's `main.tex` file. Run the corresponding clean targets to remove build artifacts:

```bash
make clean BOOK=tides_of_marisport        # remove auxiliary files for Tides of Marisport
make clean-all BOOK=tides_of_marisport    # also remove the compiled PDF
```

## Tides of Marisport Table of Contents

- **Front Matter**
  - Title Page
  - Table of Contents
- **Main Matter**
  1. [Chapter 1 – Low Tide](books/tides_of_marisport/chapters/chapter1.tex)
  2. [Chapter 2 – Undertow](books/tides_of_marisport/chapters/chapter2.tex)
  3. [Chapter 3 – Crosscurrents](books/tides_of_marisport/chapters/chapter3.tex)
  4. [Chapter 4 – Stormglass](books/tides_of_marisport/chapters/chapter4.tex)
  5. [Chapter 5 – Eyewall](books/tides_of_marisport/chapters/chapter5.tex)
  6. [Chapter 6 – Driftline](books/tides_of_marisport/chapters/chapter6.tex)
  7. [Chapter 7 – Soundings](books/tides_of_marisport/chapters/chapter7.tex)
  8. [Chapter 8 – Moorings](books/tides_of_marisport/chapters/chapter8.tex)
  9. [Chapter 9 – Crosscurrents](books/tides_of_marisport/chapters/chapter9.tex)
  10. [Chapter 10 – Outbound](books/tides_of_marisport/chapters/chapter10.tex)
- **Back Matter**
  - Appendices or References (to be added)
