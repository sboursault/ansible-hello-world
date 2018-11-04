import os
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_index_html_content(host):
    expected_content = open('tests/expected/index.html.txt', 'r').read()
    index_html = host.file('/usr/share/nginx/html/index.html')
    assert index_html.content_string == expected_content
