validate: validate_syntax validate_schema

package.json:
	npm install jsonlint

# Validate jsonld
validate_syntax: package.json
	grep -r  "@context" response_options | cut -d: -f1 | xargs -I fname jsonlint -q fname
	grep -r  "@context" schemas | cut -d: -f1 | xargs -I fname jsonlint -q fname

# you will need to install reproschema-py to run this one ( pip install reproschema )
validate_schema:
	reproschema -l DEBUG validate response_options
	reproschema -l DEBUG validate schemas
