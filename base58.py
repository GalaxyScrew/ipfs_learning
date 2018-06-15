import binascii

BASE58_ALPHABET = b"123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

#解码就是编码的逆过程，主要是n = n * div + mod 逆向求mod和正向求n 
def base58decode(base58_str):
    base58_text = bytes(base58_str, "ascii")
    n = 0
    leading_zeroes_count = 0
    for b in base58_text:
        n = n * 58 + BASE58_ALPHABET.find(b)
        if n == 0:
            leading_zeroes_count += 1
    res = bytearray()
    while n >= 256:
        div, mod = divmod(n, 256)
        res.insert(0, mod)
        n = div
    else:
        res.insert(0, n)
    return binascii.hexlify(bytearray(1) * leading_zeroes_count + res).decode('ascii')


def base58encode(hexstring):
    byteseq = bytes(binascii.unhexlify(bytes(hexstring, 'ascii'))) #将16进制转换为二进制
    n = 0
    leading_zeroes_count = 0
    for c in byteseq:
        n = n * 256 + c #对每一个字符按8个比特位进行扩展，得出一个大整数
        if n == 0:
            leading_zeroes_count += 1 #首部0的个数
    res = bytearray()
    while n >= 58:
        div, mod = divmod(n, 58) #对大整数不断进行mod58
        res.insert(0, BASE58_ALPHABET[mod]) #将余数对应的base58字符拼接
        n = div
    else:
        res.insert(0, BASE58_ALPHABET[n])
    return (BASE58_ALPHABET[0:1] * leading_zeroes_count + res).decode('ascii') #输出拼接后的base58字符串

tmp = base58decode("QmajJpKAWiY2h6xMmzz71d35YnEH9Le3Fz2dLu4BEqmyFQ")
re = base58encode(tmp)

print(tmp)
print(re)
