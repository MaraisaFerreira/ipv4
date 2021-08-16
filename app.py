from classes.calc_ipv4 import CalcIPV4

calc_ipv4 = CalcIPV4(ip='192.168.0.1', mask='255.255.255.0')
print(f'IP: {calc_ipv4.ip}')
print(f'Máscara: {calc_ipv4.mask}')
print(f'Prefixo: {calc_ipv4.prefix}')
print(f'Rede: {calc_ipv4.net}')
print(f'Broadcast: {calc_ipv4.broadcast}')
print(f'Qtds IPs: {calc_ipv4.ips_amount}')
