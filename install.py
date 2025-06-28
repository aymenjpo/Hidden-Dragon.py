import os
import time
import sys
from colored import fg, attr
import pyfiglet

# ألوان
RED = fg('red')
GREEN = fg('green')
CYAN = fg('cyan')
YELLOW = fg('yellow')
RESET = attr('reset')

# راية الأداة
os.system("clear")
ascii_banner = pyfiglet.figlet_format("APT Launcher", font="slant")
print(CYAN + ascii_banner + RESET)

# معلومات وهمية للأداة
print(YELLOW + "🔰 Version: 6.9.0-WAR")
print("🛠 Developed by: DDDHHR" + RESET)
print(GREEN + "\n[✔] Initializing core modules...")
time.sleep(1.5)
print("[✔] Loading Kernel Injection Protocols...")
time.sleep(1.5)
print("[✔] Bypassing Android SE-Linux Policy...")
time.sleep(1.5)
print("[✔] Overclocking base CPU level...")
time.sleep(1.5)

# تهديد وهمي
print(RED + "\n⚠️  WARNING: Unauthorized access detected!")
print("⚠️  Activating self-destruct protocol in 60 seconds..." + RESET)
time.sleep(2)

# تشغيل الملف الرئيسي
print(CYAN + "\n🚀 Launching APT.py ...\n" + RESET)
time.sleep(2)

try:
    os.system("python Hidden-Dragonp.py")
except Exception as e:
    print(RED + f"❌ Error launching apt.py: {e}" + RESET)
    sys.exit(1)
