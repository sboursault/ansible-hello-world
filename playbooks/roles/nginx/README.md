nginx role
=========

Install and configure nginx.

Role Variables
--------------

| variable              | example values  | default 
|:--------------------  |-----------------|---------
| nginx_config_template | path/to/file.j2 | ""     
| index_html_template   | path/to/file.j2 | ""    


Example Playbook
----------------

### with default configuration

    ---
    - hosts: servers
      roles:
        - role: nginx

### with custom configuration


    ---
    - hosts: servers
      roles:
        - role: nginx
          nginx_config_template: nginx/nginx.conf.j2
          index_html_template: nginx/index.html.j2
