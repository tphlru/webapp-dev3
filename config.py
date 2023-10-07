from dynaconf import Dynaconf

Settings = Dynaconf(envvar_prefix="DYNACONF", settings_files=["settings.toml", ".secrets.toml"])
