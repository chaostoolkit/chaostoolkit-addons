from importlib.metadata import version, PackageNotFoundError

__all__ = ["__version__"]


try:
    __version__ = version("chaostoolkit-addons")
except PackageNotFoundError:  # pragma: no cover
    __version__ = 'unknown'
