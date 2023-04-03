# Changelog

## [Unreleased][]

[Unreleased]: https://github.com/chaostoolkit/chaostoolkit-addons/compare/0.8.5...HEAD

## [0.8.5][]

[0.8.5]: https://github.com/chaostoolkit/chaostoolkit-addons/compare/0.8.4...0.8.5

### Changed

* Make safeguard probe that got triggered available to review

## [0.8.4][]

[0.8.4]: https://github.com/chaostoolkit/chaostoolkit-addons/compare/0.8.3...0.8.4

### Changed

- `cancel_futures` is only support in Python 3.9+

## [0.8.3][]

[0.8.3]: https://github.com/chaostoolkit/chaostoolkit-addons/compare/0.8.2...0.8.3

### Changed

- Better management of ending the experiment

## [0.8.2][]

[0.8.2]: https://github.com/chaostoolkit/chaostoolkit-addons/compare/0.8.1...0.8.2

### Changed

- Indirection to the exeit function so we can override in tests

## [0.8.1][]

[0.8.1]: https://github.com/chaostoolkit/chaostoolkit-addons/compare/0.8.0...0.8.1

### Changed

- Switched to regular thread to check if must interrupted as the future
  executor is bit painful when it comes to exiting the program

## [0.8.0][]

[0.8.0]: https://github.com/chaostoolkit/chaostoolkit-addons/compare/0.7.0...0.8.0

### Changed

- Reworked how we trigger the actual exit call so that we never block the
  threads playing the safeguards. Now only one thread can trigger the exit.

## [0.7.0][]

[0.7.0]: https://github.com/chaostoolkit/chaostoolkit-addons/compare/0.6.0...0.7.0

### Changed

- Added a flag to know when the guardian was fully setup

## [0.6.0][]

[0.6.0]: https://github.com/chaostoolkit/chaostoolkit-addons/compare/0.5.0...0.6.0

### Changed

- No need for the safeguard Guardian class to be a thread-local

## [0.5.0][]

[0.5.0]: https://github.com/chaostoolkit/chaostoolkit-addons/compare/0.4.0...0.5.0

### Changed

- Allow for callback to use their own guardian instance in the safeguard control

## [0.4.0][]

[0.4.0]: https://github.com/chaostoolkit/chaostoolkit-addons/compare/0.3.0...0.4.0

### Added

- The control `chaosaddons.controls.repeat` to run an activity multiple times

## [0.3.0][]

[0.3.0]: https://github.com/chaostoolkit/chaostoolkit-addons/compare/0.2.0...0.3.0

### Added

- Validate probes in the safeguard control [#7][7], using the new
  `validate_control` capability of the chaostoolkit core
- Export control functions in module variable `__all__`

[7]: https://github.com/chaostoolkit/chaostoolkit-addons/issues/7

### Changed

- Requires Python 3.7+ to match Chaos Toolkit itself

## [0.2.0][]

[0.2.0]: https://github.com/chaostoolkit/chaostoolkit-addons/compare/0.1.3...0.2.0

### Changed

- Ensure to not replay safeguard with frequency once triggered

### Added

-  The `bypass` control to dynamically filter activities that should not be
   executed
-  The `idle` action/probe to pause experiments without blocking the process

## [0.1.3][]

[0.1.3]: https://github.com/chaostoolkit/chaostoolkit-addons/compare/0.1.2...0.1.3

### Changed

-   Ensure latests setuptools when releasing

## [0.1.2][]

[0.1.2]: https://github.com/chaostoolkit/chaostoolkit-addons/compare/0.1.1...0.1.2

### Added

-   pyproject.toml

## [0.1.1][]

[0.1.1]: https://github.com/chaostoolkit/chaostoolkit-addons/compare/0.1.0...0.1.1

### Added

-   MANIFEST.in

## [0.1.0][]

[0.1.0]: https://github.com/chaostoolkit/chaostoolkit-addons/tree/0.1.0

### Added

-   Initial release