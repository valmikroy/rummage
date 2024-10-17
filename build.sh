apt update && apt upgrade -y && apt autoremove -y
apt-get install wget sudo -y
apt-get install build-essential -y
wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
tar -xzf ta-lib-0.4.0-src.tar.gz
cd ta-lib
wget 'http://git.savannah.gnu.org/gitweb/?p=config.git;a=blob_plain;f=config.guess;hb=HEAD' -O './config.guess'
wget 'http://git.savannah.gnu.org/gitweb/?p=config.git;a=blob_plain;f=config.sub;hb=HEAD' -O './config.sub'
./configure --prefix=/usr
make
make install
rm -rf ta-lib
rm -rf ta-lib-0.4.0-src.tar.gz
pip install --upgrade pip

