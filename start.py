import sys
import subprocess
import threading
import time
import signal

def start_tg_bot():
    try:
        print("Starting telegram bot...")
        subprocess.run(["python", "tg_bot.py"])
    except KeyboardInterrupt:
        print("Telegram bot thread interrupted")

def start_django_server():
    try:
        print("Starting Django Server...")
        subprocess.run([
            "python",
            "manage.py",
            "runserver",
        ])
    except KeyboardInterrupt:
        print("Django server thread interrupted")

def signal_handler(sig, frame):
    print("\nCtrl+C received. Stopping all threads.")
    sys.exit(0)

if __name__ == "__main__":
    # Register the signal handler for Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)
    tg_bot_thread = threading.Thread(target=start_tg_bot)
    django_thread = threading.Thread(target=start_django_server)
    try:
        django_thread.start()
        time.sleep(2)
        tg_bot_thread.start()
        time.sleep(2)
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt. Stopping all threads.")
        sys.exit(0)