<img src="https://www.logaster.com/blog/wp-content/uploads/2020/06/image14-3.png" alt="My cool logo"/>

# Current Minecraft Version Supported 1.18.2
## Documentation by TheGreatStorm
If your following commands documentation keep in mind we utilize `/opt/server` in the examples make sure this directory exists in your box if you are copy pasting.

## Prerequisites
* Ubuntu 64-bit
    * `sudo dpkg --add-architecture i386; sudo apt update; sudo apt install ansible wget tar unzip`
    * `Get the latest version of java.`
* Centos 8 - NOT SUPPORTED
    * `sudo yum install epel-release -y`
    * `sudo yum install git ansible java-1.8.0-openjdk wget -y`

## Commands
* install.yml
  * `ansible-playbook install.yml --extra-vars '{"app_dir":"/opt/server"}'`
* start.yml
  * `ansible-playbook start.yml --extra-vars '{"app_dir":"/opt/server","max_memory":"1512","min_memory":"512"}'`
* stop.yml
  * `ansible-playbook stop.yml`
* restart.yml
  * `ansible-playbook start.yml --extra-vars '{"app_dir":"/opt/server","max_memory":"1512","min_memory":"512"}'`

  
  
## Notes
* Change Configurations
    * Look for minecraft folder and edit the server.properties.
* Is this bedrock or java
    * Java Only
* How do I update the minecraft server version
    * Download the server.jar of your version over the existing server.jar. Make a backup of server.jar.