BOOK ?= tides_of_marisport
PROJECT ?= main
BOOK_DIR := books/$(BOOK)
IMAGE = latex-builder

# Build Docker image (only once)
build-image:
	docker build -t $(IMAGE) .

# Compile LaTeX document inside Docker
pdf: build-image
	@test -d $(BOOK_DIR) || (echo "Book '$(BOOK)' not found in $(BOOK_DIR)." && exit 1)
	docker run --rm -v $(PWD):/data $(IMAGE) $(BOOK_DIR)/$(PROJECT).tex

# Clean auxiliary files for the selected book
clean:
	@test -d $(BOOK_DIR) || (echo "Book '$(BOOK)' not found in $(BOOK_DIR)." && exit 1)
	@exts="aux log out toc bbl blg fls fdb_latexmk"; \
	for ext in $$exts; do \
		find $(BOOK_DIR) -name "*.$$ext" -delete; \
	done

# Clean everything including PDF for the selected book
clean-all: clean
	rm -f $(BOOK_DIR)/$(PROJECT).pdf
