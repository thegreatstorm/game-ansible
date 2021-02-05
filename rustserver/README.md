<img src="https://cdn.akamai.steamstatic.com/steam/apps/252490/header.jpg"/>

## Prerequisites
* Centos 8
    * `sudo yum install epel-release -y`
    * `sudo yum install git ansible python38.x86_64 glibc.i686 libstdc++.i686 wget -y`
* Ubuntu 64-bit
    * `sudo dpkg --add-architecture i386; sudo apt update; sudo apt install wget tar netcat lib32gcc1 lib32stdc++6 steamcmd lib32z1`

## Active Playbooks
* install.yml
* start.yml
* stop.yml
* restart.yml
* update.yml

## Inactive Playbooks
* plugin-install.yml
    * It works, but this may not work for other GameServers
* partial-wipe.yml
    * Testing & arguments need to be created
* wipe.yml
    * Testing & arguments need to be created