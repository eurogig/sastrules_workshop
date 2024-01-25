#! /bin/bash
checkov -s -d sast/examplewebform/ --framework sast_python  --repo-id cli/uniquereponame2 --prisma-api-url https://api3.prismacloud.io/ --skip-results-upload --external-checks-dir sast_rules
