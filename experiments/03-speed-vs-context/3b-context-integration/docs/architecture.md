# Architecture Decision Records

## ADR-001: Error Handling Strategy
- All public functions must raise ValueError for invalid inputs
- Never return None silently on error
- Error messages must be descriptive and include the invalid value

## ADR-002: Naming Conventions
- Functions use snake_case
- Classes use PascalCase
- Constants use UPPER_SNAKE_CASE
- Private functions prefixed with underscore

## ADR-003: Type Safety
- All functions must have type hints
- Use Optional[] for nullable returns
- Avoid bare dict/list - prefer TypedDict or dataclass

## ADR-004: Documentation
- All public functions must have docstrings
- Include Args, Returns, Raises sections
- Examples in docstrings for complex functions
