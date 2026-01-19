# Quick Reference Guide - Schema System

## Running Tests

```bash
# Navigate to repository root
cd c:\Users\joren\Desktop\Thesis_local\awesIO

# Run all schema tests
python tests\test_schemas.py
```

## Validating Your Files

### Python API
```python
from awesio.validator import validate

# Validate system configuration
validate(
    input="your_system_config.yml",
    schema_type="system_schema"
)

# Validate operational constraints
validate(
    input="your_constraints.yml",
    schema_type="operational_constraints_schema"
)

# Validate power curves
validate(
    input="your_power_curves.yml",
    schema_type="power_curves_schema"
)

# Validate wind resource
validate(
    input="your_wind_resource.yml",
    schema_type="wind_resource_schema"
)
```

## Component Type Reference

### Wing Types
| Type | Required Fields | Specific Properties |
|------|----------------|-------------------|
| `LEI_soft_kite` | projected_surface_area_m2, span_m, aspect_ratio, mass_kg | `flattening_factor` |
| `ram_air_soft_kite` | projected_surface_area_m2, span_m, aspect_ratio, mass_kg | `flattening_factor` |
| `fixed_wing` | wing_area_m2, span_m, aspect_ratio, mass_kg | `chord_m`, `taper_ratio`, `dihedral_angle_deg`, `sweep_angle_deg` |
| `rigid_wing` | wing_area_m2, span_m, aspect_ratio, mass_kg | Same as fixed_wing |

### Tether Types
| Type | Required Fields | Specific Properties |
|------|----------------|-------------------|
| `non_conductive_composite` | length_m, diameter_m, density_kg_m3, max_tether_force_n | `conductive: false` |
| `conductive_composite` | length_m, diameter_m, density_kg_m3, max_tether_force_n | `conductive: true` |
| `synthetic_rope` | length_m, diameter_m, max_tether_force_n | `linear_density_kg_m` |
| `steel_cable` | length_m, diameter_m, max_tether_force_n | `wire_count` |

### Ground Station Types
| Type | Required Components | Specific Requirements |
|------|-------------------|---------------------|
| `pumping_ground_gen_station` | drum, generator | drum.type: `electric_winch` |
| `rotary_ground_gen_station` | drum, generator | drum.type: `rotary_drum` |
| `fly_gen_station` | structure | Minimal requirements |

## Terrain Constraints Template

```yaml
terrain_constraints:
  description: "Site-specific terrain restrictions"
  reference_point: "Ground station location"
  azimuth_reference: "True north (0 deg)"
  azimuth_zones:
    # Zone 1: Open area
    - azimuth_range_deg: [0, 90]
      flight_allowed: true
      distance_restrictions:
        - distance_range_m: [0, 50]
          min_height_agl_m: 0
        - distance_range_m: [50, 200]
          min_height_agl_m: 100
        - distance_range_m: [200, 500]
          min_height_agl_m: 150
    
    # Zone 2: No-fly zone (e.g., building)
    - azimuth_range_deg: [90, 120]
      flight_allowed: false
    
    # Zone 3: Restricted area
    - azimuth_range_deg: [120, 360]
      flight_allowed: true
      distance_restrictions:
        - distance_range_m: [0, 100]
          min_height_agl_m: 80
```

## Common Validation Errors & Fixes

### Error: "Additional properties are not allowed"
**Cause**: Property not defined in schema for that component type
**Fix**: Check if property is valid for that type, or add to schema if needed

### Error: "'type' is not one of ['LEI_soft_kite', ...]"
**Cause**: Invalid component type
**Fix**: Use one of the supported types from the reference tables above

### Error: "'system_type' is a required property"
**Cause**: Missing system_type in operational constraints metadata
**Fix**: Add system_type to metadata section

### Error: "None is not of type 'string'"
**Cause**: Field has null value instead of string
**Fix**: Provide a string value (can be empty string "" if needed)

### Error: "flattening_factor is unexpected"
**Cause**: Using flattening_factor with fixed_wing type
**Fix**: Remove flattening_factor (only for soft kites) or change wing type

## File Structure Requirements

### System Configuration
```yaml
metadata:
  name: "System Name"
  description: "Description"
  note: "Notes"
  awesIO_version: "0.1.0"
  schema: "system_schema.yml"

assembly:
  airborne_type: soft_kite | rigid_wing | hybrid
  generation_type: pumping_ground_gen | rotary_ground_gen | fly_gen

components:
  wing: { ... }
  tether: { ... }
  # Optional: bridle, control_system, ground_station
```

### Operational Constraints
```yaml
metadata:
  name: "Constraint Set Name"
  description: "Description"
  note: "Notes"
  awesIO_version: "0.1.0"
  schema: "operational_constraints_schema.yml"
  system_type: pumping_ground_gen | rotary_ground_gen | fly_gen

# Optional sections:
airspace_constraints: { ... }
terrain_constraints: { ... }
safety_constraints: { ... }
# etc.
```

## Schema Files Location

All schemas are located in:
```
src/awesio/schemas/
├── system_schema.yml
├── operational_constraints_schema.yml
├── power_curves_schema.yml
└── wind_resource_schema.yml
```

## Documentation Files

- [docs/SCHEMA_DOCUMENTATION.md](./SCHEMA_DOCUMENTATION.md) - Comprehensive guide
- [docs/SCHEMA_SUMMARY.md](./SCHEMA_SUMMARY.md) - Summary of changes
- This file - Quick reference

## Support

For issues or questions:
1. Check validation error message
2. Consult [SCHEMA_DOCUMENTATION.md](./SCHEMA_DOCUMENTATION.md)
3. Review example files in `examples/` directory
4. Run test suite to see working examples
