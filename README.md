# mac_lookup
Dockerized CLI script to pull MAC Address vendor information from macaddress.io.

To install, clone this repository to your local machine, then follow these instructions to run: 

1. Obtain an API key from [https://macaddress.io/api].
2. Add an environment variable named MACADDRESS_IO_API_KEY with the API key you obtained.
3. Build the container with the command: 
```   docker build -t mac_lookup .```
4. Ensure the ```mac_lookup``` command is executable with ```chmod +x mac_lookup```
5. Optionally move ```mac_lookup``` to path directory such as ```/usr/local/bin``` or ```/usr/bin```

Usage: 

```mac_lookup <mac_address>```

<mac_address> can be formatted in any of these formats: 
* XX:XX:XX:XX:XX:XX
* XX-XX-XX-XX-XX-XX
* XXXX.XXXX.XXXX