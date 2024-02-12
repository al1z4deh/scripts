import argparse



def read_ip_list(file_path):

    ip_list = []

    with open(file_path, 'r') as file:

        for line in file:

            ip_list.append(line.strip())

    return ip_list



def show_ips(ip_list):

    for ip in ip_list:

        parts = ip.split(':')

        if len(parts) > 1:

            print(parts[0])

        else:

            print(ip)



def show_ports(ip_list):

    ports = set()

    for ip in ip_list:

        parts = ip.split(':')

        if len(parts) > 1:

            ports.add(parts[1])

    for port in ports:

        print(f"{port}")



def main():

    parser = argparse.ArgumentParser(description='Show IP addresses or ports.')

    parser.add_argument('-f', '--file', type=str, required=True, help='File containing list of IP addresses with optional ports')



    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument('-i', '--show-ips', action='store_true', help='Show IP addresses')

    group.add_argument('-p', '--show-ports', action='store_true', help='Show ports')



    args = parser.parse_args()



    ip_list = read_ip_list(args.file)



    if args.show_ips:

        show_ips(ip_list)

    elif args.show_ports:

        show_ports(ip_list)



if __name__ == "__main__":

    main()

