RST2LATEX = rst2latex.py
PDFLATEX = pdflatex
PS2PDF = ps2pdf
INKSCAPE = inkscape
CONVERT = convert

DA := Overview.pdf Model.pdf PriceFetching.pdf WebTrading.pdf \
      TwitterTrading.pdf Login.pdf Schema.pdf
DA := $(addprefix domain-analysis/,$(DA))

SSD := BuyStocks_SD.pdf SellStocks_SD.jpg ModifyLeague_SD.jpg \
       ViewLeague_SD.jpg ViewPortfolio_SD.jpg
SSD := $(addprefix ssd/,$(SSD))

POW := plan_of_work.pdf

TARGET = report1
TRASH  = $(TARGET).pdf \
         $(TARGET).tex $(TARGET).aux $(TARGET).log  $(TARGET).out \
	 $(TARGET).maf $(TARGET).mtc $(TARGET).mtc0 $(DA)

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

%.pdf: %.eps
	$(PS2PDF) $< $@

%.pdf: %.ps
	$(PS2PDF) $< $@

%.pdf: %.svg
	$(INKSCAPE) --export-pdf=$@ $<

report1.pdf : report1.tex $(DA) $(SSD) $(POW) UseCaseDiagram.pdf

%.pdf: %.tex
	$(PDFLATEX) $<
	$(PDFLATEX) $<

%.tex: %.rst Makefile docutils.conf stylesheet.tex
	@# Explaination of options:
	@#   --use-latex-toc: uses LaTeX to generate a ToC with page numbers
	@#   --use-latex-docinfo: uses LaTeX to generate the title page
	@#   --documentclass=report: enables LaTeX title page
	@#   --latex-preamble='': use the default font instead of Times
	@#   --traceback: Give Python stack traces
	$(RST2LATEX) --traceback --config=docutils.conf --stylesheet-path=stylesheet.tex $< > $@
