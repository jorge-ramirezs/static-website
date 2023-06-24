#!/usr/bin/env python3
import os

import aws_cdk as cdk

from static_website.static_website_stack import StaticWebsiteStack


app = cdk.App()
StaticWebsiteStack(app, "StaticWebsiteStack",
                   )

app.synth()
