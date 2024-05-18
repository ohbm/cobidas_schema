# you will need to install reproschema-py to run this one ( pip install reproschema )
validate:
	pre-commit run -a check-json
	reproschema -l DEBUG validate response_options
	reproschema -l DEBUG validate schemas
