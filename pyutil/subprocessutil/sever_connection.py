from __future__ import annotations
from connection.JsonSettingReader import JsonSettingReader
from connection.ServerConnectionSubprocess import ServerConnectionSubprocess
from connection.connection_info_reader import ConnectionInfoReader
from connection.net_command_error import NetCommandConnectionError


class ServerConnection:
    __readers : list[JsonSettingReader]
    def __init__(self):
        self.__readers = ConnectionInfoReader().to_readers()
    
    def __str__(self):
        return "\n+++++++++++++++++++++++++++++++++\n".join([str(r) for r in self.__readers])
    
    def __send(self, reader: JsonSettingReader,ignore:bool):
        ServerConnectionSubprocess(
            address=reader.address,
            user=reader.user,
            password=reader.password,
            ).send_command(ignore=ignore)
        
    def run(self,ignore=False):
        for reader in self.__readers:
            self.__send(reader,ignore)
            
    def connetct(self) -> dict[str]:
        errors: dict[str,str] = {}
        for reader in self.__readers:
            try:
                self.__send(reader, False)
            except NetCommandConnectionError as e:
                errors[str(reader)] = str(e)
            except Exception as e:
                raise e
        return errors


            
            
