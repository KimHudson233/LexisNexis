# Lexis Nexis Setup

## Installs

Download and install Docker Desktop from:
https://docs.docker.com/desktop/setup/install/windows-install/

Install Git command line:
https://git-scm.com/install/windows

Create Github Repo:
https://github.com/KimHudson233/lexisnexis-setup


## Testing

Clone Repo to laptop:
	git clone https://github.com/KimHudson233/LexisNexis.git

Deploy localstack into Docker:
	docker run -p 4566:4566 --name Localstack -d localstack/localstack:4.13.1

Run the validation script to test localstack is working:
	pip install -r requirements.txt
	python validate.py
