import subprocess
import concurrent.futures
import os
import ipaddress

def run_nmap_scan(target_ip, port_range='22-443', scan_delay="1s", decoy=False, randomize=False):
    """
    Runs an Nmap scan on the specified target IP with stealth scanning techniques,
    including OS and version detection.
    """
    print(f"Scanning {target_ip} with Nmap...\n")
    
    # Build the Nmap command with stealthy options
    command = f"nmap -sS -sV -O -T2 --scan-delay {scan_delay} -p {port_range} {target_ip}"  # Stealth scan options

    # Add decoy scan option if enabled
    if decoy:
        command += " -D RND:10"  # Use 10 random decoys

    # Add random host scan option if enabled
    if randomize:
        command += " --randomize-hosts"

    # Execute the Nmap command
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    return result.stdout  # Return scan results as text

def scan_multiple_targets(targets, port_range='22-443', scan_delay="1s", decoy=False, randomize=False):
    """
    Scans multiple targets concurrently with stealthy options.
    """
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Run scans for each target concurrently
        results = list(executor.map(lambda target: run_nmap_scan(target, port_range, scan_delay, decoy, randomize), targets))
    return results

def get_ip_range(start_ip, end_ip):
    """
    Returns a list of IP addresses in the specified range.
    """
    start = ipaddress.IPv4Address(start_ip)
    end = ipaddress.IPv4Address(end_ip)
    
    return [str(ip) for ip in ipaddress.IPv4Network(f"{start_ip}/{end - start + 1}", strict=False).hosts()]

def get_network_ips(network):
    """
    Returns a list of IP addresses in the given network.
    """
    return [str(ip) for ip in ipaddress.IPv4Network(network).hosts()]

if __name__ == "__main__":
    # Ask the user for the scanning method (single IP, range, or network)
    scan_type = input("Choose scan type (1: Single IP, 2: IP Range, 3: Network): ")

    targets = []
    if scan_type == '1':
        target = input("Enter target IP address: ")
        targets.append(target)
    elif scan_type == '2':
        start_ip = input("Enter start IP address of the range: ")
        end_ip = input("Enter end IP address of the range: ")
        targets = get_ip_range(start_ip, end_ip)
    elif scan_type == '3':
        network = input("Enter the network (e.g., 192.168.1.0/24): ")
        targets = get_network_ips(network)
    else:
        print("Invalid choice. Exiting.")
        exit(1)

    # Optionally, allow the user to specify port range
    port_range = input("Enter the port range to scan (default is 22-443): ") or '22-443'
    
    # Set the save directory for results
    save_directory = "scan_results"  # You can change this to any directory path you want
    
    # Create the directory if it doesn't exist
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)
        print(f"Directory '{save_directory}' created.")
    
    # Ask if the user wants to use stealth features
    scan_delay = input("Enter scan delay (default is 1s): ") or '1s'
    decoy = input("Use decoy (yes/no, default is no): ").lower() == 'yes'
    randomize = input("Randomize host order (yes/no, default is no): ").lower() == 'yes'
    
    # Run the scan concurrently
    scan_results = scan_multiple_targets(targets, port_range, scan_delay, decoy, randomize)
    
    # Print and save scan results
    for i, result in enumerate(scan_results):
        print(f"\nScan Results for {targets[i]}:")
        print(result)

        # Save each result to a separate file in the specified directory
        result_file_path = os.path.join(save_directory, f"nmap_scan_results_{targets[i].replace('.', '_')}.txt")
        
        with open(result_file_path, "w") as file:
            file.write(result)
        print(f"Results for {targets[i]} saved to '{result_file_path}'.")
    
    print("\nScan complete!")
