# Portainer Stack Deploy

Action to deploy a docker compose stack to a Portainer instance

## Usage

The bare minimum for a stack to be deployed

```yml
name: Example action
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - uses: rrennoir/portainer-stack@v1
        with:
          portainerUrl: ${{ secrets.PORTAINER_URL }}
          portainerUsername: ${{ secrets.PORTAINER_USERNAME }}
          portainerPassword: ${{ secrets.PORTAINER_PASSWORD }}
          portainerEndpointId: 2
          stackName: example-stack
          stackType: 2
          composeFile: tests/docker-compose.yml
```

## Variables

| Name | Description | Default | Required |
| --- | --- | --- | --- |
| portainerUrl | Url of the portainer instance | | yes |
| portainerUsername | Username to login to the Portainer API | | yes |
| portainerPassword | Password to login to the Portainer API | | yes |
| portainerEndpointId | Portainer endpoint to use (usually 2) | 1 | no |
| stackName | Name of the stack to create / update / delete  | | yes |
| stackType | Type of stack (1 swarm, 2 compose, 3 kubernetes) | 1 | no |
| composeFile | Path to the compose file | | yes |
| prune | Remove obsolete services | false | no |
| pullImage | Force repulling imagees | false | no |
| delete | Delete the stack instead of creating / updating | false | no |
| verifySSL | Verify the SSL cerficate, useful when the certificate is auto signed | false | no |

## Examples

Checkout the [test action](.github/workflows/test.yml) for example on how to create, update and delete a stack.
