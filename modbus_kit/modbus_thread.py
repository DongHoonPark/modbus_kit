import threading
import queue
from typing import Any, Callable, Iterable, Mapping

class ModbusPeriodicScan(object):
    def __init__(self, aname:str, period:float, opcode:int, dtype:str) -> None:
        self._aname  : str   = aname
        self._period : float = period
        self._opcode : int   = opcode
        self._dtype  : str   = dtype

class ModbusThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
        args=(), kwargs=None, *, daemon=None):

        super().__init__(group=group, target=target, name=name,
            args=args, kwargs=kwargs, daemon=daemon)

        self._terminate_flag = False
        self._transaction_queue = queue.PriorityQueue()

    def run(self):
        while(not self._terminate_flag):
            pass

    def terminate(self):
        self._terminate_flag = True

    def transaction_push(self):
        pass