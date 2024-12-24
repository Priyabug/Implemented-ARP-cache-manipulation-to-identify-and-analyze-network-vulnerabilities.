<h1>Implemented-ARP-cache-manipulation-to-identify-and-analyze-network-vulnerabilities.</h1>



<h2>Description</h2>
The Address Resolution Protocol (ARP) is a communication protocol used for discovering the link layer
address, such as the MAC address, given an IP address. The ARP protocol is a very simple protocol, and
it does not implement any security measure. The ARP cache poisoning attack is a common attack against
the ARP protocol. Using such an attack, attackers can fool the victim into accepting forged IP-to-MAC
mappings. This can cause the victim’s packets to be redirected to the computer with the forged MAC
address, leading to potential man-in-the-middle attacks.
<br />

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Languages and Utilities Used</title>
</head>
<body>
<h2>2. Languages and Utilities Used</h2>

    <ul>
        <li>
            <strong>Python:</strong> Used to write scripts for ARP packet crafting, spoofing, and sniffing using Scapy.
        </li>
        <li>
            <strong>Shell scripting:</strong> To interact with Docker and network utilities like <code>tcpdump</code>, <code>sysctl</code>, etc.
        </li>
    </ul>

    <ul>
        <li>
            <strong>Scapy:</strong> A Python library for crafting and analyzing network packets.
        </li>
        <li>
            <strong>tcpdump:</strong> For packet sniffing.
        </li>
        <li>
            <strong>Docker:</strong> To create and manage the virtualized lab environment.
        </li>
        <li>
            <strong>Wireshark:</strong> For packet analysis.
        </li>
        <li>
            <strong>Telnet and Netcat:</strong> For communication between hosts.
        </li>
    </ul>
</body>
</html>

    <h2>3. Environments Used</h2>
    <ul>
        <li>
            <strong>SEED Ubuntu 20.04 VM:</strong>
            <ul>
                <li>Pre-configured with necessary tools, aliases, and scripts.</li>
                <li>Supports containerized setups.</li>
            </ul>
        </li>
        <li>
            <strong>Docker:</strong>
            <ul>
                <li>Used to create isolated environments for the attacker (Host M) and victims (Hosts A and B).</li>
                <li>Lab network: <code>10.9.0.0/24</code>.</li>
            </ul>
        </li>
        <li>
            <strong>Docker Compose:</strong>
            <ul>
                <li>Simplifies container management using the <code>docker-compose.yml</code> file.</li>
            </ul>
        </li>
    </ul>

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
 

- <b> Writing C Programs for Sniffing and Spoofing:</b>
 
     1. Tasks in this set involve writing programs in C to manually implement packet sniffing and spoofing, allowing students to understand the
          low-level implementation details of these techniques.<br>

