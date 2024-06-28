#!/usr/bin/env python

import {{ cookiecutter.module_name }}.tests

assert {{ cookiecutter.module_name }}.tests.test().wasSuccessful()
