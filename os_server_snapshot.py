#!/usr/bin/python
# coding : utf-8
#
#

try:
    import shade
    from shade import meta
    HAS_SHADE = True
except ImportError:
    HAS_SHADE = False

DOCUMENTATION = '''
---
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
'''
EXAMPLES = '''
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
'''
def _wait(timeout, cloud, server):
    """Wait for the server to reach the desired state for the given action."""

    for count in shade._utils._iterate_timeout(
            timeout,
            "Timeout waiting for server to complete %s"):
        try:
            server = cloud.get_server(server.id)
        except Exception:
            continue

        if server.status == 'ACTIVE':
            return

        if server.status == 'ERROR':
            module.fail_json(msg="Server reached ERROR state while attempting to %s" % action)

def main():
    argument_spec = openstack_full_argument_spec(
        server=dict(required=True),
        snapshotname=dict(required=True),
    )

    module_kwargs = openstack_module_kwargs()
    module = AnsibleModule(argument_spec, **module_kwargs)

    if not HAS_SHADE:
        module.fail_json(msg='shade is required for this module')

    wait = module.params['wait']
    timeout = module.params['timeout']
    snapshotname = module.params['snapshotname']

    try:
        cloud = shade.openstack_cloud(**module.params)
        server = cloud.get_server(module.params['server'])
        if not server:
            module.fail_json(msg='Could not find server %s' % server)
        status = server.status
        if status != 'ACTIVE':
            module.fail_json(msg='Server is not runinn %s' % server)
        result=cloud.create_image_snapshot(snapshotname,server,wait,timeout)
        if wait:
            _wait(timeout, cloud, server)
            module.exit_json(changed=True, result="created snapshot with id %s" % (result))
    except shade.OpenStackCloudException as e:
        module.fail_json(msg=str(e), extra_data=e.extra_data)
# this is magic, see lib/ansible/module_common.py
from ansible.module_utils.basic import *
from ansible.module_utils.openstack import *
if __name__ == '__main__':
    main()
