# Code Style Guide

## Error Handling
- Prefer explicit ValueError/TypeError over silent failures
- Always validate inputs at function boundaries
- Use guard clauses (early return) over nested if-else

## Return Values
- Functions should have a single, predictable return type
- Avoid returning different types based on conditions
- Use Optional[] only when None is a meaningful result, not an error

## Constants
- Define at module level, not inside functions
- Group related constants together
- Add comments explaining non-obvious values
