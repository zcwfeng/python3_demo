# pip install PyYaml
import os
import yaml
config_file = os.path.dirname(os.path.realpath(__file__)) + '/config.yaml'
configs = yaml.load(open(config_file,'r'))
conns = configs.get('mysql.config')['conn']
for k,v in conns.items():
    print(k,'====:',v)
