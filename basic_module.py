#!/usr/bin/python  
 
from ansible.module_utils.basic import *                         # Step 1
 
def main(): 
 
    module = AnsibleModule(argument_spec={})                    # Step 2
    rc, out, err = module.run_command(['/usr/bin/uname', '-a']) # Step 3 
    module.exit_json(changed=False, meta=out)                   # Step 4
 
if __name__ == "__main__":
 
    main()
