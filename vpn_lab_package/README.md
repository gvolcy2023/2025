# VPN Lab - Cisco VRF Site-to-Site VPN with OSPF

## 🔧 Topology

```
[LAN A: 192.168.1.0/24] -- RouterA -- Internet -- RouterB -- [LAN B: 192.168.2.0/24]
          |                                |
     Public IP: 1.1.1.1              Public IP: 2.2.2.2
     Tunnel IP: 10.10.10.1           Tunnel IP: 10.10.10.2
```

## 📝 Contents

- `routers.csv`: Defines router data for the VPN setup.
- `templates/router_template.j2`: Jinja2 template for Cisco config.
- `generate_configs.py`: Python script to generate the configs.
- `RouterA_config.txt`, `RouterB_config.txt`: Output configs after script runs.

## ▶️ How to Use

1. Install Jinja2:
   ```bash
   pip install jinja2
   ```

2. Run the script:
   ```bash
   python3 generate_configs.py
   ```

3. The script will read `routers.csv` and generate one config per router.

## ✅ Technologies Used

- Python 3
- Jinja2 templating
- Cisco IOS configuration
- VRF + IPSec + OSPF
