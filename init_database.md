########################################
# ON NEW MACHINE ONLY
########################################
https://cloudcone.com/docs/article/how-to-install-docker-on-ubuntu-22-04-20-04/

sudo apt install apt-transport-https curl gnupg-agent ca-certificates software-properties-common -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
sudo apt install docker-ce docker-ce-cli containerd.io -y
sudo usermod -aG docker $USER
newgrp docker
docker version
sudo systemctl status docker

########################################
# INSTALL AND RUN MYSQL DOCKER
# CREATING DATABASE & PERMISSIONS
########################################
docker pull mysql
docker run --name mysql_container -h 127.0.0.1 -p 3306:3306 -d -e MYSQL_ROOT_PASSWORD=temp123 mysql
docker exec -it mysql_container bash 

# Attendre quelques secondes que la base se lance
mysql -u root -ptemp123 
# Then copy paste the scripts/init_opa_database.sql
# then exit
exit


########################################
# install python requirements contrab & init
########################################
cd setup
chmod 755 *
pip install -r requirements.txt 
./init_crontab.sh
pkill -f get_stream_data.py
python3 get_stream_data.py </dev/null &>/dev/null &
pkill -f get_historical_data.py
python3 get_historical_data.py  </dev/null &>/dev/null &
