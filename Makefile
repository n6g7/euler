.PHONY: test test-python test-go test-rust lint

test: test-python test-go test-rust

test-python:
	python3 -m pytest tests/ solutions/ --tb=short -q

test-go:
	@if find solutions -name '*_test.go' -print -quit | grep -q .; then \
		go test ./solutions/...; \
	else \
		echo "test-go: no Go tests found, skipping"; \
	fi

test-rust:
	@if [ -f Cargo.toml ]; then \
		cargo test; \
	else \
		echo "test-rust: no Cargo.toml found, skipping"; \
	fi

lint:
	flake8 .
