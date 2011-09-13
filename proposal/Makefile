RST2LATEX = rst2latex.py
PDFLATEX = pdflatex

TARGET = proposal
TRASH  = $(TARGET).pdf \
         $(TARGET).tex $(TARGET).aux $(TARGET).log  $(TARGET).out \
         $(TARGET).maf $(TARGET).mtc $(TARGET).mtc0

.PHONY: all clean
.SECONDARY:

ifeq ($(shell which $(PDFLATEX)),)
$(error Missing Dependency - LaTeX)
endif

ifeq ($(shell which $(RST2LATEX)),)
$(error Missing Dependency - reStructured Text)
endif

all: $(TARGET).pdf

clean:
	$(RM) $(TRASH)

%.pdf: %.tex
	$(PDFLATEX) $<
	$(PDFLATEX) $<

%.tex: %.rst Makefile
	@# Explaination of options:
	@#   --use-latex-toc: uses LaTeX to generate a ToC with page numbers
	@#   --use-latex-docinfo: uses LaTeX to generate the title page
	@#   --documentclass=report: enables LaTeX title page
	@#   --latex-preamble='': use the default font instead of Times
	$(RST2LATEX) --use-latex-toc --use-latex-docinfo --documentclass=article --documentoptions=a4,titlepage --latex-preamble='' $< > $@
