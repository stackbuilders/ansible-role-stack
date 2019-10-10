import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_stack_2_1_3_version(host):
    cmd = host.run('/root/stack-2.1.3/stack --version')
    assert cmd.rc == 0
    assert '2.1.3' in cmd.stdout


def test_stack_1_9_3_version(host):
    cmd = host.run('/root/stack-1.9.3/stack --version')
    assert cmd.rc == 0
    assert '1.9.3' in cmd.stdout
