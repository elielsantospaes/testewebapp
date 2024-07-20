#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "3137b764-fbcd-4d66-96ca-fd4bb6bf34c7")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "ptf8Q~QGEwtmKb~8dacA-JfE7XUDPXYPOIV41dyi")
