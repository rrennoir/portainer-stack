import os
from portainer import PortainerStack

def main():
    
    stackInfo = PortainerStack(os.environ["INPUT_PORTAINERURL"],
                               os.environ["INPUT_PORTAINERUSERNAME"],
                               os.environ["INPUT_PORTAINERPASSWORD"],
                               int(os.environ["INPUT_PORTAINERENDPOINTID"]),
                               os.environ["INPUT_STACKNAME"], 
                               int(os.environ["INPUT_STACKTYPE"]),
                               os.environ["INPUT_COMPOSEFILE"],
                               bool(os.environ["INPUT_PRUNE"]),
                               bool(os.environ["INPUT_PULLIMAGE"]),
                               bool(os.environ["INPUT_DELETE"]),
                               bool(os.environ["INPUT_VERIFYSSL"]))

    stackInfo.deployStack()

if __name__ == "__main__":
    main()
