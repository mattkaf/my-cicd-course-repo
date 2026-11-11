from pathlib import Path
from datetime import datetime
def main():
output_dir = Path("build")
output_dir.mkdir(exist_ok=True)
report_file = output_dir / "build_report.txt"
report_contents = [
"CI/CD Build Report",
"===================",
f"Generated at: {datetime.utcnow().isoformat()} UTC",
"",
"Project files:",
"- src/calculator.py",
"- tests/test_calculator.py",
"- .github/workflows/python-tests.yml",
"- scripts/generate_report.py",
"",
"Status: Build artifact created successfully."
]
report_file.write_text("\n".join(report_contents), encoding="utf-8")
print(f"Report written to {report_file}")
if __name__ == "__main__":
main()