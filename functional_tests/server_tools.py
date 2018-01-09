from fabric.api import run
from fabric.context_managers import settings


def _get_manage_dot_py(host):
    return f'~/sites/{host}/virtualenv/bin/python ~/sites/{host}/manage.py'


def reset_database(host):
    manage_dot_py = _get_manage_dot_py(host)
    with settings(host_string=f'felipequintella@{host}'):
        run(f'{manage_dot_py} flush --noinput')


def create_session_on_server(host, email):
    manage_dot_py = _get_manage_dot_py(host)
    with settings(host_string=f'felipequintella@{host}'):
        session_key = run(f'{manage_dot_py} create_session {email}')
        print(session_key)
        print(session_key.strip())
        return session_key.strip()