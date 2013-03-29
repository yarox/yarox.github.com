import datetime
import os

from fabric.api import local, lcd, settings, prompt
from fabric.utils import puts, warn

from pelicanconf import DEPLOYMENT


# Get directories
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
SETTINGS_FILE = os.path.join(BASE_PATH, "pelicanconf.py")
OUTPUT_PATH = os.path.join(BASE_PATH, "output")
INPUT_PATH = os.path.join(BASE_PATH, "content")


# Commands
def post(markup="rst"):
    """Creates an empty blog post with some metadata filled"""

    with settings(abort_on_prompts=False):
        title = prompt('Enter title:', validate=validate_title)

    slug = title.lower().replace(" ", "-")
    file_name = os.path.join(INPUT_PATH, "{0}.{1}".format(slug, markup))

    if os.path.exists(file_name):
        warn("post already exists")
    else:
        with open(file_name, "w") as out_file:
            padding = "#" * len(title)
            out_file.write("{1}\n{0}\n{1}\n\n".format(title, padding))

            out_file.write(":status: draft\n")
            out_file.write(":date: {0}\n".format(datetime.datetime.now().strftime("%Y-%m-%d")))
            out_file.write(":tags: some, tags, here\n")
            out_file.write(":slug: {0}\n\n".format(slug))
            out_file.write("Start here.\n")

        puts("Your post is at: {0}".format(file_name))


def validate_title(title):
    if title:
        return title
    else:
        raise RuntimeError('Title must not be empty')

def generate():
    """Generates the pelican static site"""
    cmd = "pelican {0} -o {1} -s {2}".format(INPUT_PATH, OUTPUT_PATH, SETTINGS_FILE)
    local(cmd)


def clean():
    """Destroys the pelican static site"""
    cmd = "find {0} -mindepth 1 ! -wholename *.git* -delete".format(OUTPUT_PATH)

    with settings(warn_only=True):
        result = local(cmd)

    if result.failed:
        puts("site already deleted")


def regenerate():
    """Cleans and generates the pelican static site"""
    clean()
    generate()


def start_server():
    """Serves the site in the development webserver"""
    local("make devserver")


def stop_server():
    """Stops the development webserver"""
    local("./develop_server.sh stop")


def deploy(name='default'):
    "Generates the site and executes the deployment commands"
    try:
        commands = DEPLOYMENT[name]
    except KeyError:
        print('unknown command name "{0}".'.format(name))
        print('available commands:')

        for name, command in DEPLOYMENT.items():
            print('\t{0}: {1}'.format(name, command))
    else:
        #generate()

        with lcd(OUTPUT_PATH):
            for command in commands:
                local(command)
