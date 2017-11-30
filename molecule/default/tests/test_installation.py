"""
Role tests
"""

import os
import pytest
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    """
    Ensure /etc/hosts file exists
    """

    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


@pytest.mark.parametrize('path,user,group,mode', [
    ('/opt/hadoop/etc/hadoop/core-site.xml', 'root', 'root', 0o600),
    ('/opt/hadoop/etc/hadoop/hdfs-site.xml', 'root', 'root', 0o600),
    ('/opt/hadoop/etc/hadoop/yarn-site.xml', 'root', 'root', 0o600),
    ('/opt/hadoop/etc/hadoop/slaves', 'root', 'root', 0o600),
])
def test_config_files(host, path, user, group, mode):
    """
    Ensure config files exists
    """

    current_file = host.file(path)
    assert current_file.exists
    assert current_file.user == user
    assert current_file.group == group
    assert current_file.mode == mode


def test_processes(host):
    """
    Do some process testing
    """

    proc_args = [p.args for p in host.process.filter(comm='java')]

    if 'master' in host.ansible('setup')['ansible_facts']['ansible_hostname']:
        assert len(proc_args) == 2
        assert len([arg for arg in proc_args if 'proc_namenode' in arg]) == 1
        assert len(
            [arg for arg in proc_args if 'proc_resourcemanager' in arg]) == 1
    else:
        assert len(proc_args) == 1
        assert 'proc_datanode' in proc_args[0]
