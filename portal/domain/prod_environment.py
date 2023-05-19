class ProductionEnvironment:
    deployed: bool
    loadbalancer_ip: str
    database_ip: str
    webserver_ips: list

    def __init__(self, deployed: bool, loadbalancer_ip: str, database_ip: str, webserver_ips: list):
        self.deployed = deployed
        self.loadbalancer_ip = loadbalancer_ip
        self.database_ip = database_ip
        self.webserver_ips = webserver_ips