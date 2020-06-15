# Chaos Toolkit Extension Template

[![Build Status](https://travis-ci.org/chaostoolkit/chaostoolkit-extension-template.svg?branch=master)](https://travis-ci.org/chaostoolkit/chaostoolkit-extension-template)
[![Requirements Status](https://requires.io/github/chaostoolkit/chaostoolkit-extension-template/requirements.svg?branch=master)](https://requires.io/github/chaostoolkit/chaostoolkit-extension-template/requirements/?branch=master)

This project should be used as a starting point to create activities, such as probes and actions, you can call from
your experiments through the Chaos Toolkit.

## Install

This package requires Python 3.5+

To be used from your experiment, this package must be installed in the Python
environment where [chaostoolkit][] already lives.

[chaostoolkit]: https://github.com/chaostoolkit/chaostoolkit

```
$ pip install chaostoolkit-<your extension name here>
```

## Usage

<Explain your probes and actions usage from the experiment.json here>

That's it!

Please explore the code to see existing probes and actions.

## Configuration

<Specify any extra configuration your extension relies on here>

## Test

To run the tests for the project execute the following:

```
$ pytest
```

## Contribute

If you wish to contribute more functions to this package, you are more than
welcome to do so. Please, fork this project, make your changes following the
usual [PEP 8][pep8] code style, sprinkling with tests and submit a PR for
review.

[pep8]: https://pycodestyle.readthedocs.io/en/latest/
