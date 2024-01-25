#! /bin/bash
checkov -s -d sast/example1loader/ --framework sast_python  --repo-id cli/uniquereponame --prisma-api-url https://api3.prismacloud.io/ --skip-results-upload --external-checks-dir sast_rules
