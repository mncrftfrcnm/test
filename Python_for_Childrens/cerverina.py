import yaml
import netmiko
def send_show_command(device,command):
    ssh = netmiko.ConnectHandler(**device)
    return ssh.send_command(command)
if __name__ == "__main__":
    command = input('command: ')
    file = input('file.yaml: ')
    with open(file) as f:
        devices = yaml.safe_load(f)

    for dev in devices:
        print('\n'+send_show_command(dev, command))
