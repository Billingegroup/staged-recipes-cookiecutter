staged-recipes-cookiecutter
###########################

Cookiecutter for making conda-forge recipes.

Run with ``cookiecutter https://github.com/billingegroup/staged-recipes-cookiecutter``.

This can only be run with Python 3.11+ as it uses hashlib.

Background information on ``meta.yaml``
********************************************

A recipe is a folder that contains the files necessary to build a conda package, including
the ``meta.yaml`` file. The ``meta.yaml`` file contains information about dependencies,
the package version, the license, the documentation link, and the maintainer(s) of the
package.

In ``meta.yaml``, there are three important keywords under the ``requirements`` section: ``build``, ``host``, and ``run``.

- **Build dependencies** are used for compiling but are not needed on the host where the package will be used. Examples include compilers, CMake, Make, pkg-config, etc.

- **Host dependencies** are required during the building of the package. Examples include setuptools, pip, etc.

- **Run dependencies** are required during runtime. Examples include matplotlib-base, numpy, etc.

To avoid any confusion, there is a separate YAML section called ``build`` above the ``requirements`` section. This section is for setting up the entire operating system.

For more information, please refer to the official documentation `here <https://conda-forge.org/docs/maintainer/adding_pkgs/#build-host-and-run>`_.
