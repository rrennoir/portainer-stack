import os
from portainer import PortainerStack


def get_bool_env(env_name: str) -> bool:

    input = os.environ[env_name].lower()

    if input not in ["true", "false"]:
        raise ValueError("Invalid argument for bool type, must be true or false")

    return input == "true"

def get_int_env(env_name: str) -> int:

    input = os.environ[env_name]

    if not input.isnumeric():
        raise ValueError("Invalid argument for int type, must be a number")

    return int(input)


def main():
    
    stackInfo = PortainerStack(os.environ["INPUT_PORTAINERURL"],
                               os.environ["INPUT_PORTAINERUSERNAME"],
                               os.environ["INPUT_PORTAINERPASSWORD"],
                               get_int_env("INPUT_PORTAINERENDPOINTID"),
                               os.environ["INPUT_STACKNAME"], 
                               get_int_env("INPUT_STACKTYPE"),
                               os.environ["INPUT_COMPOSEFILE"],
                               get_bool_env("INPUT_PRUNE"),
                               get_bool_env("INPUT_PULLIMAGE"),
                               get_bool_env("INPUT_DELETE"),
                               get_bool_env("INPUT_VERIFYSSL"))

    stackInfo.deployStack()

if __name__ == "__main__":
    main()
