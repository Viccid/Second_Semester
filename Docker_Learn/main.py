import time

try:
    while True:
        print("Hello")
        time.sleep(2)
except KeyboardInterrupt:
    print("\nScript interrupted")
