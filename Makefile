# Execute the "targets" in this file with `make <target>` e.g., `make test`.
#
# You can also run multiple in sequence, e.g. `make clean lint test serve-coverage-report`

# build:
# 	bash run.sh build

clean:
	bash run.sh clean

help:
	bash run.sh help

install:
	bash run.sh install

generate-proj:
	bash run.sh generate-project

test:
	pytest -v tests/

# lint:
# 	bash run.sh lint

# lint-ci:
# 	bash run.sh lint:ci

# publish-prod:
# 	bash run.sh publish:prod

# publish-test:
# 	bash run.sh publish:test

# release-prod:
# 	bash run.sh release:prod

# release-test:
# 	bash run.sh release:test

# serve-coverage-report:
# 	bash run.sh serve-coverage-report

# test-ci:
# 	bash run.sh test:ci

# test-quick:
# 	bash run.sh test:quick

# test:
# 	bash run.sh run-tests

# test-wheel-locally:
# 	bash run.sh test:wheel-locally
