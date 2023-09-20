import configparser
import os
import framework.text.path as opath

def loadConfig(app: str, config_file: str):
    if not os.path.exists(f"{opath.get.openpy_path()}/configs/{app}"): os.mkdir(f"{opath.get.openpy_path()}/configs/{app}") 
    if not os.path.exists(f'{opath.get.openpy_path()}/configs/{app}/{config_file}.ini'): open(f"{opath.get.openpy_path()}/configs/{app}/{config_file}.ini", "w")

    parser = configparser.ConfigParser()
    return parser.read(f"{opath.get.openpy_path()}/configs/{app}/{config_file}.ini")

def saveConfig(app: str, config_file: str, config: configparser.ConfigParser):
    if not os.path.exists(f"{opath.get.openpy_path()}/configs/{app}"): os.mkdir(f"{opath.get.openpy_path()}/configs/{app}") 
    if not os.path.exists(f'{opath.get.openpy_path()}/configs/{app}/{config_file}.ini'): open(f"{opath.get.openpy_path()}/configs/{app}/{config_file}.ini", 'w')
    
    with open(f'{opath.get.openpy_path()}/configs/{app}/{config_file}.ini', 'w') as file: config.write(file)