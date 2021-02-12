<img src="https://static.wikia.nocookie.net/terraria_gamepedia/images/a/a4/NewPromoLogo.png/revision/latest/scale-to-width-down/486?cb=20200506135559" alt="My cool logo"/>

## Documentation by TheGreatStorm
If your following commands documentation keep in mind we utilize `/opt/server` in the examples make sure this directory exists in your box if you are copy pasting.

## Prerequisites
* Centos 8
    * `sudo yum install epel-release -y`
    * `sudo yum install git ansible wget glibc.i686 libstdc++.i686 unzip -y`

## Commands
* install.yml
  * `ansible-playbook install.yml --extra-vars '{"app_dir":"/opt/server"}'`

# Port default
* Default port is `7777 (TCP/UDP)`
  
## Notes
* Change Configurations
    * Look for minecraft folder and edit the server.properties.
* Bedrock Edition
    * Just do the ports for bedrock in server.properties.