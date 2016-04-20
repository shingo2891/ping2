# -*- coding: utf-8 -*-
# PINGテストプログラム
import loglog
import setting
import TestPing
import TestArp
import time


# Get Next IP adress
def NextIPaddress(ip_address):
    ip_info = ip_address.split(".")
    num = int(ip_info[3]) + 1
    if num == 256:
        num = 0
    ip_info[3] = str(num)
    return ip_info[0] + "." + ip_info[1] + "." + ip_info[2] + "." + ip_info[3]


# Get Previous IP adress
def PrevIPaddress(ip_address):
    ip_info = ip_address.split(".")
    num = int(ip_info[3]) - 1
    if num == -1:
        num = 255
    ip_info[3] = str(num)
    return ip_info[0] + "." + ip_info[1] + "." + ip_info[2] + "." + ip_info[3]


def Ping(ip_address):
    count_ok = 0
    count_ng = 0
    ping_count = setting.get_ping_count()

    print("ping -n 1 " + ip_address)
    loglog.writeLog("ping -n 1 " + ip_address)

    for var in range(0, int(ping_count)):
        ERROR, mes = TestPing.ping_test(ip_address)

        if ERROR is True:
            count_ng = count_ng + 1
        else:
            count_ok = count_ok + 1

        print(mes)
        loglog.writeLog(mes)
        time.sleep(1.0)

    print("OK:" + str(count_ok) + "  NG:" + str(count_ng))
    loglog.writeLog("OK:" + str(count_ok) + "  NG:" + str(count_ng))


def Arp(ip_address):
    ERROR, MAC_ADDR = TestArp.get_mac_from_ip(ip_address)
    if ERROR is True:
        print("Do not get MAC address")
        print(MAC_ADDR)
        loglog.writeLog(MAC_ADDR)
    else:
        print(ip_address + "," + MAC_ADDR)
        loglog.writeLog(ip_address + "," + MAC_ADDR)


# ------------------------
# main
# ------------------------
if __name__ == "__main__":
    print("======== ping2.py ========")
    setting.get_setting()
    ip_next = setting.get_static_ip()

    while True:
        print("   p + Enter:前のIPアドレス選択, n + Enter:次のIPアドレス選択")
        print("   x + Enter:アプリ終了")
        print("   Enter:PING実行")
        print("   Enter-> PING IP: " + ip_next)
        command = input()
        print("command: " + command)

        if command == 'n':
            # Set Next IP address
            ip_next = NextIPaddress(ip_next)

        elif command == 'p':
            # Set Previous IP address
            ip_next = PrevIPaddress(ip_next)

        elif command == '':
            Ping(ip_next)
            Arp(ip_next)
            print("")
            print("")
            ip_next = NextIPaddress(ip_next)

        elif command == 'e':
            print("終了")
            break

        elif command == 'x':
            print("終了")
            break

        else:
            print("Error!")

# End Of File
