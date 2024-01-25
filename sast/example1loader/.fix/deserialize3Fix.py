from yaml import load as stevesawesomeloader
from yaml import SafeLoader

data = stevesawesomeloader(stream, Loader=SafeLoader)
