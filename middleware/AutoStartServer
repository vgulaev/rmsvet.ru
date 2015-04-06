#!/bin/bash
#Update system
yum -y upgrade
yum -y install gcc
yum -y install make
yum -y install tar
#Install developer pack
yum -y groupinstall "Development tools"
yum -y install zlib-devel
yum -y install bzip2-devel
yum -y install openssl-devel
yum -y install ncurses-devel
yum -y install sqlite-devel
yum -y install readline-devel
yum -y install tk-devel
yum -y install gdbm-devel
yum -y install db4-devel
yum -y install libpcap-devel
yum -y install xz-devel
#Install Python 3.4.3
cd
wget https://www.python.org/ftp/python/3.4.1/Python-3.4.1.tar.xz --no-check-certificate
tar xf Python-3.4.1.tar.xz
cd Python-3.4.1
./configure --prefix=/usr/local --enable-shared LDFLAGS="-Wl,-rpath /usr/local/lib"
make && sudo make altinstall
#Install mysql
yum -y install mysql
yum -y install mysql-server
/sbin/service mysqld start
#Write mysqld in autoload
chkconfig mysqld on
#RePass $1
echo "Write the password for mysql"
read password
/usr/bin/mysqladmin -u root password $password
