#!/usr/bin/python3
 
 
from ansible.module_utils.basic import *
 
try:
    import json
except ImportError:
    import simplejson as json
 
 
def write_to_file(module, hostname, hostname_file):
 
    try:
        with open(hostname_file, 'w+') as f:
            try:
                f.write("%s\n" %hostname)
            finally:
                f.close()
    except Exception:
        err = str(get_exception())
        module.fail_json(msg="failed to write to the /etc/hostname file ${0}".format(err))
 
def main():
 
    hostname_file = '/etc/hostname'
    module = AnsibleModule(argument_spec=dict(name=dict(required=True, type=str)))
    name = module.params['name']
    write_to_file(module, name, hostname_file)
    module.exit_json(changed=True, meta=name)
 
if __name__ == "__main__":
 
    main()
