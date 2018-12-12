import os
from pathlib import Path
import subprocess
import pandas

if __name__ == "__main__":
    python_solutions = Path("solutions/python")
    for solution_dir in python_solutions.iterdir():
        if not solution_dir.is_dir():
            continue

        subj_id = solution_dir.name
        subprocess.call(f"pipenv run pytest {solution_dir} --excelreport={subj_id}.xls",
                        shell=True)

    excel_reports = Path(".").glob("*.xls")
    test_data = []
    for report in excel_reports:
        data = pandas.read_excel(report)
        data.insert(0, "subj_id", report.stem)
        test_data.append(data)
        os.remove(report)
    all_data = pandas.concat(test_data)

    data_dir = Path("data")
    if not data_dir.is_dir():
        data_dir.mkdir()
    all_data.to_csv("data/saddle-points-python.csv", index=False)
