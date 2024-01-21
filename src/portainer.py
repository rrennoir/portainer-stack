import requests
from typing import List, Any
from dataclasses import dataclass

@dataclass
class PortainerStack:

    portainerUrl: str
    portainerApikey: str
    portainerEndpointId: int
    stackName: str
    stackType: int
    composeFile: str
    prune: bool
    pullImage: bool
    delete: bool
    verifySSL: bool

    @property
    def apiUrl(self) -> str:
        return f"{self.portainerUrl}/api"

    def deployStack(self) -> None:

        token = self.portainerApikey

        header = {
                    "Content-Type": "application/json",
                    "X-API-Key": f"{token}"
                 }

        stack_id = self.getStackIdByName(header)

        if self.delete:
            print("Deleting stack")
            if stack_id != -1:
                self.deleteStack(header, stack_id)
            return

        composeContent = ""
        with open(self.composeFile, "r") as fp:
            composeContent = fp.read()

        if stack_id != -1:
            print("Updating stack")
            self.updateStack(header, stack_id, composeContent)
        else:
            print("Creating stack")
            self.createStack(header, composeContent)

    def login(self) -> str:

        auth_json = {
                    "username": self.portainerUsername,
                    "password": self.portainerPassword
                }

        login_request = requests.post(f"{self.apiUrl}/auth", json=auth_json, verify=self.verifySSL)
        if login_request.status_code != 200:
            print(f"Failed to login {login_request.status_code}: {login_request.text}")
            exit(1)

        return login_request.json()["jwt"]

    def listStacks(self, header: dict[str, str]) -> List[dict[str, Any]]:

        stacks_request = requests.get(f"{self.apiUrl}/stacks", headers=header, verify=self.verifySSL)
        if stacks_request.status_code != 200:
            print(f"Failed to list stacks, {stacks_request.status_code}: {stacks_request.text}")

        return stacks_request.json()

    def getStackIdByName(self, header: dict[str, str]) -> int:

        stacks = self.listStacks(header)
        for stack in stacks:
            if stack["Name"] == self.stackName:
                return stack["Id"]

        return -1

    def createStack(self, header: dict[str, str], composeContent: str) -> None:

        create_data = {
                "name": self.stackName,
                "swarmID": str(self.portainerEndpointId),
                "stackFileContent": composeContent
            }
        create_request = requests.post(
                f"{self.apiUrl}/stacks?type={self.stackType}&method=string&endpointId={self.portainerEndpointId}",
                headers=header,
                json=create_data,
                verify=self.verifySSL)

        if create_request.status_code != 200:
            print(f"Failed to create stack, {create_request.status_code}: {create_request.text}")
            exit(1)


    def updateStack(self, header: dict[str, str], stackId: int, composeContent: str) -> None:

        update_data = {
                "prune": True,
                "pullImage": True,
                "stackFileContent": composeContent
            }

        update_request = requests.put(
                f"{self.apiUrl}/stacks/{stackId}?endpointId={self.portainerEndpointId}",
                headers=header,
                json=update_data,
                verify=self.verifySSL)

        if update_request.status_code != 200:
            print(f"Failed to update stack, {update_request.status_code}: {update_request.text}")
            exit(1)

    def deleteStack(self, header: dict[str, str], stackId: int) -> None:

        del_request = requests.delete(
                f"{self.apiUrl}/stacks/{stackId}?external=false&endpointId={self.portainerEndpointId}",
                headers=header,
                verify=self.verifySSL)

        if del_request.status_code != 204:
            print(f"Failed to delete stack, {del_request.status_code} {del_request.text}")
            exit(1)

