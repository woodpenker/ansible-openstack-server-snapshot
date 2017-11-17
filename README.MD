module: os_server_snapshot
short_description: Take a snapshot of the server instance
version_added: "1.0"
author: "zwuding"
description:
    -Take a snapshot of the server instance
option:
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


requriments:
    - "python >= 2.6"
    - "shade"
---
# take a snipshot of the instance
- os_server_snapshot:
    auth:
        auth_url: xxxx
        username: admin
        password: admin
        project_name: admin
    server: test
    snapshotname: test-snapshpt-1
    timeout: 200
