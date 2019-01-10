# -*-coding:utf-8-*-
__author__ = "Allen Woo"

mongo_host='127.0.0.1'
redis_host='127.0.0.1'
try:
    docker_flag = os.environ.get('DOCKER', "")
    if docker_flag == '1':
        mongo_host = 'mongodb'
        redis_host='redis'
        print('Run in docker!')
    else:
        redis_host='127.0.0.1'
        mongo_host = '127.0.0.1'
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
DB_CONFIG = {
    "mongodb": {
        "mongo_web": {
            "username": "root",
            "config": {
                "fsync": False,
                "replica_set": None
            },
            "dbname": "osr_web",
            "host": [
                "%s:27017"%mongo_host
            ],
            "password": ""
        },
        "mongo_user": {
            "username": "root",
            "config": {
                "fsync": False,
                "replica_set": None
            },
            "dbname": "osr_user",
            "host": [
                "%s:27017"%mongo_host
            ],
            "password": ""
        },
        "mongo_sys": {
            "username": "root",
            "config": {
                "fsync": False,
                "replica_set": None
            },
            "dbname": "osr_sys",
            "host": [
                "%s:27017"%mongo_host
            ],
            "password": ""
        }
    },
    "redis": {
        "host": [
            redis_host
        ],
        "password": "",
        "port": [
            "6379"
        ]
    }
}