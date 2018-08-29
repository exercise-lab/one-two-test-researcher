all: img/one-two-test-diachronic.png img/one-two-test-individual.png
img/one-two-test-diachronic.png:
img/one-two-test-individual.png:
img/%.png: dot/%.gv
	dot -Tpng -o $@ $<
docs/one-two-test.md: docs/one-two-test.Rmd
	cd docs/ && Rscript -e "rmarkdown::render('$(basename $<)', output_file = '$(basename $@)', output_format = 'github_document')"