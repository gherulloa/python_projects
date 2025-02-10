from abc import ABC, abstractmethod

class Scanner(ABC):
    @abstractmethod
    def scan_document(self):
        pass
    @abstractmethod
    def get_scanner_status(self):
        pass
class Printer(ABC):
    @abstractmethod
    def print_document(self):
        pass
    @abstractmethod
    def get_printer_status(self):
        pass
class MFD1(Scanner, Printer):
    num_of_MFD1 = 0
    resolution = 20
    def __init__(self):
        MFD1.num_of_MFD1 += 1
        self.serial_num = f"MFD1.{MFD1.num_of_MFD1}"
    def scan_document(self) -> str:
        return "Document has been scanned."
    def get_scanner_status(self) -> str:
        return f"Scanner:\nMax Resolution: {MFD1.resolution}\nSerial Number: {self.serial_num}"
    def print_document(self):
        return "Document has been printed."
    def get_printer_status(self) -> str:
        return f"Printer:\nMax Resolution: {MFD1.resolution}\nSerial Number: {self.serial_num}"

class MFD2(Scanner, Printer):
    num_of_MFD2 = 0
    printing_history = []
    resolution = 40
    def __init__(self):
        MFD2.num_of_MFD2 += 1
        self.serial_num = f"MFD2.{MFD2.num_of_MFD2}"
    def scan_document(self) -> str:
        return "Document has been scanned."
    def get_scanner_status(self) -> str:
        return f"Scanner:\nMax Resolution: {MFD2.resolution}\nSerial Number: {self.serial_num}"
    def print_document(self) -> str:
        document = f"Document{len(MFD2.printing_history) + 1}"
        MFD2.printing_history.append(document)
        return f"{document} has been printed."
    def get_printer_status(self) -> str:
        return f"Printer:\nMax Resolution: {MFD2.resolution}\nSerial Number: {self.serial_num}"
    @classmethod
    def print_history(cls):
        return f"{cls.printing_history} documents have been printed."
    
class MFD3(Scanner, Printer):
    num_of_MFD3 = 0
    printing_operations = []
    resolution = 80
    def __init__(self):
        MFD3.num_of_MFD3 += 1
        self.serial_num = f"MFD3.{MFD3.num_of_MFD3}"
    def scan_document(self) -> str:
        return "Document has been scanned."
    def get_scanner_status(self):
        return f"Scanner:\nMax Resolution: {MFD3.resolution}\nSerial Number: {self.serial_num}"
    def print_document(self) -> str:
        document = f"Document{len(MFD2.printing_history) + 1}"
        MFD3.printing_operations.append(document)
        return f"{document} has been printed."
    def get_printer_status(self) -> str:
        return f"Printer:\nMax Resolution: {MFD3.resolution}\nSerial Number: {self.serial_num}"
    @classmethod
    def print_history(cls):
        return f"{cls.printing_operations} documents have been printed."

cheap_dev = MFD1()
med_dev = MFD2()
premium_dev = MFD3()

for i in (cheap_dev, med_dev, premium_dev):
    print(i.print_document())
    print(i.scan_document())
    print(i.get_printer_status())
    print(i.get_scanner_status())
    print()

print(med_dev.print_history(), "\n")
print(premium_dev.print_history())