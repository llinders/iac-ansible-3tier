class TestEnvironment:
    deployed: bool
    database_ip: str
    webserver_ip: str

    def __init__(self, deployed: bool, database_ip: str, webserver_ip: str):
        self.deployed = deployed
        self.database_ip = database_ip
        self.webserver_ip = webserver_ip