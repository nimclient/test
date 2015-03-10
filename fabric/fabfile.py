# coding: utf-8
import fabric.api as fab


def dev_reload():
    with fab.cd("/home/nimclient/test")
        fab.sudo("git pull", user="nimclient")
        fab.sudo("pip install -U -r requirements/requirements.txt")
    fab.sudo("echo done")

