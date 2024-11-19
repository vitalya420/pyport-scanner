import ipaddress
import socket
from typing import Iterable


def _is_ip_addr(dest: str):
    try:
        return not not ipaddress.ip_address(dest)
    except ValueError:
        return False


def _is_network(dest):
    try:
        return not not ("/" in dest and ipaddress.ip_network(dest))
    except ValueError:
        return False


def _prepare(dest, ports):
    retval = []
    if isinstance(ports, int):
        retval = [f"{dest}:{ports}"]
    elif isinstance(ports, Iterable):
        for port in ports:
            retval.append(f"{dest}:{port}")
    return retval


def _syn_single_dest(destination, ports, timeout, callback, callback_opened_only):
    if not _is_ip_addr(destination):
        destination = socket.gethostbyname(destination)
    print("single dest", _prepare(destination, ports))


def _syn_miltiply_dest(destinations, ports, timeout, callback, callback_opened_only):
    all_ = []
    if isinstance(destinations, str) and _is_network(destinations):
        network = ipaddress.ip_network(destinations)
        for ip in network.hosts():
            all_.extend(_prepare(ip, ports))
    print(all_)


def syn_scan(dest, ports, timeout=5.0, callback=None, callback_opened_only=True):
    if (isinstance(dest, str) or isinstance(dest, int)) and "/" not in dest:
        return _syn_single_dest(dest, ports, timeout, callback, callback_opened_only)
    else:
        return _syn_miltiply_dest(dest, ports, timeout, callback, callback_opened_only)
