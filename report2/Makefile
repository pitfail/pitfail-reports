RST2LATEX = rst2latex.py
PDFLATEX = pdflatex
PS2PDF = ps2pdf
INKSCAPE = inkscape
CONVERT = convert

TARGET = report2
TRASH  = $(TARGET).pdf \
         $(TARGET).tex $(TARGET).aux $(TARGET).log  $(TARGET).out \
         $(TARGET).maf $(TARGET).mtc $(TARGET).mtc0

.PHONY: all clean
.SECONDARY:

all: $(TARGET).pdf

clean:
	$(RM) $(TRASH)

%.pdf: %.eps
	$(PS2PDF) $< $@

%.pdf: %.ps
	$(PS2PDF) $< $@

%.pdf: %.svg
	$(INKSCAPE) --export-pdf=$@ $<

%.pdf: %.tex
	$(PDFLATEX) $<
	$(PDFLATEX) $<

%.tex: %.rst Makefile docutils.conf stylesheet.tex
	$(RST2LATEX) --traceback --config=docutils.conf --stylesheet-path=stylesheet.tex $< > $@
