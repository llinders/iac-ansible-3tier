class TestEnvironment:
    deployed: bool
    webserver_ip: str
    database_ip: str

    def __init__(self, deployed: bool, webserver_ip: str, database_ip: str,):
        self.deployed = deployed
        self.webserver_ip = webserver_ip
        self.database_ip = database_ip

    def __iter__(self):
        yield 'deployed', self.deployed
        yield 'webserver_ip', self.webserver_ip
        yield 'database_ip', self.database_ip