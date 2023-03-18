sync_depends:
	@echo "Syncing dependencies..."
	poetry update
	poetry export --without-hashes -f requirements.txt --output requirements.txt
