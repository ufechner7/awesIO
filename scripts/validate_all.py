from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from awesio.validator import validate

# Define all files to validate with their respective schemas
VALIDATIONS = [
    ("examples/fly_gen/fixed_wing_fly_gen_airborne.yml", "airborne_schema"),
    ("examples/ground_gen/soft_kite_pumping_ground_gen_airborne.yml", "airborne_schema"),
    ("examples/fly_gen/fly_gen_tether.yml", "tether_schema"),
    ("examples/ground_gen/ground_gen_tether.yml", "tether_schema"),
    ("examples/fly_gen/fly_gen_ground_station.yml", "ground_station_schema"),
    ("examples/ground_gen/ground_gen_ground_station.yml", "ground_station_schema"),
    ("examples/fly_gen/fly_gen_operational_constraints.yml", "operational_constraints_schema"),
    ("examples/ground_gen/ground_gen_operational_constraints.yml", "operational_constraints_schema"),
    ("examples/ground_gen/ground_gen_power_curves.yml", "power_curves_schema"),
    ("examples/wind_resource.yml", "wind_resource_schema"),
]

def main():
    base_dir = Path(__file__).parent.parent
    
    print("Validating all files:")
    print("=" * 60)
    
    all_passed = True
    for file_path, schema_type in VALIDATIONS:
        full_path = base_dir / file_path
        print(f"\n{file_path}")
        
        if not full_path.exists():
            print(f"  ✗ File not found")
            all_passed = False
            continue
        
        try:
            validate(
                input=full_path,
                schema_type=schema_type,
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
