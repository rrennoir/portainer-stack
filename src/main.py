import os
from portainer import PortainerStack

def main():
    
    stackInfo = PortainerStack(os.environ["INPUT_portainerUrl"],
                               os.environ["INPUT_portainerUsername"],
                               os.environ["INPUT_portainerPassword"],
                               int(os.environ["INPUT_portainerEndpointId"]),
                               os.environ["INPUT_stackName"], 
                               int(os.environ["INPUT_stackType"]),
                               os.environ["INPUT_composeFile"],
                               bool(os.environ["INPUT_prune"]),
                               bool(os.environ["INPUT_pullImage"]),
                               bool(os.environ["INPUT_delete"]),
                               bool(os.environ["INPUT_verifySSL"]))

    stackInfo.deployStack()

if __name__ == "__main__":
    main()
