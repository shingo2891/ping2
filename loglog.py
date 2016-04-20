# -*- coding: utf-8 -*-
import sys
import datetime
import setting


# ------------------------
# Add log
# ------------------------
def writeLog(message):
    try:
        file_log = open(setting.get_log_file_name(), "a")
    except Exception as e:
        print("++++File error++++")
        print("type:" + str(type(e)))
        print("args:" + str(e.args))
        print("message:" + e.message)
        print("e自身:" + str(e))
        file_log.close()
        sys.exit(1)

    # Add log data
    time = datetime.datetime.today()
    file_log.write(time.strftime("%m/%d %H:%M:%S "))
    file_log.write(message + "\n")

    file_log.close()

# End Of File
