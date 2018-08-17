#!/usr/bin/python

import os
import json
import sys

# Reading the input payload from STDIN
payload = sys.stdin.read()
# Parse the payload
requested_vars = json.loads(payload)

secrets = {}
for var_name in requested_vars["secrets"]:
    environment_vars[var_name] = { "value": os.environ[var_name], "error": None }

print json.dumps(environment_vars)
