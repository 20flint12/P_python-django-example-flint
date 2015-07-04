
mysql -u root

Администрирование
Восстановление забытого пароля для root'a

    Остановите mysqld
sudo service mysql stop

    Запустите mysqld с параметрами --skip-grant-tables --user=root:
sudo mysqld --skip-grant-tables --user=root

    Подключитесь к MySQL-серверу командой:
mysql -u root

    Обновите пароль для root'a:
//UPDATE mysql.user SET Password=PASSWORD('<новый пароль>') WHERE User='root';
UPDATE mysql.user SET Password=PASSWORD('1234') WHERE User='root';
FLUSH PRIVILEGES;