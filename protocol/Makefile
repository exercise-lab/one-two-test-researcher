all: 0-setup.pdf 1-instructions.pdf 2-saddle-points-part2.pdf 3-cleanup.pdf
0-setup.pdf: 0-setup.md
1-instructions.pdf: 1-instructions.md
2-saddle-points-part2.pdf: 2-saddle-points-part2.md
3-cleanup.pdf: 3-cleanup.md
%.pdf: %.md
	pandoc -o $@ --template template.tex $<
