<h1>Implemented-ARP-cache-manipulation-to-identify-and-analyze-network-vulnerabilities.</h1>



<h2>Description</h2>
Two key ideas in network security are packet sniffing and spoofing, which pose serious risks to network communication. Understanding these two risks is necessary in order to comprehend networking security protocols. Numerous tools exist for packet sniffing and spoofing, including Wireshark, Tcpdump, Netwox, Scapy, and others. Both attackers and security specialists frequently utilize some of these techniques. While knowing how to use these tools is vital, understanding how they operate—that is, how software implements packet sniffing and spoofing.
<br />


<h2>Languages and Utilities Used</h2>

- <b>Python</b> 
- <b>Ununtu 20.04 VM</b>

<h2>Environments Used </h2>

- <b>Windows 10</b> (21H2)

<h2> Lab topics covered</h2>

- <b>Basics of packet sniffing and spoofing.</b>
- <b>Using the pcap library and Scapy for packet sniffing.</b>
- <b>Using raw sockets and Scapy for packet spoofing.</b>
- <b>Manipulating packets using Scapy.</b>

<h2>Shell scripts commands</h2>

- `./dc-build.sh` - Build the docker images, it can take one additional parameter to be used in the build process, e.g. `./dc-build.sh --no-cache`.
- `./dc-up.sh` - Start the docker containers in the foreground.
- `./dc-up-d.sh` - Start the docker containers in the background.
- `./dc-stop.sh` - Stop the docker containers, it can take one additional parameter to be used in the stop process.
- `./dc-down.sh` - Stop and remove the docker containers, it can take one additional parameter to be used in the stop and remove process.
- `./dc-unittest.sh` - Utility script to aid in running a specific unit test class.

<h2>Program walk-through:</h2>

- <b> Using Scapy for Sniffing and Spoofing:</b>

     1. Sniffing packets with Scapy, including setting filters to capture specific types of packets (like ICMP or TCP).<br>
     2. Spoofing ICMP packets with arbitrary source IP addresses using Scapy.<br>
     3. Implementing a traceroute-like tool using Scapy by manipulating the TTL (Time-To-Live) field in IP packets.<br>
     4. Combining sniffing and spoofing techniques to create a program that automatically sends spoofed ICMP replies.<br>

- <b> Writing C Programs for Sniffing and Spoofing:</b>
 
     1. Tasks in this set involve writing programs in C to manually implement packet sniffing and spoofing, allowing students to understand the
          low-level implementation details of these techniques.<br>

