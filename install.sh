apt updata
apt upgrade 

apt install python3.8 -y
apt install python3.pip

python3.8 -m pip install -U pip
python3.8 -m pip install -U setuptools
python3.8 -m pip uninstall pyrogram
python3.8 -m pip install -U pyrofork
python3.8 -m pip install -U requests

python3.8 -m pip install -U pySmartDL
python3.8 -m pip install -U selenium-wire
python3.8 -m pip install -U selenium 

sudo snap install firefox
sudo add-apt-repository -y ppa:mozillateam/ppa
echo '
Package: *
Pin: release o=LP-PPA-mozillateam
Pin-Priority: 1001

Package: firefox
Pin: version 1:1snap1-0ubuntu2
Pin-Priority: -1
' | sudo tee /etc/apt/preferences.d/mozilla-firefox

sudo snap remove firefox
sudo apt update && sudo apt install -y firefox



