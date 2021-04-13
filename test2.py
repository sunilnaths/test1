import yaml
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result, print_title
from nornir_utils.plugins.tasks.data import load_yaml
from nornir_jinja2.plugins.tasks import template_file
from nornir_netmiko.tasks import netmiko_send_config
from user_login import user_login
from nornir.core.filter import F


def load_vars(task1):
    data = task1.run(task=load_yaml, file='Var_Nornir.yaml')
    task1.host["facts"] = data.result
    print_result(data.result)
    basic_configuration(task1)


def basic_configuration(task1):
    r = task1.run(task=template_file, template="L2_VxLAN1.j2",
                  path='')
    task1.host["Var-Nornir.yaml"] = r.result
    vlan_output = task1.host["Var_Nornir.yaml"]
    vlan_send = vlan_output.splitlines()
    task1.run(task=netmiko_send_config, name="VLAN Commands",
              config_commands=vlan_send)


print_title("config")
result = nr.run(task=load_vars)
print_result(result)
