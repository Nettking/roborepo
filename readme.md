# Project Overview

This repository now organizes each LaTeX book inside the `books/` directory. Every book contains its own `main.tex`, chapter files, and supporting material so they can be managed independently.

## Available Books

- **sample_book** – The existing fantasy manuscript with ten chapters and supporting front matter. Its entry point is `books/sample_book/main.tex`.
- **placeholder_book** – A blank template ready for new content, located at `books/placeholder_book/main.tex`.

## Building a PDF

Use the `BOOK` variable with the provided `Makefile` to choose which book to compile:

```bash
make pdf                 # builds books/sample_book/main.tex by default
make pdf BOOK=placeholder_book
```

The generated PDF and auxiliary files are stored next to the selected book's `main.tex` file. Run the corresponding clean targets to remove build artifacts:

```bash
make clean BOOK=sample_book        # remove auxiliary files for the sample book
make clean-all BOOK=sample_book    # also remove the compiled PDF
```

## Sample Book Table of Contents

- **Front Matter**
  - Title Page
  - Table of Contents
- **Main Matter**
  1. [Chapter 1 – Low Tide](books/sample_book/chapters/chapter1.tex)
  2. [Chapter 2 – Undertow](books/sample_book/chapters/chapter2.tex)
  3. [Chapter 3 – Crosscurrents](books/sample_book/chapters/chapter3.tex)
  4. [Chapter 4 – Stormglass](books/sample_book/chapters/chapter4.tex)
  5. [Chapter 5 – Eyewall](books/sample_book/chapters/chapter5.tex)
  6. [Chapter 6 – Driftline](books/sample_book/chapters/chapter6.tex)
  7. [Chapter 7 – Soundings](books/sample_book/chapters/chapter7.tex)
  8. [Chapter 8 – Moorings](books/sample_book/chapters/chapter8.tex)
  9. [Chapter 9 – Crosscurrents](books/sample_book/chapters/chapter9.tex)
  10. [Chapter 10 – Outbound](books/sample_book/chapters/chapter10.tex)
- **Back Matter**
  - Appendices or References (to be added)
