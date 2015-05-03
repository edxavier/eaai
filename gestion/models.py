from mongoengine import *
from mongoengine.context_managers import switch_db

# Create your models here.

try:
#    connect('gestion',alias="gestion",host='localhost')
    connect('gestion',alias="gestion",host='192.168.137.200')
except Exception, e:
    print e.message


class Boot_history(Document):
    node = StringField()
    platform = StringField()
    event = StringField()
    node_date = DateTimeField()
    server_date = DateTimeField()

    meta = {"db_alias": "gestion"}
    

class Hosts(Document):
    ip = StringField(unique=True)
    connected = BooleanField(default=False)
    hostname = StringField(default="----")
    contact = StringField(default="----")
    description = StringField(default="----")
    location = StringField(default="----")
    services = IntField(default=-1)
    uptime = StringField(default=None)
    users = IntField(default=-1)
    processes = IntField(default=-1)

    disks_status = StringField(default="ok")
    mem_status = StringField(default="ok")
    procs_status = StringField(default="ok")
    load_status = StringField(default="ok")

    last_update = DateTimeField()

    meta = {"db_alias": "gestion"}

class Memory(Document):
    swap = IntField()
    free_swap = IntField()
    ram = IntField()
    free_ram = IntField()
    used_ram = IntField()
    node_ip = StringField()
    last_update = DateTimeField()
    meta = {"db_alias": "gestion"}

class Disk(Document):
    disk_path = StringField()
    device = StringField()
    minimun = FloatField()
    total = FloatField()
    free = FloatField()
    used = FloatField()
    percent = IntField()
    error_flag = IntField()
    error_msg = StringField()
    node_ip = StringField()
    last_update = DateTimeField()
    meta = {"db_alias": "gestion"}

class Load(Document):
    load_1 = FloatField()
    load_5 = FloatField()
    load_15 = FloatField()
    load1_err_flag = IntField()
    load5_err_flag = IntField()
    load15_err_flag = IntField()
    load1_err_msg = StringField()
    load5_err_msg = StringField()
    load15_err_msg = StringField()
    node_ip = StringField()
    last_update = DateTimeField()
    meta = {"db_alias": "gestion"}

class Process(Document):
    name = StringField()
    count = IntField()
    minimun = IntField()
    maximun = IntField()
    err_flag = IntField()
    err_msg = StringField()
    node_ip = StringField()
    last_update = DateTimeField()
    meta = {"db_alias": "gestion"}

class Storage(Document):
    desc = StringField()
    size = FloatField()
    used = FloatField()
    percent_used = FloatField()
    node_ip = StringField()
    last_update = DateTimeField()
    meta = {"db_alias": "gestion"}


class Device(Document):
    desc = StringField()
    status = StringField()
    node_ip = StringField()
    last_update = DateTimeField()
    meta = {"db_alias": "gestion"}


class Software(Document):
    name = StringField()
    path = StringField()
    parameters = StringField()
    type = StringField()
    status = StringField()

    node_ip = StringField()
    last_update = DateTimeField()
    meta = {"db_alias": "gestion"}

class Interface(Document):
    desc = StringField()
    admin_status = StringField()
    oper_status = StringField()
    speed = IntField()
    inErrors = IntField()
    inDiscards = IntField()
    outErrors = IntField()
    outDiscards = IntField()

    node_ip = StringField()
    last_update = DateTimeField()
    meta = {"db_alias": "gestion"}


class Memory_hist(Document):
    ram = IntField()
    used_ram = IntField()
    node_ip = StringField()
    date = DateTimeField()
    meta = {"db_alias": "gestion"}

class Load_hist(Document):
    load1 = FloatField()
    load5 = FloatField()
    load15 = FloatField()
    node_ip = StringField()
    date = DateTimeField()
    meta = {"db_alias": "gestion"}

class Disk_hist(Document):
    disk_path = StringField()
    device = StringField()
    total = FloatField()
    used = FloatField()
    node_ip = StringField()
    date = DateTimeField()
    meta = {"db_alias": "gestion"}