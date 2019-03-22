import yaml
import os


class Config:
    def __init__(self):
        path = os.path.dirname(os.path.abspath(__file__))
        path = path.split("/")[:-1]
        path = "/".join(path)
        with open(os.path.join(path, 'config.yaml')) as fp:
            self.config = yaml.load(fp)

    def __getattr__(self, attr):
        return self.config[attr]
        