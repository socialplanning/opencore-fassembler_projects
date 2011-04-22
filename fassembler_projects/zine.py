from fassembler import tasks
from fassembler.project import Project, Setting
from pkg_resources import resource_filename

class ZineProject(Project):
    """
    Install Zine
    """

    name = 'zine'
    title = 'Install Zine'
    settings = [
        Setting('zine_instances_directory',
                default='{{env.var}}/{{project.name}}/instances',
                help="Directory that will house all projects' Zine instances (config files and sqlite databases)",
                ),
        Setting('port',
                default='{{env.base_port+4}}',
                help='Port to install Zine on'),
        Setting('host',
                default='localhost',
                help='Host to serve on'),
        Setting('spec',
                default='requirements/zine-req.txt',
                help='Specification of packages to install'),
        Setting('shared_secret_filename',
                default='{{env.var}}/secret.txt',
                help='Path to the file containing the shared secret used to encrypt and decrypt the auth cookie'),
        Setting('admin_info_filename',
                default='{{env.var}}/admin.txt',
                help='Path to the file containing credentials of a site admin user that can be used to query projects for their security policies and memberships'),
        Setting('internal_root_url',
                default='http://localhost:{{env.base_port+1}}/openplans/',
                help='Base url path to the opencore site root; if possible this should hit Zope directly using a non-internet-wide connection, because site admin credentials are passed in the HTTP request'),
        Setting('use_pip',
                default='True',
                help="Use pip to install requirements, or easy_install"),
        ]

    actions = [
        tasks.VirtualEnv(),
        tasks.InstallSpec('Install Zine',
                          '{{config.spec}}'),
        tasks.InstallPasteConfig(path=resource_filename(
                'fassembler_projects', 'templates/zine/paste.ini_tmpl')),
        tasks.InstallPasteStartup(),
        tasks.InstallSupervisorConfig(),
        ]


