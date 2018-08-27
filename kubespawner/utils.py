"""
Misc. general utility functions, not tied to Kubespawner directly
"""
import random
import hashlib

from traitlets import TraitType
import pymysql

def generate_hashed_slug(slug, limit=63, hash_length=6):
    """
    Generate a unique name that's within a certain length limit

    Most k8s objects have a 63 char name limit. We wanna be able to compress
    larger names down to that if required, while still maintaining some
    amount of legibility about what the objects really are.

    If the length of the slug is shorter than the limit - hash_length, we just
    return slug directly. If not, we truncate the slug to (limit - hash_length)
    characters, hash the slug and append hash_length characters from the hash
    to the end of the truncated slug. This ensures that these names are always
    unique no matter what.
    """
    if len(slug) < (limit - hash_length):
        return slug

    slug_hash = hashlib.sha256(slug.encode('utf-8')).hexdigest()

    return '{prefix}-{hash}'.format(
        prefix=slug[:limit - hash_length - 1],
        hash=slug_hash[:hash_length],
    ).lower()

def get_user_data(username, mysql_info):
    try:
        host, port, user, passwd, db = mysql_info["url"].split('+')
        client = pymysql.connect(host, user, passwd, db, port = int(port))
        db = client.cursor()
    except:
        return {}
    sql = "SELECT jp_gpu_enable, jp_image, jp_gpu_number, jp_cpu_request, jp_cpu_limit, jp_mem_request, jp_mem_limit FROM user \
          WHERE username = '%s'" % (username)
    db.execute(sql)
    result = db.fetchall()
    data = {}
    for item in result:
        data = {'jp_gpu_enable':item[0],
                'jp_image':item[1],
                'jp_gpu_number':item[2],
                'jp_cpu_request':item[3],
                'jp_cpu_limit':item[4],
                'jp_mem_request':item[5],
                'jp_mem_limit':item[6]}
    client.close()
    return data


class Callable(TraitType):
    """A trait which is callable.
    Notes
    -----
    Classes are callable, as are instances
    with a __call__() method."""

    info_text = 'a callable'

    def validate(self, obj, value):
        if callable(value):
            return value
        else:
            self.error(obj, value)
