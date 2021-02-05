<img src="https://cdn.akamai.steamstatic.com/steam/apps/252490/header.jpg"/>

## Documentation by TheGreatStorm
If your following commands documentation keep in mind we utilize `/opt/server` in the examples make sure this directory exists in your box if you are copy pasting.


## Prerequisites
* Centos 8
    * `sudo yum install epel-release -y`
    * `sudo yum install git ansible python38.x86_64 glibc.i686 libstdc++.i686 wget -y`
* Ubuntu 64-bit
    * `sudo dpkg --add-architecture i386; sudo apt update; sudo apt install wget tar netcat lib32gcc1 lib32stdc++6 steamcmd lib32z1`

## Commands
* install.yml
  * `ansible-playbook install.yml --extra-vars '{"app_dir":"/opt/server"}'`
* start.yml
  * `ansible-playbook start.yml --extra-vars '{"app_dir":"/opt/server","server_port":"28015", "hostname":"game-ansible", "identity":"ansible", "seed":"55", "players":"50","worldsize":"3300","rcon_port":"28016","rcon_password":"secret","description":"Ran with Ansible","header_image":"","app_port":"28016"}'`
* stop.yml
  * `ansible-playbook stop.yml`
* restart.yml
  * `ansible-playbook restart.yml --extra-vars '{"app_dir":"/opt/server","server_port":"28015", "hostname":"game-ansible", "identity":"ansible", "seed":"55", "players":"50","worldsize":"3300","rcon_port":"28016","rcon_password":"secret","description":"Ran with Ansible","header_image":"","app_port":"28016"}'`
* update.yml
  * `ansible-playbook update.yml --extra-vars '{"app_dir":"/opt/server"}'`
  * <i>Requires the game server to be shut down.</i>
* mod_install.yml
  * `ansible-playbook plugin_install.yml --extra-vars '{"app_dir":"/opt/server"}'`
  * <i>Installs oxide, you will see the oxide server under rust server directory once you restart or start the instance.</i>
* plugin_install.yml 
  * `ansible-playbook plugin_install.yml --extra-vars '{"app_dir":"/opt/server","plugin_name":"NTeleportation"}'`
  * <i>Oxide should automatically pick up the new plugin, if you have an existing plugin and trying to upgrade remove existing one first.</i>
* partial_wipe.yml
  * `ansible-playbook partial_wipe.yml --extra-vars '{"app_dir":"/opt/server"}'`
  * <i>Wipes map, and sav files.</i>
* full_wipe.yml
  * `ansible-playbook partial_wipe.yml --extra-vars '{"app_dir":"/opt/server"}'`
  * <i>Wipes out everything, including blueprints. This does not wipe out modded information.</i>

## Notes
No notes