# Game Server Ansible Scripts
### Author: TheGreatStorm
Want to learn how to setup game servers? I can help!

### How to use this?
* Create a directory in /opt/server (You can make directory anywhere, but recommended)
  * `mkdir /opt/server` 
* Run install for game server
  * `ansible-playbook <gameserver>/install.yml --extra-vars '{"app_dir":"/opt/server"}'`