.PHONY: run-py run-rust audit-module-readmes lint format

# Prefer PATH when set on the command line (per prompt),
# otherwise fall back to TARGET for backward compatibility.
ifeq ($(origin PATH),command line)
RUN_PY_PATH := $(PATH)
else
RUN_PY_PATH := $(TARGET)
endif

# Run pytest for a single module
# Usage: make run-py PATH=modules/dsa/arrays/prefix-sum/python
run-py:
	@if [ -z "$(RUN_PY_PATH)" ]; then \
		echo "Usage: make run-py PATH=<path-to-python-dir>"; \
		exit 1; \
	fi
	pytest $(RUN_PY_PATH) -q

# Run cargo test for a single Rust crate
# Usage: make run-rust MANIFEST=modules/dsa/arrays/prefix-sum/rust/Cargo.toml
run-rust:
	@if [ -z "$(MANIFEST)" ]; then \
		echo "Usage: make run-rust MANIFEST=<path-to-Cargo.toml>"; \
		exit 1; \
	fi
	cargo test --manifest-path $(MANIFEST)

# Audit module README files for the engineering module shape.
# Usage: make audit-module-readmes
# Usage: make audit-module-readmes PATHS="modules/software-engineering/apis/api-contract-basics"
audit-module-readmes:
	python scripts/audit_module_readmes.py $(PATHS)

# Optional: lint Python with ruff
lint:
	ruff check .

# Optional: format Python with ruff
format:
	ruff format .
