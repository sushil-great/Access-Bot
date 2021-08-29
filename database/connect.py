from mongoengine import register_connection
import os

def db_init(config):

    register_connection(
        alias='core',
        name=config.mongodb['db_name'],
        username=config.mongodb['username'],
        password=config.mongodb['password'],
        host=config.mongodb['uri']
    )
