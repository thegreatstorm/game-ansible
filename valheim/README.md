<img src="https://i.ytimg.com/vi/4k54ppa7es4/maxresdefault.jpg" alt="My cool logo"/>

## Documentation by TheGreatStorm
If your following commands documentation keep in mind we utilize `/opt/server` in the examples make sure this directory exists in your box if you are copy pasting.

## Commands
* install.yml
  * `ansible-playbook install.yml --extra-vars '{"app_dir":"/opt/server"}'`
* start.yml
  * `ansible-playbook start.yml --extra-vars '{"app_dir":"/opt/server","name":"ServerName","world":"Dedicated","public":"1","password":"secret", "port":"2456"}'`
* stop.yml
  * `ansible-playbook stop.yml`

## Notes
* `-public 0` to have no password server, `-public 1` to have a required password server
  * Make sure if you want a public open server, to make `-public 0` and `-password ""`
  * If you use `-public 1` make sure `-password` isn't empty or else you will get a threaded error.
* I believe the query port to find on steam is +1 from standard port given. This needs to be checked.
* Threaded error happens if you don't have proper environment variables.