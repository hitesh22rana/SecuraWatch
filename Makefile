.PHONY: dependencies-backend dependencies-frontend lint-backend lint-frontend format-backend format-frontend run-backend-dev run-client-dev run clean

dependencies-backend:
	@sh scripts/backend/dependencies.sh

dependencies-frontend:
	@sh scripts/frontend/dependencies.sh

lint-backend:
	@sh scripts/backend/lint.sh

lint-frontend:
	@sh scripts/frontend/lint.sh

format-backend:
	@sh scripts/backend/format.sh

format-frontend:
	@sh scripts/frontend/format.sh

run-backend-dev:
	@sh scripts/backend/run-dev.sh

run-client-dev:
	@sh scripts/frontend/run-dev.sh

run: clean
	@sh scripts/run.sh

clean:
	@docker-compose -f docker-compose.yml down --remove-orphans