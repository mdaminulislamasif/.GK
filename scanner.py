import os
import socket

def get_local_ip():
    # আপনার ফোনের বর্তমান লোকাল আইপি খুঁজে বের করে
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

def auto_scan():
    print("--- XENO_OS AUTO-SCAN INITIATED ---")
    local_ip = get_local_ip()
    
    if local_ip == '127.0.0.1':
        print("[!] No network connection found.")
        return

    # IP-র শেষ অংশ কেটে রেঞ্জ তৈরি করা (যেমন: 192.168.1.45 -> 192.168.1.0/24)
    ip_parts = local_ip.split('.')
    ip_parts[-1] = '0/24'
    target_range = '.'.join(ip_parts)
    
    print(f"[*] Your Local IP: {local_ip}")
    print(f"[*] Target Range Detected: {target_range}")
    print("[*] Scanning for active devices... Please wait.")
    
    # Nmap দিয়ে স্ক্যান রান করা
    os.system(f"nmap -sn {target_range}")

if __name__ == "__main__":
    auto_scan()

