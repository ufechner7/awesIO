from pathlib import Path
import sys
import argparse

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from awesio.validator import validate

def main():
    parser = argparse.ArgumentParser(description="Validate wind resource YAML files")
    parser.add_argument(
        "file",
        nargs="?",
        default=None,
        help="Path to wind resource YAML file to validate"
    )
    parser.add_argument(
        "--restrictive",
        action="store_true",
        help="Enable restrictive validation (no additional properties allowed)"
    )
    
    args = parser.parse_args()
    
    if args.file:
        wind_resource_file = Path(args.file)
    else:
        wind_resource_file = Path(__file__).parent.parent / "examples" / "AWES_Ontology" / "wind_resource.yml"
    
    if not wind_resource_file.exists():
        print(f"Error: File {wind_resource_file} not found.")
        sys.exit(1)
    
    print(f"Validating {wind_resource_file}...")
    
    try:
        validate(
            input=wind_resource_file,
            schema_type="wind_resource_schema",
            restrictive=args.restrictive
        )
        print("Validation successful!")
    except Exception as e:
        print(f"Validation failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
