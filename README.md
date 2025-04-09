

# Implemented ARP Cache Manipulation to Identify and Analyze Network Vulnerabilities

---

## 📝 **Description**

The **Address Resolution Protocol (ARP)** is a communication protocol used for discovering the link layer address (e.g., MAC address) given an IP address. However, ARP lacks inherent security measures, making it vulnerable to attacks. 

One of the common attacks on ARP is **ARP Cache Poisoning**. In this attack, an attacker manipulates the victim's ARP cache by injecting forged IP-to-MAC mappings. This leads to the redirection of network traffic to the attacker’s machine, resulting in **Man-in-the-Middle (MITM)** attacks.

![ARP Poisoning](https://github.com/user-attachments/assets/374e63f4-0121-407a-9cb5-c2c6c2aff12f)

---

## 🛠️ **Languages and Utilities Used**

- **Python**
- **Ubuntu 20.04 VM**

## 🖥️ **Environments Used**

- **Windows 10** (21H2)

---

## 📚 **Lab Topics Covered**

- **ARP Cache Poisoning**
- **MITM Attack on Telnet using ARP Cache Poisoning**
- **MITM Attack on Netcat using ARP Cache Poisoning**

---

## 📝 **Shell Scripts and Commands**

- `./dc-build.sh` - Build the Docker images. It can take an additional parameter for the build process, e.g., `./dc-build.sh --no-cache`.
- `./dc-up.sh` - Start the Docker containers in the foreground.
- `./dc-up-d.sh` - Start the Docker containers in the background.
- `./dc-stop.sh` - Stop the Docker containers. It can take one additional parameter for the stop process.
- `./dc-down.sh` - Stop and remove the Docker containers, with an additional parameter for the process.
- `./dc-unittest.sh` - A utility script for running a specific unit test class.

---

## 🚶‍♂️ **Program Walk-through:**

### **Using Scapy for Sniffing and Spoofing**

1. **Launching an ARP Cache Poisoning Attack** on a target machine.
2. **MITM Attack on Telnet** using ARP Cache Poisoning.
3. **MITM Attack on Netcat** using ARP Cache Poisoning.

---

## 🏁 **Conclusion**

In this lab, we delved deep into **ARP Cache Poisoning**, exploring how attackers can hijack network traffic and perform **Man-in-the-Middle (MITM)** attacks by poisoning ARP caches. We tested this by executing MITM attacks on **Telnet** and **Netcat** protocols.

### **Key Takeaways:**

- **ARP Cache Poisoning** can be devastating in networks lacking ARP security measures.
- **MITM attacks** are stealthy and can go unnoticed while compromising data.
- To mitigate these attacks, strategies like **Static ARP Entries** and **Encryption** must be employed.

This lab gave us practical experience in exploiting and defending against such attacks, emphasizing the importance of securing the ARP protocol and implementing robust network defenses.

---

🔒 **Security Tip**: Always secure your network traffic by using encrypted protocols (e.g., SSH instead of Telnet) and employ network security tools to prevent ARP spoofing.

 


