.PHONY: dependencies format lint lint-fix

dependencies:
	@sh scripts/dependencies.sh

format:
	@sh scripts/format.sh

lint:
	@sh scripts/lint.sh

lint-fix:
	@sh scripts/lint.sh --fix