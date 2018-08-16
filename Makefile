all: img/one-two-test-diachronic.png img/one-two-test-individual.png
img/one-two-test-diachronic.png:
img/one-two-test-individual.png:
img/%.png: dot/%.gv
	dot -Tpng -o $@ $<
