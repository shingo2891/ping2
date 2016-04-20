# -*- coding: utf-8 -*-
# IPアドレスからARPを実行してMACアドレスを取得する
import sys
import subprocess
import logging

# logging.basicConfig(level=logging.DEBUG)
# CRITICAL > ERRO > WARNGIN > INFO > DEBUG > NOTEST
# logging.debug("")


#
def get_mac_from_ip(IP_ADDR):
    cmd = "arp -a " + IP_ADDR
    logging.debug("CMD: " + cmd)
    p = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=False
    )

    out_mes = p.stdout.readlines()
    if len(out_mes) == 1:
        return True, "No arp entry"

    elif len(out_mes) == 4:
        # ARP entry
        pass
    else:
        return True, "Other Error"

    for var in range(0, len(out_mes)):
        # Windowsの場合メッセージはcp932形式で出力される
        mes = "out_mes[" + str(var) + "]:" + out_mes[var].decode('cp932').rstrip("\r\n")
        logging.debug(mes)

    ret = p.wait()
    out_ret = "return: %d" % ret
    out_err = "stderr: %s" % (p.stderr.readlines())
    # logging.debug(out_ret)
    # logging.debug(out_err)
    # logging.debug(type(out_mes[3]))

    mes1 = out_mes[3].decode('cp932')
    mes2 = mes1.split(" ")
    # logging.debug(mes2)

    for var in range(0, len(mes2)):
        mes3 = mes2[var]
        logging.debug("str_mac[" + str(var) + "]" + mes3)

    while (True):
        try:
            mes2.remove("")
        except:
            break

    for var in range(0, len(mes2)):
        mes3 = mes2[var]
        logging.debug("str_mac[" + str(var) + "]" + mes3)


    str_ip = mes2[0]
    logging.debug("IP " + str_ip)
    str_mac = mes2[1].replace("-", ":")
    logging.debug("MAC " + str_mac)

    return False, str_mac


# ------------------------
# main
# ------------------------
if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv)
    if argc != 2:
        print("error:0x01 miss match parameter")
        sys.exit()

    IP_ADDR = argv[1]
    print("IP: " + IP_ADDR)
    ERROR, MAC_ADDR = get_mac_from_ip(IP_ADDR)
    if ERROR is True:
        print("error:0x02 Do not get MAC address")
        print(MAC_ADDR)
    else:
        print("MAC: " + MAC_ADDR)

# End Of File
