########################################
# INSTALL AND RUN MYSQL DOCKER
########################################
docker pull mysql:latest
docker run --name mysql_container -h 127.0.0.1 -p 3306:3306 -v mysql_volume:/var/lib/mysql/ -d -e MYSQL_ROOT_PASSWORD=temp123 mysql


########################################
# CREATING DATABASE & PERMISSIONS
########################################
docker exec -it mysql_container bash 
mysql -u root -ptemp123 

# Then copy paste the init_opa_database.sql


########################################
# reinstall OpenSSl
########################################
sudo rm -rf /usr/lib/python3/dist-packages/OpenSSL
sudo pip3 install pyopenssl
sudo pip3 install pyopenssl --upgrade

########################################
# install python requirements
########################################
pip install -r requirements.txt 


########################################
# Launch stream and historical script 
########################################
Come back to BinBot/ then launch start.sh

