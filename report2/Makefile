RST2LATEX = rst2latex.py
PDFLATEX = pdflatex
PS2PDF = ps2pdf
INKSCAPE = inkscape
CONVERT = convert
PDF90 = pdf90

TARGET = report2
TRASH  = $(TARGET).pdf \
         $(TARGET).tex $(TARGET).aux $(TARGET).log  $(TARGET).out \
         $(TARGET).maf $(TARGET).mtc $(TARGET).mtc0 $(PDF_OBJ)

PDF_OBJ = plan_of_work/pow_report2-rotated90.pdf component_diagram.pdf schema/Schema.pdf
PDF_DEP = $(PDF_OBJ)


.PHONY: all clean

all: $(TARGET).pdf

clean:
	$(RM) $(TRASH) $(PDF_OBJ)

plan_of_work/pow_report2.pdf : plan_of_work/pow_report2.mpp
	echo "$@ depends on $< but $@ was not updated"
	false

%.pdf: %.eps
	$(PS2PDF) $< $@

%.pdf: %.ps
	$(PS2PDF) $< $@

%-rotated90.pdf: %.pdf
	cd `dirname $<` && $(PDF90) `basename $<`

%.pdf: %.svg
	$(INKSCAPE) --export-pdf=$@ $<

%.pdf: %.tex $(PDF_DEP)
	$(PDFLATEX) $<
	$(PDFLATEX) $<

%.tex: %.rst Makefile docutils.conf stylesheet.tex
	$(RST2LATEX) --traceback --config=docutils.conf --stylesheet-path=stylesheet.tex $< > $@
