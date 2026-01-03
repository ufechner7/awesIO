from pathlib import Path

schemaPath = Path(__file__).parent


def schema_validation_error_formatter(errors, schema_id):
    errors = list(errors)
    if errors:
        error_messages = []
        for error in errors:
            path = ".".join(str(p) for p in error.path) if error.path else "root"
            error_messages.append(f"  - At '{path}': {error.message}")
        
        full_message = f"Validation failed for schema '{schema_id}':\n" + "\n".join(error_messages)
        raise ValueError(full_message)
