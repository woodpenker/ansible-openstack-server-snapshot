---
Description:
    -Take a snapshot of the server instance
---
Option:
```
    snapshotname:
        description:
            - Name of the snipshot to the instance
    server:
        description:
            - Name or id of the instance
    timeout:
        description:
            - The amount of time the module should wait for the instance to perform
        required: false
        default: 180
    wait:
        description:
            - If the module should wait for the instance action to be performed.
        required: false
        default: 'yes'
```
---
requriments:
```
    - "python >= 2.6"
    - "shade"
```
---
EXAMPLE:
```
# take a snipshot of the instance
- os_server_snapshot:
    auth:
        auth_url: xxxx
        username: admin
        password: admin
        project_name: admin
    server: test
    snapshotname: test-snapshot-1
    timeout: 200
```
