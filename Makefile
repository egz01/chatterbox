.PHONY: clean test_install

dist:
	@echo "building package..."
	@python3 -m build > /dev/null
	@echo "package built!"

install: dist
	@python3 -m pip install -qq openai
	@python3 -m pip install -qq dist/*.whl
	@python3 -m chatterbox.examples.academic_example "Just sending you this message to make sure the installation works..."

test_install:
	@mkdir -p temp_env
	@cp dist/*.whl temp_env
	@python3 -m venv temp_env/venv
	@echo "testing installation on virtual env..."
	@cp .env test_installation.sh temp_env
	@cd temp_env && ./test_installation.sh

clean:
	@rm -rf dist
	@rm -rf temp_env
	