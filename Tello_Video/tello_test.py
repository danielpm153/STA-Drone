from tello import Tello
import sys
from datetime import datetime
import time

start_time = str(datetime.now())
#print(sys.argv)
#file_name = sys.argv[1]
#file_name = "command_teste.txt"
file_name = "command.txt"

f = open(file_name, "r")
commands = f.readlines()

tello = Tello()
for command in commands:
    print(command)
    if command != '' and command != '\n':
        command = command.rstrip()

        if command.find('delay') != -1:
            sec = float(command.partition('delay')[2])
            print 'delay %s' % sec
            time.sleep(sec)
            pass
        else:
            tello.send_command(command)

log = tello.get_log()

out = open('log/' + start_time + '.txt', 'w')
for stat in log:
    stat.print_stats()
    str = stat.return_stats()
    out.write(str)
