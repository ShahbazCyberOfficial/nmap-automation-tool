import subprocess
print(""" 
=====================================================
            NMAP AUTOMATION TOOL v1.0
=====================================================

Developed by: Shahbaz Bhutta

This tool performs:
✔ SYN Scan
✔ Service Version Detection
✔ OS Detection
✔ Aggressive Scan
✔ Saves the report automatically

Only enter:
1. Target IP Address
2. Report File Name

=====================================================
Important Note:

This tool performs multiple Nmap scans and gathers detailed information about the target. Depending on the target and network conditions, the scan may take some time to complete.

Please be patient and wait until the scan finishes.
""")
try:
 target=input("Enter the target IP adress: ")
 filename=input("Enter the filename to save the sacn results: ")
 print("Please wait while the target IP is being scanned aggressively..........")   
 print("Scan Started...")
 subprocess.run(["nmap","-sS","-sV","-O","-p-","-A",target,"-oN",filename])

except Exception as e:
 print(e)
else:
  print("Scan Completed Successfully.")
  print("your sacan result have been successfully saved to: ",filename)
  print("Thanks using for this automation tool")
