import os
import pandas as pd
import json
json_files = []
live_routers = []

def create_dockerun():
    os.system('rm -rf dockerrun.txt')
    os.system('docker ps > dockerrun.txt')

def read_and_convert():
    text_read = pd.read_fwf('dockerrun.txt')
    text_read.to_csv('dockerrun.csv')
    pd_readfile = pd.read_csv('dockerrun.csv')
    return pd_readfile

def create_json(f):
    for i in f['NAMES']:
         live_routers.append(i)
         os.system('rm -rf docker_json_{}'.format(i))
         os.system('docker inspect {} > docker_json_{}'.format(i,i))
         json_files.append('docker_json_{}'.format(i))

def extract_ip():
    for i,j in zip(json_files,live_routers):
        with open(i,'r') as file:
            json_file = json.load(file)
            print('Ip address for router {} - {}'.format(j,json_file[0]['NetworkSettings']['IPAddress']))
create_dockerun()
create_json(read_and_convert())
extract_ip()
