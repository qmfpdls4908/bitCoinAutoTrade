import pyupbit
access = "nDpVR4lSPgcQjdD2fqXb8KPXW3hbLAVI9xzHM9Lh"          # 본인 값으로 변경
secret = "DRM7DhKXFXZ4SmxxkkGv0yhxtkPgDxvSzZifgm6i"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)


print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회