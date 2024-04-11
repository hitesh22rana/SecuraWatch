.PHONY: dependencies format-backend format-frontend lint lint-fix run-frontend-dev

dependencies:
	@sh scripts/dependencies.sh

format-backend:
	@sh scripts/format-backend.sh

format-frontend:
	@sh scripts/format-frontend.sh

lint:
	@sh scripts/lint.sh

lint-fix:
	@sh scripts/lint.sh --fix

run-frontend-dev:
	@sh scripts/frontend-dev.sh