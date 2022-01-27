import psutil

with open('script.txt', 'w') as f:
  for pid in psutil.pids():
    p = psutil.Process(pid=pid)
    if p.status() == 'running' and p.pid == pid:
      f.write(s)

