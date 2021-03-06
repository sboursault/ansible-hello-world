nginx role
=========

Install and configure nginx.

Role Variables
--------------

| variable               | example values               | default 
|:--------------------   |-----------------             |---------
| nginx_config_templates | [ "path/to/file.j2", "..." ] | ""     
| nginx_sites_template   | path/to/file.j2              | ""     
| nginx_index_html       | path/to/index.html.j2              | ""     


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
          nginx_config_templates:
            - nginx/nginx_upstream.conf
          nginx_sites_template: nginx/nginx_sites.conf.j2
          nginx_index_html: nginx/index.html.j2
