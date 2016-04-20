# -*- coding: utf-8 -*-
# IPアドレスからPINGを実行する
import sys
import subprocess
import logging
import time

# logging.basicConfig(level=logging.DEBUG)
# CRITICAL > ERRO > WARNGIN > INFO > DEBUG > NOTEST
# logging.debug("")


#
def ping_test(IP_ADDR):
        cmd = "ping -n 1 " + IP_ADDR
        logging.debug("CMD: " + cmd)
        p = subprocess.Popen(
            cmd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=False
        )

        out_mes = p.stdout.readlines()
        for var in range(0, len(out_mes)):
            # Windowsの場合メッセージはcp932形式で出力される
            mes = "out_mes[" + str(var) + "]:"
            + out_mes[var].decode('cp932').rstrip("\r\n")
            logging.debug(mes)

        ret = p.wait()
        # out_ret = "return: %d" % ret
        # out_err = "stderr: %s" % (p.stderr.readlines())
        # logging.debug (out_ret)
        # logging.debug (out_err)
        mes1 = out_mes[2].decode('cp932').rstrip("\r\n")
        if ret == 0:
            mes2 = mes1.split(" ")
            if IP_ADDR == mes2[0]:
                return False, mes1
            else:
                return True, mes1
        else:
            return True, mes1


# IPアドレス
# 回数
def ping_test_c(IP_ADDR, count):
    count_ok = 0
    count_ng = 0

    for var in range(0, count):
        ERROR, mes = ping_test(IP_ADDR)

        if ERROR is True:
                count_ng = count_ng + 1
        else:
                count_ok = count_ok + 1

        print(mes)
        print("OK:" + str(count_ok))
        print("NG:" + str(count_ng))

        time.sleep(1.0)

    return False


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
    ERROR = ping_test_c(IP_ADDR, 3)
    if ERROR is True:
        print("error:0x02 Do not get MAC address")

# End Of File
