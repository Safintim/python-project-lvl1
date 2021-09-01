install:
	poetry install
brain-games:
	poetry run brain-games
clean-build:
	rm -rf dist
build:
	poetry build
publish:
	poetry publish --dry-run
publish-testpypi:
	poetry config repositories.testpypi https://test.pypi.org/legacy/
	poetry publish -r testpypi 
package-install:
	python3 -m pip install --user dist/*.whl
lint:
	poetry run flake8 brain_games