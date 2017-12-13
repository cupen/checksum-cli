# coding:utf-8
import io
from checksum import get_avaliable_hash, generate_hashsum

if __name__ == '__main__':
    for name in get_avaliable_hash():
        hash_sum = generate_hashsum(name, io.BytesIO(b"iambytes"))
        print("{name:>8} is ok".format(**locals()))
    pass
