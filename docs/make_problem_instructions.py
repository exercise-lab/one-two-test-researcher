from pathlib import Path
import subprocess
import pypandoc

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--language", "-l", required=True)
    parser.add_argument("--problem", "-p", required=True)
    parser.add_argument("--open-after", "-o", action="store_true")
    args = parser.parse_args()
    docs_dir = Path(__file__).absolute().parent
    problem_dir = docs_dir.parent / f"problems/{args.language}/exercises/{args.problem}"
    readme = str(problem_dir / "README.md")
    output = f"instructions-{args.language}-{args.problem}.pdf"
    pypandoc.convert_file(readme, "pdf", outputfile=output, extra_args=["--template=template.tex"])

    if args.open_after:
        subprocess.call(["open", output])



