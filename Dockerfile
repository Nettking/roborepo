# Use a full TeX Live distribution (includes most packages)
FROM blang/latex:ctanfull

# Set working directory inside container
WORKDIR /data

# Default command: build PDF automatically
ENTRYPOINT ["latexmk", "-pdf", "-interaction=nonstopmode", "-halt-on-error"]
