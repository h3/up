==
up
==

Directory structure
===================

.. code-block::

    + up/
      - project.yml
      - config.yml
      - templates/
        - alpha.nginx
        - alpha.uwsgi
        - alpha_settings.py
      + tasks/
        - custom_task.py

Command examples
================


.. code-block:: bash

  $ up deploy alpha,beta
  $ up rollback alpha
  $ up deploy alpha --only=static,code
  $ up run django dumpdb alpha

Configuration example
=====================

config.yml
----------

.. code-block:: yaml

  project: 
    - name: website
    - domain: website.com
    - user: www-data

  up:
    - auto-install-packages: true

  roles:
    - virtualenv:
      - path: /var/www/vhosts/%(stage)s.%(domain)s/venv
      - requirements: /var/www/vhosts/%(stage)s.%(domain)s/requirements.pip
      - packages: ['virtualenv']
    - django:
      - document-root: /var/www/vhosts/%(stage)s.%(domain)s
      - static-root: /var/www/vhosts/%(stage)s.%(domain)s/static
      - media-root: /var/www/vhosts/%(stage)s.%(domain)s/media
      - repository: git@git.%(domain)s:user/%(project).git@%(stage)s
    - uswgi:
      - user:%(user)s 
      - group: %(group)s
      - packages: ['uwsgi', 'uwsgi-python', 'uwsgi-http']
      - templates:
        - conf: %(stage)s.uwsgi /etc/uwsgi/apps-enabled/%(stage)s.(domain)s
    - nginx:
      - conf: /etc/nginx/sites-enabled/%(stage)s.(domain)s
      - user:%(user)s 
      - group: %(group)s
      - packages: ['nginx-full']
    - mysql:
      - packages: ['mysql-server', 'mysql-client']
    - webserver:
      - roles: ['nginx']
    - application-server:
      - roles: ['virtualenv', 'django', 'uwsgi']
  
  servers:
    - default:
      - ssh-key: ~/.ssh/id_rsa.pub
    - node-1:
      - host: node-1.%(stage).%(domain)s
    - node-2:
      - host: node-2.%(stage).%(domain)s
  
 stages:
    - default:
      - servers: ['node-1']
      - roles: ['virtualenv', 'mysql', 'django', 'uwsgi' 'nginx']
      - nginx-conf: /etc/nginx/sites-enabled/%(self).%(domain)s
      - nginx-context:
        - servername: %(self).%(domain)s
        - listen: 127.0.0.1:443 ssl
      - on-deploy:
        - log:
          - info: 'Deployed application on %(stage)s'

    - alpha:
      - mysql-databases:
        - name: %(stage)s_myapp
          user: myuser
          password: mypassword
  
    - beta@alpha:
      - mysql-databases:
        - name: %(stage)s_myapp
          user: myuser
          password: mypassword
  
    - prod:
      - mysql-databases:
        - name: %(stage)s_myapp
          user: myuser
          password: mypassword
      - servers: ['%(domain)s']
      - up-auto-install-packages: false
      - on-deploy:
        - mail:
          - to: ['notice@test.com']
            from: 'alert@deploy.com'
            subject: 'Hello'
            body: 'Site has been deployed on %(stage)s!'
  
    - api 
      - servers: ['api.%(domain)s']
      - roles: ['virtualenv', 'django', 'uwsgi' 'nginx']
  ```
