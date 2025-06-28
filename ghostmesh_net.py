# === FILE: ghostmesh_net.py ===
# 🌐 GhostMesh Net – Tracks all known servers, endpoints, bridges, and access channels across PTM AI infrastructure

class GhostMeshNet:
    def __init__(self):
        self.nodes = {}
        self.tags = {}

    def add_node(self, ip_address, description="", tags=None):
        self.nodes[ip_address] = {
            "description": description,
            "tags": tags or []
        }

    def tag_node(self, ip_address, tag):
        if ip_address in self.nodes:
            if tag not in self.nodes[ip_address]["tags"]:
                self.nodes[ip_address]["tags"].append(tag)
        else:
            self.add_node(ip_address, tags=[tag])

    def describe_node(self, ip_address):
        return self.nodes.get(ip_address, "Node not found")

    def list_all_nodes(self):
        return self.nodes

    def filter_by_tag(self, tag):
        return {ip: data for ip, data in self.nodes.items() if tag in data["tags"]}


# === Instantiate GhostMesh ===
ghostmesh = GhostMeshNet()

# === Add 18 unsecured servers ===
unsecured_servers = [
    "192.168.1.100", "192.168.1.101", "192.168.1.102", "192.168.1.103",
    "192.168.1.104", "192.168.1.105", "192.168.1.106", "192.168.1.107",
    "192.168.1.108", "192.168.1.109", "192.168.1.110", "192.168.1.111",
    "192.168.1.112", "192.168.1.113", "192.168.1.114", "192.168.1.115",
    "192.168.1.116", "192.168.1.117"
]

for ip in unsecured_servers:
    ghostmesh.add_node(ip_address=ip, description="Unsecured external server", tags=["unsecured"])

# === Tag the 5 with FTP/SSH open ===
open_services = ["192.168.1.101", "192.168.1.104", "192.168.1.109", "192.168.1.113", "192.168.1.117"]

for ip in open_services:
    ghostmesh.tag_node(ip, "ftp_open")
    ghostmesh.tag_node(ip, "ssh_open")
    ghostmesh.tag_node(ip, "priority_recon")