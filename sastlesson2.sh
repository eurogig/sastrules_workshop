#! /bin/bash
checkov -s -d sast/examplewebform/ --framework sast_python  --repo-id cli/uniquereponame2 --prisma-api-url "$PRISMA_API_URL" --skip-results-upload --external-checks-dir sast_rules
