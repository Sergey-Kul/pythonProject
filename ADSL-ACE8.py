ipaddress = input('Введи ip адрес коммутатора: ')  # создаём переменную для обозначения ip

mask = input("Введи mask коммутатора: ")  # создаём переменную для обозначения маски коммутатора

gateway = input("Введи шлюз коммутатора: ")  # создаём переменную шлюза

vpi1 = input('Введи VPI для 1 порта: ')  # vpi для 1 порта
vсi1 = input('Введи VСI для 1 порта: ')  # vci для 1 порта

vpi2 = input('Введи VPI для 2 порта: ')  # vpi для 2 порта
vсi2 = input('Введи VСI для 2 порта: ')  # vci для 2 порта

vpi3 = input('Введи VPI для 3 порта: ')  # vpi для 3 порта
vсi3 = input('Введи VСI для 3 порта: ')  # vci для 3 порта

vpi4 = input('Введи VPI для 4 порта: ')  # vpi для 4 порта
vсi4 = input('Введи VСI для 4 порта: ')  # vci для 4 порта

vpi5 = input('Введи VPI для 5 порта: ')  # vpi для 5 порта
vсi5 = input('Введи VСI для 5 порта: ')  # vci для 5 порта

vpi6 = input('Введи VPI для 6 порта: ')  # vpi для 6 порта
vсi6 = input('Введи VСI для 6 порта: ')  # vci для 6 порта

vpi7 = input('Введи VPI для 7 порта: ')  # vpi для 7 порта
vсi7 = input('Введи VСI для 7 порта: ')  # vci для 7 порта

vpi8 = input('Введи VPI для 8 порта: ')  # vpi для 8 порта
vсi8 = input('Введи VСI для 8 порта: ')  # vci для 8 порта

polvlan = input("Название пользовательского Vlan: ")  # вписываем название пользовательского vlan
pvlan = input('Введи пользовательский Vlan: ')  # вводим пользовательский вилан

mgvlan = input("Введи управляющий Vlan: ")  # создаём управляющий вилан
# погнал вывод существующего конфига для дслама асе8

f = open("ACE8DSLAM.txt", "w")
print('ip set interface iplan ipaddress', ipaddress, mask, file=f),
print('ip add route qwe 0.0.0.0 0.0.0.0 gateway', gateway, file=f)
print("rfc1483 set transport wb0 vpi", vpi1, file=f)
print("rfc1483 set transport wb0 vci", vсi1, file=f)
print("rfc1483 set transport wb1 vpi", vpi2, file=f)
print("rfc1483 set transport wb1 vci", vсi2, file=f)
print("rfc1483 set transport wb2 vpi", vpi3, file=f)
print("rfc1483 set transport wb2 vci", vсi3, file=f)
print("rfc1483 set transport wb3 vpi", vpi4, file=f)
print("rfc1483 set transport wb3 vci", vсi4, file=f)
print("rfc1483 set transport wb4 vpi", vpi5, file=f)
print("rfc1483 set transport wb4 vci", vсi5, file=f)
print("rfc1483 set transport wb5 vpi", vpi6, file=f)
print("rfc1483 set transport wb5 vci", vсi6, file=f)
print("rfc1483 set transport wb6 vpi", vpi7, file=f)
print("rfc1483 set transport wb6 vci", vсi7, file=f)
print("rfc1483 set transport wb7 vpi", vpi8, file=f)
print("rfc1483 set transport wb8 vci", vсi8, file=f)
print("bridge add vlan", polvlan, pvlan, "Qbridge", file=f)
print("bridge add vlaninterface", polvlan, "tagged uplink", file=f)
print("bridge add vlaninterface", polvlan, "untagged wan0", file=f)
print("bridge add vlaninterface", polvlan, "untagged wan1", file=f)
print("bridge add vlaninterface", polvlan, "untagged wan2", file=f)
print("bridge add vlaninterface", polvlan, "untagged wan3", file=f)
print("bridge add vlaninterface", polvlan, "untagged wan4", file=f)
print("bridge add vlaninterface", polvlan, "untagged wan5", file=f)
print("bridge add vlaninterface", polvlan, "untagged wan6", file=f)
print("bridge add vlaninterface", polvlan, "untagged wan7", file=f)
print("bridge set interface wan0 pvid", pvlan, file=f)
print("bridge set interface wan1 pvid", pvlan, file=f)
print("bridge set interface wan2 pvid", pvlan, file=f)
print("bridge set interface wan3 pvid", pvlan, file=f)
print("bridge set interface wan4 pvid", pvlan, file=f)
print("bridge set interface wan5 pvid", pvlan, file=f)
print("bridge set interface wan6 pvid", pvlan, file=f)
print("bridge set interface wan7 pvid", pvlan, file=f)
print("bridge add vlan MGMT", mgvlan, "MGMT", file=f)
print("bridge add vlaninterface MGMT tagged uplink", file=f)
print("bridgevlan add transport vtl", mgvlan, file=f)
print("ip interface iplan attachbridgevlan vtl", file=f)
print("system config save", file=f)
f.close()