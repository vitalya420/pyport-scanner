# scanner.pyi
from dataclasses import dataclass
from typing import Callable, Iterable, List, Optional, Union, Sequence, overload

_ScanDestination = Union[str, int]  # IPv4, IPv6, IP as Decimal, ip/mask, or host
_ScanDestinations = Sequence[_ScanDestination]  # Few destinantions
_PortRange = Union[int, Sequence[int], Iterable[int]]

Callback = Callable[[str, int, Optional[bool]], None]

@dataclass
class ScanResult:
    ip: str
    port: int
    opened: bool
    host: Optional[str] = None  # If it was host scan

@overload
def syn_scan(
    dest: _ScanDestination,
    ports: int,
    timeout: Optional[float] = 5.0,
    callback: Optional[Callback] = None,
    callback_opened_only: bool = True,
) -> List[ScanResult]:
    """
    Perform a SYN scan on a single destination and a single port.

    This version of the `syn_scan` function is designed for scanning a single IP address (IPv4 or IPv6),
    hostname, or network address with a subnet mask (e.g., '192.168.0.1/24') for a single port.

    Args:
        dest (_ScanDestination):
            A single destination IP address (IPv4 or IPv6), network address with a mask (e.g., '192.168.0.1/32'),
            or hostname (e.g., 'example.com') to scan.
        ports (int):
            The single port number to scan.
        timeout (Optional[float], optional):
            The timeout in seconds to wait for a response. Defaults to 5.0 seconds.
        callback (Optional[Callback], optional):
            A function to be called when a SYN/ACK response is received. This function should accept the destination,
            port, and an optional boolean indicating whether the port is open.
        callback_opened_only (bool, optional):
            If True, the callback will only be called for open ports. Defaults to True.

    Returns:
        List[ScanResult]:
            A list containing the scan result for the single port on the given destination.
    """

@overload
def syn_scan(
    dest: _ScanDestinations,
    ports: int,
    timeout: Optional[float] = 5.0,
    callback: Optional[Callback] = None,
    callback_opened_only: bool = True,
) -> List[ScanResult]:
    """
    Perform a SYN scan on multiple destinations and a single port.

    This version of the `syn_scan` function is designed for scanning multiple destination IP addresses (IPv4 or IPv6),
    hostnames, or network addresses with subnet masks (e.g., '192.168.0.1/24') for a single port.

    Args:
        dest (_ScanDestinations):
            A sequence of destination IP addresses (IPv4 or IPv6), network addresses with a mask, or hostnames to scan.
        ports (int):
            The single port number to scan.
        timeout (Optional[float], optional):
            The timeout in seconds to wait for a response. Defaults to 5.0 seconds.
        callback (Optional[Callback], optional):
            A function to be called when a SYN/ACK response is received. This function should accept the destination,
            port, and an optional boolean indicating whether the port is open.
        callback_opened_only (bool, optional):
            If True, the callback will only be called for open ports. Defaults to True.

    Returns:
        List[ScanResult]:
            A list containing the scan results for the single port across multiple destinations.
    """

@overload
def syn_scan(
    dest: _ScanDestination,
    ports: _PortRange,
    timeout: Optional[float] = 5.0,
    callback: Optional[Callback] = None,
    callback_opened_only: bool = True,
) -> List[ScanResult]:
    """
    Perform a SYN scan on a single destination and multiple ports.

    This version of the `syn_scan` function is designed for scanning a single IP address (IPv4 or IPv6),
    hostname, or network address with a subnet mask (e.g., '192.168.0.1/24') for multiple ports.

    Args:
        dest (_ScanDestination):
            A single destination IP address (IPv4 or IPv6), network address with a mask (e.g., '192.168.0.1/32'),
            or hostname (e.g., 'example.com') to scan.
        ports (_PortRange):
            A sequence of port numbers, a range of ports, or a single port number to scan.
        timeout (Optional[float], optional):
            The timeout in seconds to wait for a response. Defaults to 5.0 seconds.
        callback (Optional[Callback], optional):
            A function to be called when a SYN/ACK response is received. This function should accept the destination,
            port, and an optional boolean indicating whether the port is open.
        callback_opened_only (bool, optional):
            If True, the callback will only be called for open ports. Defaults to True.

    Returns:
        List[ScanResult]:
            A list containing the scan results for multiple ports on the given destination.
    """

@overload
def syn_scan(
    dest: _ScanDestinations,
    ports: _PortRange,
    timeout: Optional[float] = 5.0,
    callback: Optional[Callback] = None,
    callback_opened_only: bool = True,
) -> List[ScanResult]:
    """Perform a SYN scan on the specified destination(s) and ports.

    This function attempts to connect to the specified ports on the given destination(s)
    using a SYN scan method. It can handle both single and multiple destinations and ports.

    The callback function is called when a SYN/ACK response is received. This function runs
    in the same thread as the scan, so avoid long-running operations in the callback.

    Example:
        syn_scan('192.168.0.1', range(1024, 65535))
        syn_scan('192.168.0.1/23', [80, 443, 25565])
        syn_scan(['192.168.0.1', '192.168.0.2', '192.168.0.3', '10.0.0.0/23'], 80)

    Args:
        dest (_ScanDestination):
            A single destination IP address (IPv4 or IPv6),
            a network address with a mask (e.g., '192.168.0.1/32'),
            or a hostname (e.g., 'example.com').
            Can also be a list of such addresses.
        ports (_Ports):
            A single port number, a range of ports, or a sequence of port numbers to scan.
        timeout (Optional[float], optional):
            The timeout in seconds to wait for a response. Defaults to 5.0 seconds.
        callback (Optional[Callback], optional):
            A function to be called when a SYN/ACK response is received.
            This function should accept the destination, port, and an optional boolean indicating if the port is open.
        callback_opened_only (bool, optional):
            If True, the callback will only be called for open ports. Defaults to True.

    Returns:
        List[ScanResult]: A list of results indicating the status of the scanned ports.
    """
