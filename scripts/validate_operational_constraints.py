from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from awesio.validator import validate

# List of operational constraints files to validate
OPERATIONAL_CONSTRAINTS_FILES = [
    "examples/fly_gen/fly_gen_operational_constraints.yml",
    "examples/ground_gen/ground_gen_operational_constraints.yml",
]

def main():
    base_dir = Path(__file__).parent.parent
    
    print("Validating operational constraints files:")
    print("=" * 60)
    
    all_passed = True
    for file_path in OPERATIONAL_CONSTRAINTS_FILES:
        full_path = base_dir / file_path
        print(f"\n{file_path}")
        
        if not full_path.exists():
            print(f"  ✗ File not found")
            all_passed = False
            continue
        
        try:
            validate(
                input=full_path,
                schema_type="operational_constraints_schema",
                restrictive=False
            )
            print(f"  ✓ Valid")
        except Exception as e:
            print(f"  ✗ Invalid: {e}")
            all_passed = False
    
    print("\n" + "=" * 60)
    if all_passed:
        print("All files validated successfully!")
        sys.exit(0)
    else:
        print("Some files failed validation.")
        sys.exit(1)

if __name__ == "__main__":
    main()
