from PySide6.QtWidgets import QWidget

class ModbusPeriodicScan(object):
    def __init__(self, aname:str, period:float, opcode:int, address:int, dtype:str) -> None:
        self._aname  : str   = aname
        self._period : float = period
        self._opcode : int   = opcode
        self._address: int   = address
        self._dtype  : str   = dtype

class ModbusPeriodicScanWidget(QWidget):
    def __init__(self, parent, f):
        super().__init__(parent, f)

        self.modbus_periodic_scan = ModbusPeriodicScan()
        self.init_ui()

    def init_ui(self):
        pass
