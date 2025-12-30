# Project Roadmap

## Phase 1: Core Engine (Complete)

- [x] Basic project scaffolding and file structure.
- [x] Refactor code into `src/` package structure.
- [x] Transition from print to professional logging.

## Phase 2: Configuration & Robustness (Active)

- [ ] **Dynamic Configuration**: Implement `config.yaml` to remove hardcoded paths.
- [ ] **Data Path Toggling**: Enable seamless switching between `data/sample` and `data/raw`.
- [ ] **Exception Resilience**: Improve extraction logic to handle malformed or encrypted PDFs.

## Phase 3: Integration & Expansion (Planned)

- [ ] **Cigna Integration**: Add support for automated downloading and processing of receipts directly from the Cigna portal.
- [ ] **Database Integration**: Log extracted medical expenses (Date, Amount, Provider) into a local SQLite database or CSV for tracking.
- [ ] **Fidelity Reconciliation**: Cross-reference extracted receipts with your [Health Savings Account](https://digital.fidelity.com/ftgw/digital/portfolio/summary) (currently at **$45,770.64**) to identify unclaimed reimbursements.

## Phase 4: Intelligence

- [ ] **OCR Support**: Integrate Tesseract or similar for non-searchable image-based PDFs.
- [ ] **Categorization**: Auto-categorize expenses into "Vision," "Dental," or "Medical" based on provider metadata.
