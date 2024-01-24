from yaml import dump, load
from yaml import SafeLoader, SafeDumper

data = load(stream, Loader=SafeLoader)

