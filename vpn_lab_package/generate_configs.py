import csv
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('router_template.j2')

with open('routers.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        config = template.render(
            router_name=row['router_name'],
            role=row['role'],
            public_ip=row['public_ip'],
            tunnel_ip=row['tunnel_ip'],
            lan_ip=row['lan_ip'],
            peer_public_ip=row['peer_public_ip'],
            peer_tunnel_ip=row['peer_tunnel_ip'],
            peer_lan_ip=row['peer_lan_ip']
        )
        filename = f"{row['router_name']}_config.txt"
        with open(filename, 'w') as f:
            f.write(config)
        print(f"Generated {filename}")
