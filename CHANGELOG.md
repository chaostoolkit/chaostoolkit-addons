# Changelog

## [Unreleased][]

[Unreleased]: https://github.com/chaostoolkit/chaostoolkit-addons/compare/0.3.0...HEAD

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