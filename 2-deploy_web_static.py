#!/usr/bin/python3
"""
Fabric script to send an archive to a server
"""

from datetime import datetime
from fabric.api import *
import os

env.hosts = ["100.24.72.6", "100.27.2.148"]
env.user = "ubuntu"


def do_pack():
    """
        Returns the archive path if archive has generated correctly.
    """

    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archived_f_path = "versions/web_static_{}.tgz".format(date)
    t_gzip_archive = local("tar -cvzf {} web_static".format(archived_f_path))

    if t_gzip_archive.succeeded:
        return archived_f_path
    else:
        return None


def do_deploy(archive_path):
    """
        Distributes archive
    """
    if os.path.exists(archive_path):
        archived_file = archive_path[9:]
        newest_version = "/data/web_static/releases/" + archived_file[:-4]
        print("New version deployed!")
        return True

    return False
