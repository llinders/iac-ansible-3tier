def build_customer_env_dir(customer_number: int, env: str) -> str:
    base_dir = f"./deployments/customer_{customer_number}"
    if env == "test":
        return base_dir + "/test"
    elif env == "prod":
        return base_dir + "/prod"
    raise ValueError("Not a valid environment, please choose either 'test' or 'prod'")