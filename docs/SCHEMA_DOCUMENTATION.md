# Schema System Documentation

## Overview

The awesIO schemas have been completely redesigned to support **type-dependent validation**. This means that different component types (e.g., LEI soft kite vs. fixed wing) now have their own specific validation rules.

## Key Features

### 1. Type-Dependent Validation

Components validate different properties based on their `type` field:

**Example - Wing Types:**
- `LEI_soft_kite`: Requires `flattening_factor`, uses soft kite aerodynamics
- `fixed_wing`: Requires `wing_area_m2`, `chord_m`, `taper_ratio` - NO `flattening_factor`
- `rigid_wing`: Similar to fixed wing validation

**Example - Tether Types:**
- `non_conductive_composite` / `conductive_composite`: Requires `conductive` boolean
- `synthetic_rope`: Requires `linear_density_kg_m`
- `steel_cable`: Requires `wire_count`

**Example - Ground Station Types:**
- `pumping_ground_gen_station`: Requires `drum` (electric_winch), `generator`, optional `gearbox`, `storage`
- `rotary_ground_gen_station`: Requires `drum` (rotary_drum), `generator`
- `fly_gen_station`: Minimal requirements, mainly `storage`

### 2. Terrain Constraints with Azimuth Zones

The operational constraints schema now supports flexible terrain-based restrictions:

```yaml
terrain_constraints:
  description: Site-specific terrain restrictions
  azimuth_zones:
    - azimuth_range_deg: [0, 40]
      flight_allowed: true
      distance_restrictions:
        - distance_range_m: [0, 10]
          min_height_agl_m: 0
        - distance_range_m: [10, 50]
          min_height_agl_m: 70
        - distance_range_m: [50, 200]
          min_height_agl_m: 100
    
    - azimuth_range_deg: [40, 75]
      flight_allowed: false  # No-fly zone (e.g., building)
    
    - azimuth_range_deg: [75, 360]
      flight_allowed: true
      distance_restrictions:
        - distance_range_m: [0, 50]
          min_height_agl_m: 50
```

**Features:**
- Define unlimited azimuth zones in 360° around the system
- Each zone can be marked as flight allowed/prohibited
- Multiple distance-based height restrictions per zone
- Easy to add, remove, or modify zones without schema changes

## Schema Files

### system_schema.yml (NEW)

Main schema for airborne system configurations. Validates:
- Wing (LEI_soft_kite, ram_air_soft_kite, fixed_wing, rigid_wing)
- Bridle (LEI_soft_kite_bridle, ram_air_soft_kite_bridle, four_line_bridle, two_line_bridle)
- Control System (kite_control_unit, autopilot, manual_control)
- Tether (non_conductive_composite, conductive_composite, synthetic_rope, steel_cable)
- Ground Station (pumping_ground_gen_station, rotary_ground_gen_station, fly_gen_station)

### operational_constraints_schema.yml (UPDATED)

Validates operational constraints with:
- Wind envelope
- Flight envelope
- Tether constraints
- Cycle constraints (ground-gen specific)
- Turbine/Electrical constraints (fly-gen specific)
- Safety constraints
- Airspace constraints
- **Terrain constraints (NEW)** - azimuth-zone-based restrictions

### power_curves_schema.yml (UNCHANGED)

Validates power curve data.

### wind_resource_schema.yml (UNCHANGED)

Validates wind resource data.

## Testing

### Running Tests

```bash
# Run comprehensive schema validation tests
python tests/test_schemas.py
```

### Test Coverage

The test suite validates:
1. All example YAML files against their schemas
2. Type-dependent validation (wing types, tether types, etc.)
3. Terrain constraints with multiple azimuth zones
4. Component-specific property requirements

### Test Results

```
Total tests: 6
Passed: 6
Failed: 0
```

## Adding New Component Types

To add a new component type (e.g., a new wing type):

1. **Add the type to the enum:**
```yaml
type:
  type: string
  enum:
    - LEI_soft_kite
    - ram_air_soft_kite
    - fixed_wing
    - rigid_wing
    - your_new_type  # Add here
```

2. **Add conditional validation:**
```yaml
allOf:
  - if:
      properties:
        type:
          const: your_new_type
    then:
      properties:
        aerodynamics:
          $ref: "#/definitions/your_new_type_aerodynamics"
        structure:
          $ref: "#/definitions/your_new_type_structure"
```

3. **Define the type-specific schemas:**
```yaml
definitions:
  your_new_type_aerodynamics:
    type: object
    properties:
      # Your specific properties
```

## Usage Examples

### Validating a System Configuration

```python
from awesio.validator import validate

# Validate a system configuration
validate(
    input="examples/ground_gen/soft_kite_pumping_ground_gen_system.yml",
    schema_type="system_schema",
    restrictive=False
)
```

### Validating Operational Constraints

```python
from awesio.validator import validate

# Validate operational constraints with terrain zones
validate(
    input="examples/ground_gen/soft_kite_pumping_ground_gen_operational_constraints.yml",
    schema_type="operational_constraints_schema",
    restrictive=False
)
```

## Benefits of Type-Dependent Validation

1. **Accuracy**: Only validates properties relevant to each component type
2. **Flexibility**: Easy to add new types without breaking existing configurations
3. **Documentation**: The schema itself documents what properties each type requires
4. **Error Messages**: More specific validation errors guide users to correct issues
5. **Extensibility**: New types can be added with their own unique properties

## Migration Guide

### For LEI Soft Kites
- `flattening_factor` is now properly validated
- Soft kite-specific aerodynamics validated

### For Fixed/Rigid Wings
- No longer requires `flattening_factor`
- Requires `wing_area_m2` instead of `projected_surface_area_m2`
- Supports wing-specific properties (`chord_m`, `taper_ratio`, etc.)

### For Operational Constraints
- Add `system_type` to metadata (required)
- Ensure `note` is a string (not null)
- Can now add terrain_constraints with azimuth zones

## Schema Validation Flow

```
YAML File
    ↓
Load & Parse
    ↓
Identify Component Type
    ↓
Apply Type-Specific Schema
    ↓
Validate Properties
    ↓
Valid or Error
```

## Future Enhancements

Potential additions:
- Additional wing types (inflatable, membrane, etc.)
- More tether types (hybrid, multi-line)
- Environmental constraints (temperature, humidity)
- Obstacle detection zones
- Dynamic no-fly zones
