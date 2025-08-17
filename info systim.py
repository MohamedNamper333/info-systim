import platform
import os
import socket

print("[+] Gathering system information...\n")
print(f"System: {platform.system()}")
print(f"Node Name: {platform.node()}")
print(f"Release: {platform.release()}")
print(f"Version: {platform.version()}")
print(f"Machine: {platform.machine()}")
print(f"Processor: {platform.processor()}")
print(f"IP Address: {socket.gethostbyname(socket.gethostname())}")
print(f"Current User: {os.getlogin()}")