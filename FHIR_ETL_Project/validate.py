import requests
import json
from pathlib import Path

FHIR_SERVER_URL = "http://137.184.71.65:8080/fhir"
DATA_DIR = Path("data")

def validate_resource(file_name, resource_type):
    file_path = DATA_DIR / f"{file_name}.json"
    with open(file_path) as f:
        resource = json.load(f)

    response = requests.post(
        f"{FHIR_SERVER_URL}/{resource_type}/$validate",
        headers={"Content-Type": "application/fhir+json"},
        json=resource
    )

    print(f"\nValidating {resource_type}: {file_name}.json")
    print("HTTP Status:", response.status_code)

    outcome = response.json()
    issues = outcome.get("issue", [])
    errors = [i for i in issues if i["severity"] in ["error", "fatal"]]
    warnings = [i for i in issues if i["severity"] == "warning"]

    if not errors and not warnings:
        print("Validated successfully. No issues found.")
    else:
        for issue in errors + warnings:
            print(f"\n{issue['severity'].upper()} - {issue['diagnostics']}")
            if "location" in issue:
                print("Location:", ", ".join(issue["location"]))

if __name__ == "__main__":
    # Match filenames from Task 1
    validate_resource("patient_details_payload", "Patient")
    validate_resource("parent_condition_payload", "Condition")
    validate_resource("child_condition_payload", "Condition")