# Implemented ARP Cache Manipulation to Identify and Analyze Network Vulnerabilities

## Description

The **Address Resolution Protocol (ARP)** is a communication protocol used for discovering the link layer address (e.g., MAC address) given an IP address. The ARP protocol is simple and lacks inherent security features, making it vulnerable to attacks.

One such attack is **ARP cache poisoning**, a common method of exploiting the ARP protocol. In this attack, attackers forge IP-to-MAC mappings to mislead the victim into accepting incorrect mappings. As a result, network traffic can be redirected to an attacker’s device, allowing for potential **Man-in-the-Middle (MITM)** attacks.

![ARP Poisoning](https://github.com/user-attachments/assets/374e63f4-0121-407a-9cb5-c2c6c2aff12f)

## Languages and Utilities Used

- **Python**
- **Ubuntu 20.04 VM**

## Environments Used

- **Windows 10** (21H2)

## Lab Topics Covered

- **ARP Cache Poisoning**
- **MITM Attack on Telnet using ARP Cache Poisoning**
- **MITM Attack on Netcat using ARP Cache Poisoning**

## Shell Scripts and Commands

- `./dc-build.sh` - Build the Docker images. It can take one additional parameter for the build process, e.g., `./dc-build.sh --no-cache`.
- `./dc-up.sh` - Start the Docker containers in the foreground.
- `./dc-up-d.sh` - Start the Docker containers in the background.
- `./dc-stop.sh` - Stop the Docker containers. It can take one additional parameter for the stop process.
- `./dc-down.sh` - Stop and remove the Docker containers, with an additional parameter for the process.
- `./dc-unittest.sh` - A utility script for running a specific unit test class.

## Program Walk-through:

### Using Scapy for Sniffing and Spoofing

1. **Launching an ARP Cache Poisoning Attack** on a target machine.
2. **MITM Attack on Telnet** using ARP Cache Poisoning.
3. **MITM Attack on Netcat** using ARP Cache Poisoning.

## Conclusion

In this lab, we explored the power of **ARP Cache Poisoning** as an effective method for exploiting network vulnerabilities. By launching **Man-in-the-Middle (MITM)** attacks on protocols like **Telnet** and **Netcat**, we observed how attackers can intercept, redirect, and manipulate network traffic without detection. This demonstrated the critical need for securing the ARP protocol and implementing stronger protections against spoofing and MITM attacks.

### Key Takeaways:
- **ARP Cache Poisoning** remains a significant vulnerability, particularly in environments lacking ARP security measures.
- **MITM attacks** are potent and can be executed silently, making them difficult to detect.
- Awareness and mitigation techniques like **Static ARP Entries** and **Encryption** are essential for protecting sensitive communications.

Through this lab, we gained hands-on experience with the tools and techniques used by attackers, which is vital for building effective defense strategies in real-world networks.

     3. Launching MITM atatck on netcat<br>
 


