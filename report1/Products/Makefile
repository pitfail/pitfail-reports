
# vim: noexpandtab

PNGS = exchange-1.png exchange-2.png exchange-3.png

all: $(PNGS)

%.png: %.dot
	dot -Tpng -o $@ $<

