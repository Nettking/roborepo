PROJECT=main
IMAGE=latex-builder

# Build Docker image (only once)
build-image:
	docker build -t $(IMAGE) .

# Compile LaTeX document inside Docker
pdf: build-image
	docker run --rm -v $(PWD):/data $(IMAGE) $(PROJECT).tex

# Clean auxiliary files
clean:
	rm -f *.aux *.log *.out *.toc *.bbl *.blg *.fls *.fdb_latexmk

# Clean everything including PDF
clean-all: clean
	rm -f $(PROJECT).pdf
