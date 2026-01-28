"""Configuration loading for logsift.

Configuration is read from ``~/.logsift.toml`` when present. Any keys
that are missing fall back to the built-in defaults below. The loader is
tolerant: a missing file yields the defaults, and unknown keys are
ignored so that older versions do not choke on newer settings.
"""

import os

try:
    import tomllib as _toml
except ModuleNotFoundError:  # Python < 3.11
    try:
        import tomli as _toml
    except ModuleNotFoundError:
        _toml = None

DEFAULT_CONFIG = {
    "format": "apache",
    "color": True,
    "top": 10,
    "timezone": "UTC",
}

CONFIG_FILENAME = ".logsift.toml"


def config_path():
    """Return the path to the user configuration file."""
    return os.path.join(os.path.expanduser("~"), CONFIG_FILENAME)


def load_config(path=None):
    """Load configuration, merged over the built-in defaults.

    If ``path`` is not given, ``~/.logsift.toml`` is used. A missing file
    returns a copy of :data:`DEFAULT_CONFIG` unchanged.
    """
    if path is None:
        path = config_path()

    config = dict(DEFAULT_CONFIG)

    if not os.path.isfile(path):
        return config

    if _toml is None:
        raise RuntimeError(
            "reading a config file requires Python 3.11+ or the 'tomli' "
            "package"
        )

    with open(path, "rb") as fh:
        data = _toml.load(fh)

    for key in DEFAULT_CONFIG:
        if key in data:
            config[key] = data[key]

    return config
