# Copyright (C) 2022 CVAT.ai Corporation
#
# SPDX-License-Identifier: MIT

from cvat.settings.production import *

ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_REQUIRED = True

if USE_ALLAUTH_SOCIAL_ACCOUNTS:
    SOCIALACCOUNT_GITHUB_ADAPTER = 'cvat.apps.iam.adapters.TestGitHubAdapter'
    SOCIALACCOUNT_GOOGLE_ADAPTER = 'cvat.apps.iam.adapters.TestGoogleAdapter'