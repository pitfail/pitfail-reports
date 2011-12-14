
RST2LATEX = rst2latex.py
PDFLATEX  = pdflatex
PS2PDF    = ps2pdf
INKSCAPE  = inkscape
CONVERT   = convert
PDF90     = pdf90
WSD       = ./wsd.py
DIA       = dia

TARGET = report3
TRASH  = $(TARGET).pdf \
         $(TARGET).tex $(TARGET).aux $(TARGET).log  $(TARGET).out \
         $(TARGET).maf $(TARGET).mtc $(TARGET).mtc0 $(PDF_OBJ)

WSD_IN = $(shell find -name '*.wsd')
DIA_IN = $(shell find -name '*.dia')

PDF_OBJ = $(WSD_IN:.wsd=.pdf)
PNG_OBJ = $(DIA_IN:.dia=.png)
	
RSTS = $(wildcard *.rst)

.PHONY: all clean wsds

all: $(TARGET).pdf
	
wsds: $(PDF_OBJ)

clean:
	$(RM) $(TRASH)

%.pdf : %.wsd
	$(WSD) $< $@

%.pdf: %.eps
	$(PS2PDF) $< $@

%.pdf: %.ps
	$(PS2PDF) $< $@

%-rotated90.pdf: %.pdf
	cd `dirname $<` && $(PDF90) `basename $<`

%.pdf: %.svg
	$(INKSCAPE) --export-pdf=$@ $<

%.pdf: %.tex $(PDF_OBJ) $(PNG_OBJ)
	$(PDFLATEX) $<
	$(PDFLATEX) $<
	$(PDFLATEX) $<

%.tex: %.rst $(RSTS) Makefile docutils.conf stylesheet.tex
	$(RST2LATEX) --traceback --config=docutils.conf --stylesheet-path=stylesheet.tex $< > $@
    
%.png: %.dia
	$(DIA) --export $@ $<

# vim: noexpandtab

