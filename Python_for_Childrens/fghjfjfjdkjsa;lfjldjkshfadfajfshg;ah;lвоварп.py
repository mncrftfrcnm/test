import netmiko
import yaml
config_commands = ["logging 10.255.255.1", "logging buffered 20010", "no logging console"]
with open("devices.yml") as f:
    devices = yaml.safe_load(f)
    
    for dev in devices:
        ssh = netmiko.ConnectHandler(**dev)
        tre = ssh.send_config_set(config_commands)
#        print(tre)