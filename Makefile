validate: validate_syntax validate_schema

package.json:
	npm install -g jsonlint

# Validate jsonld
validate_syntax: package.json
	grep -r  "@context" response_options | cut -d: -f1 | xargs -I {} jsonlint -q {}
	grep -r  "@context" schemas | cut -d: -f1 | xargs -I {} jsonlint -q {}

# you will need to install reproschema-py to run this one ( pip install reproschema )
validate_schema:
	reproschema -l DEBUG validate response_options
	reproschema -l DEBUG validate schemas
