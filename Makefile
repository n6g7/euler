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
	@if find solutions -name '*.rs' -print -quit | grep -q .; then \
		python3 -c "from cli.run import _sync_cargo_toml; \
			import glob, os; \
			[_sync_cargo_toml(f) for f in \
			glob.glob('solutions/level*/problem*.rs')]" && \
		cargo test; \
	else \
		echo "test-rust: no Rust solutions found, skipping"; \
	fi

lint:
	flake8 .
