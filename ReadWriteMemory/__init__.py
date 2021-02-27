#8888888b.                        888 888       888         d8b 888            888b     d888                                                  
#888   Y88b                       888 888   o   888         Y8P 888            8888b   d8888                                                  
#888    888                       888 888  d8b  888             888            88888b.d88888                                                  
#888   d88P .d88b.   8888b.   .d88888 888 d888b 888 888d888 888 888888 .d88b.  888Y88888P888  .d88b.  88888b.d88b.   .d88b.  888d888 888  888 
#8888888P" d8P  Y8b     "88b d88" 888 888d88888b888 888P"   888 888   d8P  Y8b 888 Y888P 888 d8P  Y8b 888 "888 "88b d88""88b 888P"   888  888 
#888 T88b  88888888 .d888888 888  888 88888P Y88888 888     888 888   88888888 888  Y8P  888 88888888 888  888  888 888  888 888     888  888 
#888  T88b Y8b.     888  888 Y88b 888 8888P   Y8888 888     888 Y88b. Y8b.     888   "   888 Y8b.     888  888  888 Y88..88P 888     Y88b 888 
#888   T88b "Y8888  "Y888888  "Y88888 888P     Y888 888     888  "Y888 "Y8888  888       888  "Y8888  888  888  888  "Y88P"  888      "Y88888 
#                                                                                                                                         888 
#                                                                                                                                    Y8b d88P 
#                                                                                                                                     "Y88P"  

from typing import Any,  List, NewType
import os.path
import ctypes
import ctypes.wintypes

# Process Permissions
PROCESS_QUERY_INFORMATION = 0x0400
PROCESS_VM_OPERATION = 0x0008
PROCESS_VM_READ = 0x0010
PROCESS_VM_WRITE = 0x0020
PROCESS_ALL_ACCESS = 0x1f0fff

MAX_PATH = 260


class ReadWriteMemoryError(Exception):
    pass


class Process(object):
    """
    The Process class holds the information about the requested process.
    """
    def __init__(self, name: [str, bytes] = '', pid: int = -1, handle: int = -1, error_code: [str, bytes] = None):
        """
        :param name: The name of the executable file for the specified process.
        :param pid: The process ID.
        :param handle: The process handle.
        :param error_code: The error code from a process failure.
        """
        self.name = name
        self.pid = pid
        self.handle = handle
        self.error_code = error_code
        self.is_process_object = True
        self.keep_open = False

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}: "{self.name}"'

    def open(self):
        """
        Open the process with the Query, Operation, Read and Write permissions and return the process handle.

        :return: True if the handle exists if not return False
        """
        dw_desired_access = (PROCESS_QUERY_INFORMATION | PROCESS_VM_OPERATION | PROCESS_VM_READ | PROCESS_VM_WRITE)
        b_inherit_handle = False
        self.handle = ctypes.windll.kernel32.OpenProcess(dw_desired_access, b_inherit_handle, self.pid)
        if not self.handle:
            raise ReadWriteMemoryError(f'Unable to open process <{self.name}>')

    def set_keep_process(self, keep: bool):
        """
        It does not allow the handle to be closed with the method: 'close'

        :return: None
        """
        self.keep_open = keep

    def close(self, force: bool = False) -> int:
        """
        Closes the handle of the process.

        :return: The last error code from the result after an attempt to close the handle.
        """
        if force or not self.keep_open:
            ctypes.windll.kernel32.CloseHandle(self.handle)
            return self.get_last_error()
   
    def get_all_access_handle(self) -> int:
        """
        Gets full access handle of the process.

        :return: handle of the process
        """
        self.handle = ctypes.windll.kernel32.OpenProcess(PROCESS_ALL_ACCESS, True, self.pid)
    
    @staticmethod
    def get_last_error() -> int:
        """
        Get the last error code.

        :return: The last error code.
        """
        return ctypes.windll.kernel32.GetLastError()

    def get_pointer(self, lp_base_address: hex, offsets: List[hex] = ()) -> int:
        """
        Get the pointer of a given address.

        :param lp_base_address: The address from where you want to get the pointer.
        :param offsets: a list of offets.

        :return: The pointer of a give address.
        """
        temp_address = self.read(lp_base_address)
        pointer = 0x0
        if not offsets:
            return lp_base_address
        else:
            for offset in offsets:
                pointer = int(str(temp_address), 0) + int(str(offset), 0)
                temp_address = self.read(pointer)
            return pointer

    def get_pointer_modified(self, lp_base_address: int, offsets: List[hex] = ()) -> int:
        """
        Get the pointer of a given address.

        :param lp_base_address: The address from where you want to get the pointer.
        :param offsets: a list of offets.

        :return: The pointer of a give address.
        """
        if not offsets:
            return lp_base_address
        else:
            for offset in offsets:
                lp_base_address = self.read(lp_base_address, None, (), 0) + int(offset)
            return lp_base_address

    def read(self, lp_base_address: int, length: int, offsets: tuple = (), sepOffset: int=0) -> Any:
        """
        Read data from the process's memory.

        :param lp_base_address: The process's pointer

        :return: The data from the process's memory if succeed if not raises an exception.
        """
        try:
            if offsets:
                lp_base_address = self.get_pointer_modified(lp_base_address, offsets) + sepOffset
            if not length:
                read_buffer = ctypes.c_uint()
                lp_buffer = ctypes.byref(read_buffer)
                n_size = ctypes.sizeof(read_buffer)
                lp_number_of_bytes_read = ctypes.c_ulong(0)
                ctypes.windll.kernel32.ReadProcessMemory(self.handle, lp_base_address, lp_buffer,
                                                     n_size, lp_number_of_bytes_read)
                return read_buffer.value
            else:
                read_buffer = ctypes.create_string_buffer(length)
                lp_number_of_bytes_read = ctypes.c_ulong(0)
                ctypes.windll.kernel32.ReadProcessMemory(self.handle, lp_base_address, read_buffer, length, lp_number_of_bytes_read)
                bufferArray = bytearray(read_buffer)
                found_terminator = bufferArray.find(b'\x00')
                if found_terminator != -1:
                    return bufferArray[:found_terminator].decode('utf-8')
                # Echarle ojito, al parecer no esta del todo bien
                print(bufferArray)
                print("[ReadMemory/Error]: terminator not found.\naddress: %s" % hex(lp_base_address))
                return ""
        except (BufferError, ValueError, TypeError) as error:
            if self.handle:
                self.close()
            self.error_code = self.get_last_error()
            error = {'msg': str(error), 'Handle': self.handle, 'PID': self.pid,
                     'Name': self.name, 'ErrorCode': self.error_code}
            ReadWriteMemoryError(error)

    def read_long(self, lp_base_address: int, length: int, offsets: tuple = (), sepOffset: int=0) -> Any:
        """
        Read data from the process's memory.

        :param lp_base_address: The process's pointer

        :return: The data from the process's memory if succeed if not raises an exception.
        """
        try:
            if offsets:
                lp_base_address = self.get_pointer_modified(lp_base_address, offsets) + sepOffset
            if not length:
                read_buffer = ctypes.c_ulonglong()
                lp_buffer = ctypes.byref(read_buffer)
                n_size = ctypes.sizeof(read_buffer)
                lp_number_of_bytes_read = ctypes.c_ulonglong(0)
                ctypes.windll.kernel32.ReadProcessMemory(self.handle, lp_base_address, lp_buffer,
                                                     n_size, lp_number_of_bytes_read)
                return read_buffer.value
            else:
                read_buffer = ctypes.create_string_buffer(length)
                lp_number_of_bytes_read = ctypes.c_ulong(0)
                ctypes.windll.kernel32.ReadProcessMemory(self.handle, lp_base_address, read_buffer, length, lp_number_of_bytes_read)
                bufferArray = bytearray(read_buffer)
                found_terminator = bufferArray.find(b'\x00')
                if found_terminator != -1:
                    return bufferArray[:found_terminator].decode('utf-8')
                # Echarle ojito, al parecer no esta del todo bien
                print(bufferArray)
                print("[ReadMemory/Error]: terminator not found.\naddress: %s" % hex(lp_base_address))
                return ""
        except (BufferError, ValueError, TypeError) as error:
            if self.handle:
                self.close()
            self.error_code = self.get_last_error()
            error = {'msg': str(error), 'Handle': self.handle, 'PID': self.pid,
                     'Name': self.name, 'ErrorCode': self.error_code}
            ReadWriteMemoryError(error)

    def write(self, lp_base_address: int, value: (int, str), offsets: tuple, sepOffset: int=0) -> bool:
        """
        Write data to the process's memory.

        :param lp_base_address: The process' pointer.
        :param value: The data to be written to the process's memory

        :return: It returns True if succeed if not it raises an exception.
        """
        try:
            if offsets:
                lp_base_address = self.get_pointer_modified(lp_base_address, offsets) + sepOffset
            if isinstance(value, int):
                write_buffer = ctypes.c_uint(value)
                lp_buffer = ctypes.byref(write_buffer)
                n_size = ctypes.sizeof(write_buffer)
                lp_number_of_bytes_written = ctypes.c_ulong(0)
                ctypes.windll.kernel32.WriteProcessMemory(self.handle, lp_base_address, lp_buffer,
                                                        n_size, lp_number_of_bytes_written)
            elif isinstance(value, str):
                write_buffer = ctypes.create_string_buffer(value.encode())
                lp_buffer = ctypes.byref(write_buffer)
                n_size = ctypes.sizeof(write_buffer)
                lp_number_of_bytes_written = ctypes.c_size_t()
                ctypes.windll.kernel32.WriteProcessMemory(self.handle, lp_base_address, lp_buffer,
                                                        n_size, lp_number_of_bytes_written)
            return True
        except (BufferError, ValueError, TypeError) as error:
            if self.handle:
                self.close()
            self.error_code = self.get_last_error()
            error = {'msg': str(error), 'Handle': self.handle, 'PID': self.pid,
                     'Name': self.name, 'ErrorCode': self.error_code}
            ReadWriteMemoryError(error)

class ReadWriteMemory:
    """
    The ReadWriteMemory Class is used to read and write to the memory of a running process.
    """
    def __init__(self):
        self.process = Process()

    @staticmethod
    def get_process_by_name_list(process_name: [str, bytes]) -> "Process":
        process_ids = ReadWriteMemory.enumerate_processes()

        process_list_found = []
        for process_id in process_ids:
            self = ReadWriteMemory()
            self.process.handle = ctypes.windll.kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, process_id)
            if self.process.handle:
                image_file_name = (ctypes.c_char * MAX_PATH)()
                if ctypes.windll.psapi.GetProcessImageFileNameA(self.process.handle, image_file_name, MAX_PATH) > 0:
                    filename = os.path.basename(image_file_name.value)
                    if filename.decode('utf-8') == process_name:
                        self.process.pid = process_id
                        process_list_found.append(self.process)
                if not process_list_found:
                    self.process.close()
        return process_list_found

    def get_process_by_name(self, process_name: [str, bytes]) -> "Process":
        """
        :description: Get the process by the process executabe\'s name and return a Process object.

        :param process_name: The name of the executable file for the specified process for example, my_program.exe.

        :return: A Process object containing the information from the requested Process.
        """
        if not process_name.endswith('.exe'):
            self.process.name = process_name + '.exe'
        else:
            self.process.name = process_name

        process_ids = self.enumerate_processes()

        process_list_found = []
        for process_id in process_ids:
            self.process.handle = ctypes.windll.kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, process_id)
            if self.process.handle:
                image_file_name = (ctypes.c_char * MAX_PATH)()
                if ctypes.windll.psapi.GetProcessImageFileNameA(self.process.handle, image_file_name, MAX_PATH) > 0:
                    filename = os.path.basename(image_file_name.value)
                    if filename.decode('utf-8') == process_name:
                        self.process.pid = process_id
                        process_list_found.append(self.process)
                if not process_list_found:
                    self.process.close()
        return process_list_found

        raise ReadWriteMemoryError(f'Process "{self.process.name}" not found!')

    def get_process_by_id(self, process_id: int) -> "Process":
        """
        :description: Get the process by the process ID and return a Process object.

        :param process_id: The process ID.

        :return: A Process object containing the information from the requested Process.
        """

        self.process.handle = ctypes.windll.kernel32.OpenProcess(PROCESS_QUERY_INFORMATION, False, process_id)
        if self.process.handle:
            image_file_name = (ctypes.c_char * MAX_PATH)()
            if ctypes.windll.psapi.GetProcessImageFileNameA(self.process.handle, image_file_name, MAX_PATH) > 0:
                filename = os.path.basename(image_file_name.value)
                self.process.pid = process_id
                self.process.name = filename.decode('utf-8')
                self.process.close()
                return self.process
            else:
                raise ReadWriteMemoryError(f'Unable to get the executable\'s name for PID={self.process.pid}!')

        raise ReadWriteMemoryError(f'Process "{self.process.pid}" not found!')

    @staticmethod
    def enumerate_processes() -> list:
        """
        Get the list of running processes ID's from the current system.

        :return: A list of processes ID's
        """
        count = 32
        while True:
            process_ids = (ctypes.wintypes.DWORD * count)()
            cb = ctypes.sizeof(process_ids)
            bytes_returned = ctypes.wintypes.DWORD()
            if ctypes.windll.Psapi.EnumProcesses(ctypes.byref(process_ids), cb, ctypes.byref(bytes_returned)):
                if bytes_returned.value < cb:
                    return list(set(process_ids))
                else:
                    count *= 2