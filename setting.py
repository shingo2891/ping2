# -*- coding: utf-8 -*-
import configparser

PROGRAM_NAME = "PING2 test program"
PROGRAM_VERSION = "0.001"

# ------------------------
#
# ------------------------
print(PROGRAM_NAME + " " + PROGRAM_VERSION)
GotFile = False

STATIC_IPADDR = ""
STATIC_NETMASK = ""
STATIC_DEFAULTGW = ""
FILE_NAME_LOG = ""
PING_COUNT = ""


# ------------------------
# Version infomation
# ------------------------
def get_version_info():
    return PROGRAM_NAME


# ------------------------
#
# ------------------------
def get_program_name():
    return PROGRAM_VERSION


# ------------------------
#
# ------------------------
def get_log_file_name():
    get_setting()
    return FILE_NAME_LOG


# ------------------------
#
# ------------------------
def get_static_ip():
    get_setting()
    return STATIC_IPADDR


# ------------------------
#
# ------------------------
def get_static_nm():
    get_setting()
    return STATIC_NETMASK


# ------------------------
#
# ------------------------
def get_static_gw():
    get_setting()
    return STATIC_DEFAULTGW


# ------------------------
#
# ------------------------
def get_ping_count():
    get_setting()
    return PING_COUNT


# ------------------------
# ファイルの読み込み
# ------------------------
def get_setting():
    global GotFile

    global STATIC_IPADDR
    global STATIC_NETMASK
    global STATIC_DEFAULTGW
    global FILE_NAME_LOG
    global PING_COUNT

    if GotFile is False:
        print("setting.py:ファイル読み込み")
        inifile = configparser.SafeConfigParser()
        inifile.read("./setting.ini")

        STATIC_IPADDR = inifile.get("Setting", "IpAddr")
        STATIC_NETMASK = inifile.get("Setting", "NetMask")
        STATIC_DEFAULTGW = inifile.get("Setting", "DefaultGW")
        FILE_NAME_LOG = inifile.get("FileName", "FILE_NAME_LOG")
        PING_COUNT = inifile.get("PING", "PingCount")
        GotFile = True


def setting_check():
    print("IpAddr:          " + get_static_ip())
    print("NetMask:         " + get_static_nm())
    print("DefaultGW:       " + get_static_gw())
    print("FILE_NAME_LOG:   " + get_log_file_name())
    print("PING_COUNT:      " + get_ping_count())

# ------------------------
# main
# ------------------------
if __name__ == "__main__":
    print("====setting.py====")
