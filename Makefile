export PROJECT_NAME = gcf-data-mining
export ENVIRONMENT ?= dev

export INFRASTRUCTURE_DIR = src/infrastructure


init:
	conda env update -f environment.yaml \
		|| \
	conda create -n $(PROJECT_NAME) -f environment.yaml

	terraform init \
		-backend-config=$(INFRASTRUCTURE_DIR)/configuration/$(ENVIRONMENT)/backend.tfvars \
		$(INFRASTRUCTURE_DIR)


environment.yaml:
	conda env export --no-builds > environment.yaml
.PHONY: environment.yaml

tests:
	python -m pytest tests/
.PHONY: tests