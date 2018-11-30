all: instructions-experimenter-setup.pdf instructions-experimenter.pdf instructions-experimenter-saddle-points-part2.pdf instructions-experimenter-cleanup.pdf

instructions-experimenter-setup.pdf: instructions-experimenter-setup.md
instructions-experimenter.pdf: instructions-experimenter.md
instructions-experimenter-saddle-points-part2.pdf: instructions-experimenter-saddle-points-part2.md
instructions-experimenter-cleanup.pdf: instructions-experimenter-cleanup.md
%.pdf: %.md
	pandoc -o $@ --template template.tex $<
