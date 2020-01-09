
import argparse
import time
import cpu_control
import IO_control
import memory_control
import network_control

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--style', type=str, default="io",help='default style')#默认的instance
    parser.add_argument('--ips', type=str, default="172.26.0.5",help='default instance')#默认的instance
    parser.add_argument('--namespace', type=str, default="integ1",help='default namespace')#默认的instance
    parser.add_argument('--hour', type=float, default=1.0,help='default hour')#默认的time
    parser.add_argument('--step', type=int, default=30,help='default step')#默认的time
    args = parser.parse_args()
    now_time =time.time()
    time_diff=args.hour*60*60*1
    old_time=now_time-time_diff
    step=args.step
    len_namespace=len(args.namespace.split(','))
    namespace=[]
    for i in range(len_namespace):
        namespace.append(args.namespace.split(',')[i])
    len_ips=len(args.ips.split(','))
    instance=[]
    for i in range(len_ips):
        instance.append(args.ips.split(',')[i]+":9100")
    if args.style=='cpu':
        cpu_control.print_cpu(namespace, old_time, now_time, step)
    elif args.style=='io':
        IO_control.print_io(instance, old_time, now_time, step)
    elif args.style == 'memory':
        memory_control.print_memory(namespace, old_time, now_time, step)
    elif args.style == 'network':
        network_control.print_network(namespace, old_time, now_time, step)
    else:
        print('error, the input style is error')
if __name__ == '__main__':
    main()