# scanner.pyi
from typing import Any, Callable, List, Optional, Union, Sequence

_ScanDestination = Union[str, Sequence[str]]
_Ports = Union[int, Sequence[int]]
Callback = Callable[[str, int, Optional[bool]], None]

# Function for sync usage
def syn_scan(
    dest: _ScanDestination, ports: _Ports, timeout: Optional[float] = 5.0, /
) -> None: ...
def set_callback(func: Callback, opened_only: bool = False) -> None: ...

# Function for async usage
async def syn_scan_async(
    dest: _ScanDestination, ports: _Ports, timeout: Optional[float] = 5.0, /
) -> List[Any]: ...
