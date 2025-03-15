# ZeroTrace: All-in-One Automated Penetration Testing System

## Project Overview

ZeroTrace is an all-in-one automated penetration testing system designed to integrate a variety of scanning, exploitation, and reporting tools into a single framework. It helps penetration testers and security professionals to conduct thorough and efficient vulnerability assessments, exploit vulnerabilities, and generate detailed reports of their findings.

ZeroTrace includes:

- **Network Scanning**: Scans for devices and services on a network.
- **Web Application Security Scanning**: Scans websites for common vulnerabilities like SQL injection, XSS, and more.
- **Exploit Module**: Leverages Metasploit to exploit vulnerabilities.
- **Reporting**: Generates JSON, HTML, and PDF reports summarizing scan results.

## Features

- **Automated Vulnerability Scanning**: For network and web applications.
- **Exploitation Module**: Uses Metasploit to attempt to exploit discovered vulnerabilities.
- **Reporting System**: Generates detailed scan reports in multiple formats (JSON, HTML, PDF).
- **Easy-to-Use Interface**: Simple command-line interaction for penetration testers.
- **Extendable**: New modules and features can be easily integrated into the system.

## Tools Integrated

### 1. **Nmap** - Network Scanning
   - Purpose: Performs network discovery and security auditing. Identifies devices, services, and vulnerabilities.
   - Features: OS detection, version detection, and port scanning using stealth techniques (e.g., SYN scan).
   - Integration: Used for discovering devices and services on a network, supporting detailed reconnaissance.

### 2. **Nikto** - Web Application Security Scanning
   - Purpose: An open-source web server scanner that detects vulnerabilities in web applications.
   - Features: Scans for issues like outdated server software, vulnerable scripts, and misconfigurations.
   - Integration: Used to scan websites for vulnerabilities, including SQL injection and XSS.

### 3. **SQLMap** - SQL Injection Scanning
   - Purpose: Automates the process of detecting and exploiting SQL injection vulnerabilities.
   - Features: Detects and exploits SQL injections, enumerates databases, and dumps data.
   - Integration: Used to scan web applications for SQL injection vulnerabilities and automate exploitation.

### 4. **XSStrike** - Cross-Site Scripting (XSS) Scanning
   - Purpose: Detects and exploits XSS vulnerabilities in web applications.
   - Features: Advanced techniques for detecting and exploiting XSS vulnerabilities.
   - Integration: Scans websites for potential XSS issues and attempts exploitation.

### 5. **Metasploit Framework** - Exploit Module
   - Purpose: A tool for developing and executing exploits against remote targets.
   - Features: Automates the exploitation of vulnerabilities to gain unauthorized access.
   - Integration: Uses Metasploit for exploiting identified vulnerabilities in networks and web applications.

## Installation and Setup

### System Requirements

- **OS**: Ubuntu (or compatible Linux distribution)
- **Python**: Python 3.x
- **Required Tools**:
  - **Nmap**: For network scanning and OS detection.
  - **Nikto**: For web application vulnerability scanning.
  - **SQLMap**: For SQL injection testing.
  - **XSStrike**: For XSS vulnerability testing.
  - **Metasploit Framework**: For exploitation.
- **Dependencies**:
  - Python libraries (e.g., subprocess, json, fpdf for generating reports)
  - Install necessary tools like Nmap, SQLMap, XSStrike, Metasploit.

### Install Dependencies

1. **Clone the repository**:

   ```bash
   git clone https://github.com/LuckyStail/ZeroTrace.git

2. **Install Python dependencies:**
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

3. **Install the tools: Nmap,SQLMap,XXStrike,Metasploit**
    sudo apt install nmap
    git clone https://github.com/sqlmapproject/sqlmap.git
    git clone https://github.com/s0md3v/XSStrike.git

4. **Setting Up the Exploit Module (Metasploit)**
    msfdb init

## File Structure

    ZeroTrace/
    │
    ├── network_scanner.py         # Main scanner script
    ├── sql_injection_scanner.py   # SQL injection scanning with SQLMap
    ├── xss_scanner.py             # XSS scanning with XSStrike
    ├── exploit_module.py          # Metasploit exploitation module
    ├── report_generator.py        # For generating scan reports (JSON, HTML, PDF)
    ├── README.md                  # Project documentation
    ├── requirements.txt           # Python dependencies
    └── scan_results/              # Directory for storing scan result files

## Reporting

    ZeroTrace generates detailed reports in multiple formats:

    JSON: Machine-readable format for further analysis.
    HTML: Human-readable format for viewing in a browser.
    PDF: Portable format suitable for sharing.

    Reports are automatically generated and saved in the scan_results/ directory after each scan. You can customize the report generation by modifying the report_generator.py script


## Conclusion

    ZeroTrace is a powerful, modular, and easy-to-use automated penetration testing system. It integrates various scanning and exploitation tools into a unified platform, providing an efficient and streamlined process for vulnerability discovery and exploitation.

    By generating comprehensive reports in multiple formats, it simplifies the documentation process for penetration testers, making it an invaluable tool for both manual and automated testing.

## Contributing

    ZeroTrace is an open-source project, and contributions are welcome! If you'd like to contribute:

    1. Fork the repository.
    2. Make your changes.
    3. Submit a pull request.


## License 
    This project is licensed under the MIT License. 



### Explanation of Updates:

- **Tools Integrated**:
## 1 Nmap - Network Scanner
📌 Purpose:

   Nmap (Network Mapper) is used for network discovery, host detection, port scanning, and OS fingerprinting.
   It identifies active hosts, running services, open ports, and their versions.
   🔹 Features:
   ✔ Fast and customizable network scanning
   ✔ Detects open ports, services, and OS details
   ✔ Supports stealth scanning techniques
   
   **🛠 Integration in ZeroTrace:**
   
   Used in the network_scanner.py module to scan single IPs, ranges, or entire subnets.
   Utilizes -sS (stealth scan), -O (OS detection), -sV (service version detection), and --randomize-hosts for evasion.
## 2 Nikto - Web Vulnerability Scanner
📌 Purpose:

   Scans websites for security misconfigurations and known vulnerabilities.
   Detects outdated software, insecure HTTP headers, and common security flaws.
   🔹 Features:
   ✔ Detects over 6,700 vulnerabilities
   ✔ Identifies outdated software versions
   ✔ Scans HTTP headers, cookies, and SSL/TLS configurations
   
   **🛠 Integration in ZeroTrace:**
   
   Used in the web_scanner.py module to check for web application vulnerabilities.
   Executes nikto -h <target> and parses the results.
## 3 SQLmap - SQL Injection Testing
📌 Purpose:

   Automates the process of detecting and exploiting SQL injection vulnerabilities.
   🔹 Features:
   ✔ Supports multiple database types (MySQL, PostgreSQL, MSSQL, etc.)
   ✔ Can extract database information, dump tables, and escalate privileges
   ✔ Supports blind, time-based, and error-based injection techniques
   
   **🛠 Integration in ZeroTrace:**
   
   Used in the sql_scanner.py module to test for SQL vulnerabilities in web apps.
   Executes sqlmap -u <target_url> --dbs --batch for automated testing.
## 4 XSStrike - Cross-Site Scripting (XSS) Scanner
📌 Purpose:

   Detects and exploits XSS vulnerabilities in web applications.
   🔹 Features:
   ✔ Identifies both reflected and stored XSS attacks
   ✔ Generates custom payloads to bypass WAFs
   ✔ Uses AI-based detection methods
   
   **🛠 Integration in ZeroTrace:**
   
   Used in the xss_scanner.py module for automated web security assessments.
   Executes xsstrike -u <target_url> -f to detect XSS vulnerabilities.
## 5 Metasploit Framework - Exploitation Module
📌 Purpose:

   A powerful tool used for penetration testing and exploitation of vulnerabilities.
   Provides various exploits, payloads, and post-exploitation modules.
   🔹 Features:
   ✔ Automated exploits for known vulnerabilities
   ✔ Post-exploitation modules for privilege escalation
   ✔ Can be combined with Nmap scans to target vulnerable services
   
 **🛠 Integration in ZeroTrace:**
   
   Used in exploit_module.py to run Metasploit exploits against detected vulnerabilities.
   Executes msfconsole -x "use exploit/multi/...; set RHOST <target>; exploit" for automated attacks.
- **Installation and Setup**: Expanded to include steps for setting up all required dependencies, including Python dependencies and external tools like Nmap, SQLMap, XSStrike, and Metasploit.
- **Usage Instructions**: Prerequisites

Before running ZeroTrace, ensure you have the following installed:

Python (Recommended: Python 3.x)

Required dependencies (Install using pip install -r requirements.txt)

Administrative privileges (some scans require root access)

## Running ZeroTrace

Clone the Repository (if not already done): git clone https://github.com/LuckyStail/ZeroTrace.git
cd zerotrace

2. Set Up the Virtual Environment (Recommended): python3 -m venv venv
                                                 source venv/bin/activate  # Linux/macOS
                                                 venv\Scripts\activate  # Windows

3. Install Dependencies: pip install -r requirements.txt

4.  Run ZeroTrace: python ZeroTrace.py

## Choosing the Scan Type

      After starting ZeroTrace, you will be prompted to choose a scan type:
      
      Network Scan - Identifies live hosts and open ports.
      
      Vulnerability Scan - Detects known vulnerabilities in target systems.
      
      Web Scan - Scans web applications for security flaws.
      
      Exploit Execution - Attempts known exploits against detected vulnerabilities.
      
      Custom Scan - Allows user-defined scanning parameters.


## Setting Scan Options

      Each scan type has specific options you can configure:
      
      Target IP/Domain: Provide the IP address or domain of the target.
      
      Port Range: Specify ports to scan (e.g., 80,443 or 1-65535).
      
      Scan Depth: Choose between a quick scan or an in-depth analysis.
      
      Output Format: Select output type (text, JSON, or HTML report).

## Viewing Reports

      Scan results are stored in the reports/ directory. Open the report file using: cat reports/scan_results.txt  # Text output
jq . reports/scan_results.json  # JSON output
firefox reports/scan_results.html  # HTML output

## Conclusion

ZeroTrace is a powerful, all-in-one pentesting tool designed to streamline security assessments. With its automated scanning, vulnerability detection, and exploit execution capabilities, it provides security professionals with a comprehensive suite for penetration testing. Whether you're conducting quick reconnaissance or deep security analysis, ZeroTrace equips you with the necessary tools to uncover and address potential threats efficiently.



Feel free to modify and expand the `README.md` as needed to reflect any additional functionality or updates in your project.
