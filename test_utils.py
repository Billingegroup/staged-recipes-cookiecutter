#!/usr/bin/env python3
from pathlib import Path

import pexpect

# This assumes you are running this from a directory called scratch/diffpy.utils
# where scratch is at the same level as dev in your tree.
cc_path = (Path.cwd()).resolve()
p = pexpect.spawn(f"cookiecutter {cc_path}")

p.expect("github_org .*")
p.sendline("diffpy")

p.expect("module_name .*")
p.sendline("diffpy.utils")

p.expect("repo_name .*")
p.sendline("diffpy.utils")

p.expect("version .*")
p.sendline("3.4.0")

p.expect("Select source.*")
p.sendline("1")

p.expect("minimum_supported_python_version .*")
p.sendline("3.10")

p.expect("project_short_description .*")
p.sendline("Shared utilities for diffpy packages.")

p.expect("project_full_description .*")
p.sendline("The diffpy.utils package provides functions for extracting array data from variously formatted text files and wx GUI utilities used by the PDFgui program. The package also includes an interpolation function based on the Whittaker-Shannon formula that can be used to resample a PDF or other profile function over a new grid.")

p.expect("recipe_maintainers .*")
p.sendline("sbillinge, Sparks29032, dragonyanglong, CJ-Wright, pavoljuhas")

p.expect("runtime_requirements .*")
p.sendline("numpy >= 1.3,")

p.expect("testing_requirements .*")
p.sendline("pytest, freezegun,")

p.expect("test_these_imports .*")
p.sendline("diffpy, diffpy.utils, diffpy.utils.parsers, diffpy.utils.tests")

# Runs until the cookiecutter is done; then exits.
p.interact()
