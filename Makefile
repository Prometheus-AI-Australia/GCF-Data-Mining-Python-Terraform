export PROJECT_NAME = gcf-data-mining
export ENVIRONMENT ?= dev

export INFRASTRUCTURE_DIR = src/infrastructure

##################
## Init Targets ##
##################

conda:
	conda env update -f environment.yaml \
		|| \
	conda create -n $(PROJECT_NAME) -f environment.yaml

terraform:
	terraform init \
		-backend-config=$(INFRASTRUCTURE_DIR)/configuration/$(ENVIRONMENT)/backend.tfvars \
		$(INFRASTRUCTURE_DIR)

init: conda terraform
init:
	mkdir -p .build/function

##################
## Util Targets ##
##################

environment.yaml:
	conda env export --no-builds > environment.yaml
.PHONY: environment.yaml

tests:
	python -m pytest tests/
.PHONY: tests

########################
## Deployment Targets ##
########################

clean:
	find src/ -type f -name "*.pyc" -delete

deploy: clean
deploy:
	terraform apply \
		-var-file=$(INFRASTRUCTURE_DIR)/configuration/$(ENVIRONMENT)/deployment.tfvars \
		$(INFRASTRUCTURE_DIR)

destroy:
	terraform destroy \
		-var-file=$(INFRASTRUCTURE_DIR)/configuration/$(ENVIRONMENT)/deployment.tfvars \
		$(INFRASTRUCTURE_DIR)