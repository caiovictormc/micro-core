import ujson
import uos


class Config:

    # soon other formats
    SUPPORTED = ['config.json', 'settings.json', 'conf.json']

    def __init__(self):
        file_name = self._find_file()
        with open(file_name) as config_file:
            self._config = ujson.load(config_file)

    def _find_file(self):
        for supported in SUPPORTED:
            if supported in uos.listdir():
                return supported

    def get(self, option, default=None):
        if option in self._config.keys():
            return self._config[option]
        return default

    def __call__(self, *arg, **kwargs):
        return self.get(*arg, **kwargs)


# from microconf import conf
conf = Config()
