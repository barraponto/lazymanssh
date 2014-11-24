import json
import click
from storm.__main__ import add as host_add

@click.command('lazymanssh')
@click.argument('IPs', type=click.File('rb'))
@click.option('--host', prompt=True, type=click.STRING,
              help='the hostname prefix for ~/.ssh/config')
@click.option('--user', prompt=True, type=click.STRING,
              help='the user for ssh logins')
@click.option('--key', prompt=True, type=click.Path(
              exists=True, dir_okay=False, resolve_path=True),
              help='the identity file for ssh logins')
def lazyness(ips, host, user, key):
    '''Generates ~.ssh/config host configurations for the given IPs'''
    ip_list = json.loads(''.join([n for n in ips]))
    for index, ip in enumerate(ip_list):
        host_add(host + str(index), user + '@' + ip, key)
