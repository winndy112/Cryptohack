from Crypto.Util.number import  bytes_to_long as btl
from Crypto.Util.number import long_to_bytes as ltb
 
n = 110581795715958566206600392161360212579669637391437097703685154237017351570464767725324182051199901920318211290404777259728923614917211291562555864753005179326101890427669819834642007924406862482343614488768256951616086287044725034412802176312273081322195866046098595306261781788276570920467840172004530873767                                                             
e = 1 # m^1 mod n = m => ct=m
ct = 44981230718212183604274785925793145442655465025264554046028251311164494127485
print(ltb(ct))
