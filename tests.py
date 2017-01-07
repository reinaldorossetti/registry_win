# Instanciando a classe

from os import environ, system
import platform
from subprocess import getstatusoutput
# importando a classe
from registry import RegistryWin
# Instanciando a classe.
reg = RegistryWin()

"""
O primeiro problema eh adicionar o path do projeto no sistema, ou qualquer caminho que deseja.
Primeiramente temos que passar pra funcao 'user' ou 'machine', existe dois Path um do User e outro do Machine.
Segundo passamos o path do projeto ou o path de arquivos para serem executados.
"""
path = r'C:\testlink_automation'
print(reg.windows_path_set('user', path))

"""
Segundo problema eh adicionar o nome do site no modo de compatibilidade para sites antigos, que precisam ter
uma compatibilidade com alguma versao do browser.
"""
# passamos a configuracao em hex, para juntar com o site desejado.
conf_site_hex = '41 1f 00 00 53 08 ad ba 01 00 00 00 30 00 00 00 01 00 00 00 01 00 00 00 0c 00 00 00 9a dd 65 6f\
 28 5d d2 01 01 00 00 00 09 '
print(reg.compatibility_mode('user', "gmail.com", conf_site_hex))

"""
Temos um terceiro problema que eh a subchave FEATURE_BFCACHE precisa estah setado como 0 por padrao.
For IE 11 only, you will need to set a registry entry on the target computer so that the driver can maintain
a connection to the instance of Internet Explorer it creates.
"""

# Primeiro verifica a versao do IE, se for IE11 ele executa a funcao pra adicionar a chave bfcache.
# Verificar se o sistema operacional eh 64 ou 32bits, systeminfo me retorna o tipo de sistema.
# quando coloco o [1] que dizer que quero somente o segundo valor da lista, que eh o resultado do cmd.

reg.reg_path = "Software\Microsoft\Internet Explorer"
reg.key_name = "svcVersion"
# cria a key
key_open = reg.open_key_reg("machine")
verified = reg.query_path(key_open)
reg.close_reg(key_open)

def add_key_bfcache():
    sys = getstatusoutput("systeminfo | findstr //C:\"Tipo de sistema\" /C:\"System type\"")[1]
    if 'x64' in sys.lower():
        reg.reg_path = "SOFTWARE\Wow6432Node\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_BFCACHE"
    else:
        reg.reg_path = "SOFTWARE\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_BFCACHE"

    # cria a key
    key_open = reg.open_key_reg("machine")

    # Configuro as variaveis.
    reg.key_name = "iexplore.exe"
    reg.value = 0

    # Verifica se a chave jah existe.
    # caso nao exista ele seta.
    verified = reg.query_path(key_open)
    if not verified == 0:
        reg.set_reg_path_dword(key_open)
        print("FEATURE_BFCACHE adicionado.")
    else:
        print("Registro jah adicionado.")

if "11." in verified:
    add_key_bfcache()
