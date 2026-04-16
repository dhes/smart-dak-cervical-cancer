#!/bin/bash
# Download the latest FHIR IG Publisher jar
mkdir -p input-cache
curl -L https://github.com/HL7/fhir-ig-publisher/releases/latest/download/publisher.jar -o input-cache/publisher.jar
