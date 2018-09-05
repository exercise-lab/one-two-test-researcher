.PHONY: clean
all: docs/one-two-test.md img/one-two-test.png
docs/one-two-test.md: docs/one-two-test.Rmd
docs/%.md: docs/%.Rmd
	cd docs/ && Rscript -e "rmarkdown::render('$(shell basename $<)', output_file = '$(shell basename $@)', output_format = 'github_document')"
img/one-two-test.png:
img/%.png: dot/%.gv
	dot -Tpng -o $@ $<
clean:
	rm img/*.png
	rm -rf docs/*_files docs/*_cache
