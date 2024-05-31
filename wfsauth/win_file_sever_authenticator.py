from __future__ import annotations
from wfsauth.configration.json_setting_reader import JsonSettingReader
from wfsauth.executor.server_connection_subprocess import FileSeverAuthenticationCommandExecutor
from wfsauth.configration.connection_info_builder import ConnectionInformationBuilder
from wfsauth.error.net_command_error import NetUseCommandCError

class WindFileServerAuthenticator:
    """Windowsのファイル共有の認証を通す"""
    __readers : list[JsonSettingReader]
    def __init__(self):
        self.__readers = ConnectionInformationBuilder().to_readers()
    
    def __str__(self):
        return "\n+++++++++++++++++++++++++++++++++\n".join([str(r) for r in self.__readers])
    
    def __send(self, reader: JsonSettingReader,ignore:bool):
        FileSeverAuthenticationCommandExecutor(
            address=reader.address,
            user=reader.user,
            password=reader.password,
            ).send_command(ignore=ignore)
        
    def run(self,ignore=False):
        for reader in self.__readers:
            self.__send(reader,ignore)
            
    def connect(self) -> dict[str]:
        errors: dict[str,str] = {}
        for reader in self.__readers:
            try:
                self.__send(reader, False)
            except NetUseCommandCError as e:
                errors[str(reader)] = str(e)
            except Exception as e:
                raise e
        return errors


            
            
