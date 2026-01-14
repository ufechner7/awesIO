from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from awesio.validator import validate

# List of airborne files to validate
AIRBORNE_FILES = [
    "examples/fly_gen/fixed_wing_fly_gen_airborne.yml",
    "examples/ground_gen/soft_kite_pumping_ground_gen_airborne.yml",
]

def main():
    base_dir = Path(__file__).parent.parent
    
    print("Validating airborne files:")
    print("=" * 60)
    
    all_passed = True
    for file_path in AIRBORNE_FILES:
        full_path = base_dir / file_path
        print(f"\n{file_path}")
        
        if not full_path.exists():
            print(f"  ✗ File not found")
            all_passed = False
            continue
        
        try:
            validate(
                input=full_path,
                schema_type="airborne_schema",
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
