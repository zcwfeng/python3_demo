import os
import yaml

class CustomConfigParser(object):

    config_file = os.path.dirname(os.path.realpath(__file__)) + '/config.yaml'
    configs = yaml.load(open(config_file,'r'))
    @classmethod
    def get(cls, server='mysql.config',key=None):
        if not cls.configs:
            cls.configs = yaml.load(open(cls.config_file, 'r'))
        section = cls.configs.get(server, None)
        if section is None:
            raise NotImplementedError
        value = section.get(key, None)
        if value is None:
                raise NotImplementedError
        return value

if __name__ == '__main__':
    configs = CustomConfigParser()
    mysql_conn = configs.get(key='conn')
    print(mysql_conn)
