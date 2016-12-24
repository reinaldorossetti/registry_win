import winreg
import re
import win32gui
import win32con

# use this if you need to modify the system variable and if you have admin privileges.


class RegistryWin:

    def __init__(self):

        self.reg_path = ""
        self.key_name = ""
        self.value = ""

    def open_key_reg(self, local):
        winreg.CreateKey(winreg.HKEY_CURRENT_USER, self.reg_path)
        if "user" == local:
            registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.reg_path, 0, winreg.KEY_ALL_ACCESS)
        else:
            registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, self.reg_path, 0, winreg.KEY_ALL_ACCESS)

        return registry_key

    def set_reg_path(self, reg_key):
        winreg.SetValueEx(reg_key, self.key_name, 0, winreg.REG_SZ, self.value)
        # notify the system about the changes
        win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SETTINGCHANGE, 0, self.reg_path)


    def set_reg_path_bin(self, reg_key):
        winreg.SetValueEx(reg_key, self.key_name, 0, winreg.REG_BINARY, self.value)
        # notify the system about the changes
        win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SETTINGCHANGE, 0, self.reg_path)

    def query_path(self, reg_key):
        try:
            value, regtype = winreg.QueryValueEx(reg_key, self.key_name)
        except WindowsError:
            value = ''
        return value

    def windows_path_set(self, local, new_path):
        self.key_name = 'PATH'
        if local == 'user':
            self.reg_path = 'Environment'
        else:
            self.reg_path = 'SYSTEM\CurrentControlSet\Control\Session Manager\Environment'

        # vai gerar o reg_key
        reg_key = self.open_key_reg(local)
        # consulta o valor do registro.
        path = self.query_path(reg_key)

        if new_path not in path:
            self.value = ("{};{}".format(path, new_path))
            self.set_reg_path(reg_key)

        if new_path in self.query_path(reg_key):
            print("Relizado com sucesso")
        else:
            return False

        winreg.CloseKey(reg_key)  # close connection
        return True


    def compatibility_mode(self, local, site, value):
        self.key_name = 'UserFilter'
        self.reg_path = 'Software\Microsoft\Internet Explorer\BrowserEmulation\ClearableListData'
        self.value = value
        reg_key = self.open_key_reg(local)
        result = self.find_site(site, reg_key)
        if not result:
            self.set_reg_path_bin(reg_key)
            result = (self.find_site(site, reg_key))
        # close connection
        winreg.CloseKey(reg_key)
        if result:
            return "Site adicionado no registro com sucesso."
        else:
            return "Erro - Site nao encontrado."

    def find_site(self, site, reg_key):
        path = self.query_path(reg_key)
        path = str(path)
        # Remove todos hex da string.
        path = re.sub(r'[\\x00-\\xff]+?', '', path)
        if site in path:
            return True
        return False


if __name__ == '__main__':
    # Instanciando a classe
    reg = RegistryWin()
    # Temos que passar pra funcao 'user' ou 'machine', existe dois Path um do User e outro do Machine.
    # Adicionar o caminho do projeto no sistema Windows.
    path = r'C:\testlink_automation'
    print(reg.windows_path_set('user', path))

    # Converte hex pra bytes, para poder enviar pro registro.
    # nome do site em hex 67 00 6d 00 61 00 69 00 6c 00 2e 00 63 00 6f 00 6d 00
    # http://codebeautify.org/string-hex-converter
    site_hex = bytes.fromhex('41 1f 00 00 53 08 ad ba 01 00 00 00 30 00 00 00 01 00 00 00 01 00 00 00 0c 00 00 00 9a dd 65 6f\
     28 5d d2 01 01 00 00 00 09 00 67 00 6d 00 61 00 69 00 6c 00 2e 00 63 00 6f 00 6d 00')

    print(reg.compatibility_mode('user', "gmail.com", site_hex))
