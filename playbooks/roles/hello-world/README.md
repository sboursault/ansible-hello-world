hello-world role
=========

Install and start the hello-world service.

Role Variables
--------------

| variable            | possible values | default 
|:--------------------|-----------------|---------
| hello_world_version | 1.0, 1.1        | null (     
| hello_world_port    | any number      | 5005    



Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
        - role: hello-world
          hello_world_version: 1.1
          hello_world_port: 5005

License
-------

MIT
