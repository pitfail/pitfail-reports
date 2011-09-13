RST2PDF = rst2pdf
RST2LATEX = rst2latex.py
PDFLATEX = pdflatex

TARGET = proposal
TRASH = $(TARGET).pdf $(TARGET).tex $(TARGET).aux

.PHONY: all all-rst all-latex clean
.SECONDARY:

# Use LaTeX as an intermediate if it is available.
ifeq ($(shell which pdflatex),)
all: all-rst
else
all: all-latex
endif

all-rst: $(TARGET).pdf

all-latex: $(TARGET).tex
	$(PDFLATEX) $^
	$(PDFLATEX) $^

clean:
	$(RM) $(TRASH)

%.pdf: %.rst
	$(RST2PDF) $^

%.tex: %.rst
	$(RST2LATEX) $^ > $@
