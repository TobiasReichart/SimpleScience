import random, shutil, time
w, h = shutil.get_terminal_size()
c = [random.randint(0, w) for _ in range(w)]
while True:
    line = "".join("\033[1;32m" + random.choice("0123456789ABCDEF") if i in c else " " for i in range(w))
    print(line)
    c = [(x + random.choice([-1, 0, 1])) % w for x in c]
    time.sleep(0.05)