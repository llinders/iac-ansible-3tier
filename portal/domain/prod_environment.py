class ProductionEnvironment:
    files_prepared: bool
    deployed: bool
    loadbalancer_ip: str
    database_ip: str
    webserver_ips: list

    def __init__(self, files_prepared: bool, deployed: bool, loadbalancer_ip: str, database_ip: str, webserver_ips: list):
        self.files_prepared = files_prepared
        self.deployed = deployed
        self.loadbalancer_ip = loadbalancer_ip
        self.database_ip = database_ip
        self.webserver_ips = webserver_ips
    
    def __iter__(self):
        yield 'files_prepared', self.files_prepared
        yield 'deployed', self.deployed
        yield 'loadbalancer_ip', self.loadbalancer_ip
        yield 'database_ip', self.database_ip
        yield 'webservers', self.webserver_ips 