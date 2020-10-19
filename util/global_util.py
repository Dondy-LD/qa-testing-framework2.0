# -*- coding: utf-8 -*-


def init():
    global _global_dict
    _global_dict = {}


def set_value(key, value):
    """ define a global parameter"""
    _global_dict[key] = value


def get_value(key, defValue=None):
    """ get the global paramter, will return the default value if no value """
    try:
        return _global_dict[key]
    except KeyError:
        return defValue