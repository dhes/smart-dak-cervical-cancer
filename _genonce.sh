#!/bin/bash
# Run the FHIR IG Publisher once

# Pre-build: render decision tables from DMN
echo "Rendering decision tables from DMN..."
python3 render-decision-tables.py

# Run the publisher
publisher_jar=input-cache/publisher.jar
if [ ! -f "$publisher_jar" ]; then
  echo "Publisher not found. Run ./_updatePublisher.sh first."
  exit 1
fi
java -jar "$publisher_jar" -ig . "$@"
