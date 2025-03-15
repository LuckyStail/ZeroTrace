import subprocess
import json
import os
from exploit import run_metasploit_exploit
from reporting import generate_json_report, generate_html_report, generate_pdf_report

def run_sqlmap_scan(target_url):
    """Runs an advanced SQL injection scan using SQLmap."""
    print(f"\n[+] Running SQLmap scan on {target_url}...\n")
    command = f"sqlmap -u {target_url} --batch --dbs --level 5 --risk 3 --dump"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

def run_nikto_scan(target_url):
    """Runs a Nikto web vulnerability scan."""
    print(f"\n[+] Running Nikto scan on {target_url}...\n")
    command = f"nikto -h {target_url}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

def run_xss_scan(target_url):
    """Runs an XSS scan using XSStrike."""
    print(f"\n[+] Running XSStrike XSS scan on {target_url}...\n")
    
    # Check if XSStrike is installed
    xsstrike_path = os.path.join(os.path.dirname(__file__), "XSStrike/xsstrike.py")
    if not os.path.exists(xsstrike_path):
        return "[!] XSStrike is not installed. Please install it first."

    command = f"python3 {xsstrike_path} -u {target_url} --crawl"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

def run_exploitation(target_url):
    """Trigger exploitation using Metasploit."""
    exploit_results = run_metasploit_exploit(target_url)
    return exploit_results

if __name__ == "__main__":
    target = input("\nEnter the target website URL (e.g., http://example.com): ")

    print("\nChoose scan type:")
    print("1. SQL Injection Scan (SQLmap)")
    print("2. Web Vulnerability Scan (Nikto)")
    print("3. XSS Scan (XSStrike)")
    print("4. Run All Scans")
    print("5. Exploit Vulnerabilities (Metasploit)")

    choice = input("\nEnter option (1/2/3/4/5): ")

    scan_results = {"target": target}

    if choice == "1":
        sqlmap_results = run_sqlmap_scan(target)
        scan_results["sqlmap_results"] = sqlmap_results
        print("\n[+] SQLmap Scan Results:\n", sqlmap_results)

    elif choice == "2":
        nikto_results = run_nikto_scan(target)
        scan_results["nikto_results"] = nikto_results
        print("\n[+] Nikto Scan Results:\n", nikto_results)

    elif choice == "3":
        xss_results = run_xss_scan(target)
        scan_results["xss_results"] = xss_results
        print("\n[+] XSStrike XSS Scan Results:\n", xss_results)

    elif choice == "4":
        sqlmap_results = run_sqlmap_scan(target)
        nikto_results = run_nikto_scan(target)
        xss_results = run_xss_scan(target)
        scan_results["sqlmap_results"] = sqlmap_results
        scan_results["nikto_results"] = nikto_results
        scan_results["xss_results"] = xss_results
        print("\n[+] SQLmap Scan Results:\n", sqlmap_results)
        print("\n[+] Nikto Scan Results:\n", nikto_results)
        print("\n[+] XSStrike XSS Scan Results:\n", xss_results)

    elif choice == "5":
        exploit_results = run_exploitation(target)
        scan_results["exploit_results"] = exploit_results
        print("\n[+] Exploitation Results:\n", exploit_results)

    else:
        print("\n[!] Invalid option. Exiting...")
        exit()

    # Generate reports
    generate_json_report(scan_results)
    generate_html_report(scan_results)
    generate_pdf_report(scan_results)

    print("\n[+] Reports generated!")
