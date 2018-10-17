nginx role
=========

Install and configure nginx.

Role Variables
--------------

| variable            | possible values | default 
|:--------------------|-----------------|---------
| hello_world_version | 1.0, 1.1        | 1.0     
| hello_world_port    | any number      | 5005    

path are relative to the playbook directory

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
