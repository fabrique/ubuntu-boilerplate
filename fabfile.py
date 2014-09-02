from fabric.api import *
from fabric.contrib.console import confirm



@task
def install(flavor=None):
    server_name = prompt('Server name: ', default='NEWSERVER')
    if flavor == 'web':
        postgres = False
        mysql = False
        nginx = True
        memcached = True
        redis = True
        rabbitmq = False
        supervisor = True
    else:
        postgres = confirm("Install PostgreSQL?", default=False)
        mysql = confirm("Install MySQL?", default=False)
        nginx = confirm("Install NGINX?", default=False)
        memcached = confirm("Install Memcached?", default=False)
        redis = confirm("Install Redis?", default=False)
        rabbitmq = confirm("Install RabbitMQ?", default=False)
        supervisor = confirm("Install Supervisor?", default=False)

    run('apt-get update -q')
    run('apt-get upgrade -qy')
    run('apt-get install git-core vim -qy')
    run('update-alternatives --set editor /usr/bin/vim.basic')

    put('./sudoers', '/etc/sudoers', mode=0440)

    run('locale-gen en_US.UTF-8')
    run('update-locale LANG=en_US.UTF-8')
    run('ln -sfn /usr/share/zoneinfo/Europe/Amsterdam /etc/localtime')

    put('./bash.bashrc', '/etc/bash.bashrc', mode=0644)
    put('./root.bashrc', '/root/.bashrc', mode=0644)
    put('./skel.bashrc', '/etc/skel/.bashrc', mode=0644)
    run('touch /etc/skel/.hushlogin')

    put('./iptables', '/etc/network/iptables', mode=0644)
    put('./iptables-start', '/etc/network/if-pre-up.d/iptables', mode=0755)
    run('iptables-restore < /etc/network/iptables')

    put('./sshd_config', '/etc/ssh/sshd_config', mode=0644)

    run('hostname %s' % server_name)
    run('echo "%s %s" >> /etc/hosts' % (env.host_string.split('@')[-1], server_name))

    # Create fabrique user
    run('useradd fabrique -Um -s /bin/bash' )
    # Create ssh identity
    sudo('ssh-keygen -t rsa -f /home/fabrique/.ssh/id_rsa -C "fabrique@%s" -q -N ""' % server_name, user='fabrique', shell=False)
    # Enable Fabrique devs to ssh
    run('wget "http://dev.fabriquehq.nl/install/authorized_keys" -O "/home/fabrique/.ssh/authorized_keys"')
    run('chmod 644 /home/fabrique/.ssh/authorized_keys')
    run('chown fabrique: /home/fabrique/.ssh/authorized_keys')

    # Dotfiles
    put('./dotfiles/', '/home/fabrique/')
    run('chown fabrique:fabrique /home/fabrique/.*rc')
    run('chown -R fabrique:fabrique /home/fabrique/.vim')

    # Celery (configs only)
    put('./celerybeat.default', '/etc/default/celerybeat', mode=0644)
    put('./celeryd.default', '/etc/default/celeryd', mode=0644)
    put('./celerybeat.initd', '/etc/init.d/celerybeat', mode=0755)
    put('./celeryd.initd', '/etc/init.d/celeryd', mode=0755)
    run('mkdir -p /var/run/celery')
    run('chown www-data: /var/run/celery')

    # Install essentials
    run('apt-get install build-essential gcc g++ make bash-completion htop -qy')

    # Python stuff
    run('apt-get install python-software-properties python python-dev python-setuptools ipython python-imaging libjpeg-dev -qy')
    run('easy_install pip')
    run('pip install ipdb virtualenv')

    # Version control
    run('apt-get install git-core mercurial subversion -qy')

    # uWSGI
    run('pip install uwsgi')
    run('mkdir -p /etc/uwsgi/vassals')
    put('./uwsgi.conf', '/etc/init/uwsgi.conf', mode=0644)
    run('mkdir -p /var/log/uwsgi')

    # Ruby
    run('apt-get install ruby rubygems ruby-compass -qy')

    if postgres:
        run('apt-get install libpq-dev postgresql-server-dev-9.3 postgresql-9.3 postgresql-client-9.3 python-psycopg2 -qy')
        #sudo('createuser -s web', user='postgres', shell=False)

    if mysql:
        run('apt-get install mysql-server mysql-client python-mysqldb libmysqlclient-dev')

    if nginx:
        run('apt-get install nginx -qy')
        put('./nginx.conf', '/etc/nginx/nginx.conf', mode=0644)
        put('./proxy_params', '/etc/nginx/proxy_params', mode=0644)

    if memcached:
        run('apt-get install memcached -qy')

    if redis:
        run('apt-get install redis-server -qy')

    if rabbitmq:
        run('apt-get install rabbitmq-server -qy')

    if supervisor:
        run('apt-get install supervisor -qy')

    print "Done with basic setup."

