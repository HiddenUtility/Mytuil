

import subprocess
from subprocess import CalledProcessError
from wfsauth.error.net_command_error import NetUseCommandCError


class FileSeverAuthenticationCommandExecutor:
    """NET USEを使って認証を通す"""
    NET_PATTERN = "NET USE {0} /user:{1} {2}"

    def __init__(self,address="",user="",password=""):
        self.__net_cmd = self.NET_PATTERN.format(address, user, password)

    def send_command(self,ignore=False) -> None:
        print(self.__net_cmd)
        args = self.__net_cmd.split(" ")
        try:
            res = subprocess.run(args,shell=True ,capture_output = True)
        except CalledProcessError as e:
            raise e
        except Exception as e:
            raise e
        else:
            print(res.stdout.decode("cp932"))
            err = res.stderr.decode("cp932")

        if err != "":
            if not ignore:
                raise NetUseCommandCError(err)
            else:
                print(err)
