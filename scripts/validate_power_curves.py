from pathlib import Path
import sys
import argparse

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from awesio.validator import validate

def main():
    parser = argparse.ArgumentParser(description="Validate power curves YAML files")
    parser.add_argument(
        "file",
        nargs="?",
        default=None,
        help="Path to power curves YAML file to validate"
    )
    parser.add_argument(
        "--restrictive",
        action="store_true",
        help="Enable restrictive validation (no additional properties allowed)"
    )
    
    args = parser.parse_args()
    
    if args.file:
        power_curves_file = Path(args.file)
    else:
        power_curves_file = Path(__file__).parent.parent / "examples" /  "power_curves.yml"
    
    if not power_curves_file.exists():
        print(f"Error: File {power_curves_file} not found.")
        sys.exit(1)
    
    print(f"Validating {power_curves_file}...")
    
    try:
        validate(
            input=power_curves_file,
            schema_type="power_curves_schema",
            restrictive=args.restrictive
        )
        print("Validation successful!")
    except Exception as e:
        print(f"Validation failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
