# greamline_infra
greamline Infra repository
1. Для выполнения команд на bastionhost используйте скрипт:
python3 ssh_connect.py
2. Для выполнения команд на someinternalhost используйте скрипт:
python3 ssh_connect_smh.py
3. Изменен скрипт установки пакетов на bastionhost:
sudo bash setupvpn.sh
4. Подключение к VPN осуществляется с использованием конфигурационного файла:
Otus_test_otus_vpn.ovpn
