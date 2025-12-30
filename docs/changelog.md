# Changelog

All notable changes to the HSA Digital Shoebox project will be documented in this file.

## [0.2.0] - 2025-12-30

### Added

- **Logging Framework**: Replaced all standard `print()` statements with a structured `logging` configuration for better audit trails and error tracking.
- **Dependency Management**: Created `pyproject.toml` to manage core dependencies like `pypdf >= 6.5.0`.
- **VS Code Integration**: Added `.vscode/launch.json` with proper `PYTHONPATH` support for local debugging.

### Changed

- **Project Refactoring**: Major restructuring of the file hierarchy, moving core logic into a dedicated `src/` directory.
- **Module Improvements**: Standardized imports and renamed `pdf_extractor.py` to align with package naming conventions.
- **Enhanced Error Handling**: Integrated `try-except` blocks within the main processing loop to ensure continuous execution during batch processing.

### Fixed

- **Path Resolution**: Resolved issues where the debugger could not locate the source files or the data directories.
- **Import Errors**: Fixed `ModuleNotFoundError` by correctly setting up package initialization in `__init__.py`.

## [0.1.0] - 2024-12-15

### Added

- Initial project layout and basic file structure.
- Basic PDF text extraction logic.
