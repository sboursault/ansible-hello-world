hello-world role
=========

Install and start the hello-world service.

Role Variables
--------------

| variable            | example values  | default 
|:--------------------|-----------------|---------
| hello_world_version | 1.0             | ""     


Example Playbook
----------------
    ---
    - hosts: servers
      roles:
        - role: hello-world
          hello_world_version: 1.1
