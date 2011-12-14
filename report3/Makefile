
RST2LATEX = rst2latex.py
PDFLATEX  = pdflatex
PS2PDF    = ps2pdf
INKSCAPE  = inkscape
CONVERT   = convert
PDF90     = pdf90
WSD       = ./wsd.py
DIA       = dia
SEQDIAG   = seqdiag
RUBBER    = rubber

TARGET = report3
TRASH  = $(TARGET).pdf \
         $(TARGET).tex $(TARGET).aux $(TARGET).log  $(TARGET).out \
         $(TARGET).maf $(TARGET).mtc $(TARGET).mtc0 $(PDF_OBJ) $(SVG_OBJ)

PNG_IN = $(wildcard figures/FB/*.png)
WSD_IN = $(shell find . -name '*.wsd')
DIA_IN = $(shell find . -name '*.dia')
SVG_IN = use_case_diagram.svg figures/domain/original-domain.svg figures/component_diagram.svg

SVG_OBJ = $(DIA_IN:.dia=.svg)
PDF_OBJ = $(SVG_OBJ:.svg=.pdf) $(SVG_IN:.svg=.pdf) $(WSD_IN:.wsd=.pdf)

RSTS = $(wildcard *.rst)

.PHONY: all clean wsds pngs

all: $(TARGET).pdf

wsds: $(PDF_OBJ)

pngs: $(PNG_OBJ)

clean:
	$(RM) $(TRASH)

%.pdf : %.wsd
	$(WSD) pdf $< $@

%.svg : %.wsd
	$(WSD) svg $< $@

%.svg : %.diag
	$(SEQDIAG) $< $@

%.pdf: %.eps
	$(PS2PDF) $< $@

%.pdf: %.ps
	$(PS2PDF) $< $@

%-rotated90.pdf: %.pdf
	cd "`dirname $<`" && $(PDF90) "`basename $<`"

%.pdf: %.svg
	$(INKSCAPE) --export-pdf=$@ $<

%.pdf: %.tex $(PDF_OBJ)
	$(RUBBER) --warn refs --pdf report3

%.tex: %.rst $(RSTS) Makefile docutils.conf stylesheet.tex
	$(RST2LATEX) --traceback --config=docutils.conf --stylesheet-path=stylesheet.tex $< > $@

%.svg: %.dia
	$(DIA) --export=$@ $<

# vim: noexpandtab

