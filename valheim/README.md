<img src="https://i.ytimg.com/vi/4k54ppa7es4/maxresdefault.jpg" alt="My cool logo"/>

## Documentation by TheGreatStorm
If your following commands documentation keep in mind we utilize `/opt/server` in the examples make sure this directory exists in your box if you are copy pasting.

## Commands
* install.yml
  * `ansible-playbook game-ansible/valheim/install.yml --extra-vars '{"app_dir":"/opt/server"}'`
* start.yml
  * `ansible-playbook start.yml --extra-vars '{"app_dir":"/opt/server","name":"ServerName","world":"Dedicated","public":"1","password":"secret", "port":"2456""}'`

## Notes
* Issues with Password and Server staying up
  * `If you leave the password empty or remove it from the start up command it causes the server to crash`
* I believe the query port to find on steam is +1 from standard port given. This needs to be checked.
