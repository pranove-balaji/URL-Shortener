import hashlib
import base64

def generate_short_url(long_url):
    hashobj = hashlib.sha256(long_url.encode())
    short_hash = base64.urlsafe_b64encode(hashobj.digest())[:6].decode()
    print(short_hash)
generate_short_url("https://www.youtube.com/watch?v=X-n6t2tgwEk&list=PLLa_h7BriLH2ihMfDMpSHl2PbBjSzvDtw&index=4")