<h1>Implemented-ARP-cache-manipulation-to-identify-and-analyze-network-vulnerabilities.</h1>



<h2>Description</h2>
The Address Resolution Protocol (ARP) is a communication protocol used for discovering the link layer
address, such as the MAC address, given an IP address. The ARP protocol is a very simple protocol, and
it does not implement any security measure. The ARP cache poisoning attack is a common attack against
the ARP protocol. Using such an attack, attackers can fool the victim into accepting forged IP-to-MAC
mappings. This can cause the victim’s packets to be redirected to the computer with the forged MAC
address, leading to potential man-in-the-middle attacks.
<br />

<h2>Languages and Utilities Used</h2>

- <b>Python</b> 
- <b>Ununtu 20.04 VM</b>

<h2>Environments Used </h2>

- <b>Windows 10</b> (21H2)

<h2> Lab topics covered</h2>

- <b>ARP Cache Poisoning</b>
- <b>MITM Attack on Telnet using ARP Cache Poisoning</b>
- <b>MITM Attack on Netcat using ARP Cache Poisoning</b>


<h2>Shell scripts commands</h2>

- `./dc-build.sh` - Build the docker images, it can take one additional parameter to be used in the build process, e.g. `./dc-build.sh --no-cache`.
- `./dc-up.sh` - Start the docker containers in the foreground.
- `./dc-up-d.sh` - Start the docker containers in the background.
- `./dc-stop.sh` - Stop the docker containers, it can take one additional parameter to be used in the stop process.
- `./dc-down.sh` - Stop and remove the docker containers, it can take one additional parameter to be used in the stop and remove process.
- `./dc-unittest.sh` - Utility script to aid in running a specific unit test class.

<h2>Program walk-through:</h2>

- <b> Using Scapy for Sniffing and Spoofing:</b>

     1. Launching an ARP cache poisoning attack on a target machine<br>
     2. Launching MITM attack on Telnet.<br>
     3. Launching MITM atatck on netcat<br>
 


