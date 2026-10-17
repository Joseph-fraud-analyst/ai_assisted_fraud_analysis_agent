import json
from pathlib import Path
from evaluator import evaluate

ROOT = Path(__file__).resolve().parents[1]
tests_path = ROOT / "data" / "test_cases.json"
output_path = ROOT / "output" / "evaluation_results.json"
cases = json.loads(tests_path.read_text(encoding="utf-8"))
results = [evaluate(case) for case in cases]
output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_text(json.dumps(results, indent=2), encoding="utf-8")
passed = sum(1 for r in results if r["passed"])
print(f"Evaluation results: {passed}/{len(results)} passed")
for result in results:
    status = "PASS" if result["passed"] else "FAIL"
    print(f"{status} {result['test_id']} [{result['category']}]")
    for issue in result["issues"]:
        print(f"  - {issue}")
print(f"Results written to: {output_path}")
