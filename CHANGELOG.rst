Change Log
----------

..
   All enhancements and patches to pytest-repo-health will be documented
   in this file.  It adheres to the structure of http://keepachangelog.com/ ,
   but in reStructuredText instead of Markdown (for ease of incorporation into
   Sphinx documentation and the PyPI description).
   
   This project adheres to Semantic Versioning (http://semver.org/).

.. There should always be an "Unreleased" section for changes pending release.

Unreleased
~~~~~~~~~~

3.1.1 - 2024-04-15
~~~~~~~~~~~~~~~~~~

* Adding python3.11 support.


3.0.2 - 2023-04-17
~~~~~~~~~~~~~~~~~~

* If a check is an ``async def``, but is not marked with
  ``@pytest.mark.asyncio``, raise a true error, not just a warning that can be
  lost in the logs.

* Correct packaging errors.


3.0.0 - 2022-10-13
~~~~~~~~~~~~~~~~~~

BREAKING CHANGE
_______________

* Dropped Python 3.7 support


2.2.4 - 2021-12-16
~~~~~~~~~~~~~~~~~~

Fixed
_____

* Allow matching remote URL for .github repo


2.2.3 - 2021-11-23
~~~~~~~~~~~~~~~~~~

No change.

2.2.2 - 2021-11-23
~~~~~~~~~~~~~~~~~~

Removed
_______

* Removed Python 3.6 support as it is reaching end of life in December 2021

2.1.0 - 2020-11-03
~~~~~~~~~~~~~~~~~~

Added
_____

* Added ability to set filename for checks metadata file. You can now give a file path after --repo-health-metadata flag

2.0.1 - 2020-08-12
~~~~~~~~~~~~~~~~~~

Fixed
_____

* Fixed uploads to PyPI from Travis CI

2.0.0 - 2020-08-12
~~~~~~~~~~~~~~~~~~

Removed
_______

* Removed support for Python 3.5.  Versions 3.5.3 and above will likely still work for now, but they are no longer being tested; this lets us upgrade some dependencies and avoid confusion when aiohttp fails to install under 3.5.2 and below.  Python 3.5 reaches EOL in 1 month anyway.

Fixed
_____

* Recent versions of github.py installed from source control are now supported (and recommended if you want to inspect a repository's code of conduct, as 0.5.0 has a bug that throws an exception when attempting this).
* Checks can now be run on a ``.github`` repository (the regular expression used to parse out the organization and repository names didn't work with this before)

1.1.1 - 2020-07-21
~~~~~~~~~~~~~~~~~~

Fixed
_____

* Gracefully handle errors in fetching data from GitHub

1.1.0 - 2020-07-16
~~~~~~~~~~~~~~~~~~

Added
_____

* New fixtures that allow checks to easily fetch information about a git
  repository: ``git_repo`` and ``git_origin_url``

* New fixtures that allow checks to easily fetch information from the GitHub API
  about the repository: ``github_client`` and ``github_repo``

1.0.0 - 2020-05-13
~~~~~~~~~~~~~~~~~~

Added
_____

* ``--repo-health-metadata`` option to collect metadata for each check and save it in a YAML file.

* Added the current timestamp to the output (under ``TIMESTAMP``)


0.1.0 - 2020-04-13
~~~~~~~~~~~~~~~~~~

Initial release.
