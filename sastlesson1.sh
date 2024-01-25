#! /bin/bash
checkov -s -d sast/example1loader/ --framework sast_python  --repo-id cli/uniquereponame --prisma-api-url "$PRISMA_API_URL" --skip-results-upload --external-checks-dir sast_rules
