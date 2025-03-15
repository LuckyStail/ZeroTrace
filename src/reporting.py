import json
import os
from datetime import datetime

def generate_json_report(scan_results, filename="scan_report.json"):
    """Generate a JSON report for the scan results."""
    print(f"\n[+] Generating JSON report: {filename}...")

    # Get the current date and time for report
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report_data = {
        "report_timestamp": timestamp,
        "scan_results": scan_results
    }

    # Save the report in JSON format
    with open(filename, "w") as json_file:
        json.dump(report_data, json_file, indent=4)

    print(f"[+] JSON report saved as {filename}.")

def generate_html_report(scan_results, filename="scan_report.html"):
    """Generate an HTML report for the scan results."""
    print(f"\n[+] Generating HTML report: {filename}...")

    # Start of the HTML file
    html_content = f"""
    <html>
    <head><title>Scan Report</title></head>
    <body>
        <h1>Scan Report</h1>
        <p><strong>Report Generated on:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        <h2>Scan Results</h2>
        <pre>{json.dumps(scan_results, indent=4)}</pre>
    </body>
    </html>
    """

    # Save as an HTML file
    with open(filename, "w") as html_file:
        html_file.write(html_content)

    print(f"[+] HTML report saved as {filename}.")

def generate_pdf_report(scan_results, filename="scan_report.pdf"):
    """Generate a PDF report for the scan results."""
    try:
        from fpdf import FPDF
    except ImportError:
        print("[!] Please install FPDF: 'pip install fpdf'")

    print(f"\n[+] Generating PDF report: {filename}...")

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Scan Report", ln=True, align="C")
    pdf.cell(200, 10, txt=f"Report Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)

    pdf.ln(10)
    pdf.multi_cell(0, 10, txt=json.dumps(scan_results, indent=4))

    pdf.output(filename)
    print(f"[+] PDF report saved as {filename}.")
