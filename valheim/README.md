<img src="https://i.ytimg.com/vi/4k54ppa7es4/maxresdefault.jpg" alt="My cool logo"/>

## Documentation by TheGreatStorm
If your following commands documentation keep in mind we utilize `/opt/server` in the examples make sure this directory exists in your box if you are copy pasting.

## Prerequisites
* Centos 8
    * `sudo yum install epel-release -y`
    * `sudo yum install git ansible glibc.i686 libstdc++.i686 wget -y`
* Ubuntu 64-bit
    * `sudo dpkg --add-architecture i386; sudo apt update; sudo apt install wget tar netcat lib32gcc1 lib32stdc++6 steamcmd lib32z1`

## Commands
* install.yml
  * `ansible-playbook install.yml --extra-vars '{"app_dir":"/opt/server"}'`
* start.yml
  * `ansible-playbook start.yml --extra-vars '{"app_dir":"/opt/server","name":"ServerName","world":"Dedicated","public":"1","password":"secret", "port":"2456"}'`
* stop.yml
  * `ansible-playbook stop.yml`
* restart.yml
  * `ansible-playbook restart.yml --extra-vars '{"app_dir":"/opt/server","name":"ServerName","world":"Dedicated","public":"1","password":"secret", "port":"2456"}'`
* update.yml -- Look at notes for more info before running.
  * `ansible-playbook update.yml --extra-vars '{"app_dir":"/opt/server"}'`

## Notes
* <del>`-public 0` to have no password server, `-public 1` to have a required password server
  * Make sure if you want a public open server, to make `-public 0` and `-password ""`
  * If you use `-public 1` make sure `-password` isn't empty or else you will get a threaded error.</del>
* Public Servers are currently not avaliable.
* I believe the query port to find on steam is +1 from standard port given. This needs to be checked.
* Threaded error happens if you don't have proper environment variables.
* If your going to update your valheim server make sure you run stop.yml first before doing update.yml
* How to make systemd service
  * Helped by gelbbauch
  * ``` cat << EOF > /etc/systemd/system/valheim.service
    [Unit]
    Description=Valheim game server
    
    [Service]
    Type=forking
    ExecStart=/usr/bin/ansible-playbook /opt/server/game-ansible/valheim/start.yml --extra-vars '{"app_dir":"/opt/server","name":"Wastaken","world":"Dedicated","public":"1","password":"4Valhalla!", "port":"2456"}'
    ExecStop=/usr/bin/ansible-playbook /opt/server/game-ansible/valheim/stop.yml
    Type=oneshot
    RemainAfterExit=yes
    
    [Install]
    WantedBy=multi-user.target
    EOF`
    
    then:
    
    systemctl daemon-reload
    
    and
    
    systemctl enable --now valheim.service```