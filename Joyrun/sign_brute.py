import hashlib

class BruteForce():
    def cut_string(self, sign):

        new_sign = ''

        if '?' in sign:
            sign_list = sign.split('?')
            new_sign = new_sign + sign_list[0]
            sign = sign_list[-1]

        if '&' in sign:
            sign_list = sign.split('&')
            sign_list = sorted(sign_list)
            for index in sign_list:
                new_sign = new_sign + index
        #         if '=' in index:
        #             index = index.split('=')
        #             new_sign = new_sign + index[0] + index[-1]
        # elif '=' in sign:
        #     sign=sign.split('=')
        #     new_sign = new_sign + sign[0] + sign[-1]

        return new_sign

    def check(self, sign):

        sign = self.cut_string(sign)

        _sign = "0AA65D69C29E0FF7D4F5E7840565D951"
        # "A20E12CBEF371E51785C09988144F751"
        # "43136B804F02E9662C2C81629DDEB9A3"
        # "00CF00A55EB5AD6550577F8CCD048F02"
        # "8CC06A1729F338FCC4ADAF60C2BC9F67"
        # "0AA65D69C29E0FF7D4F5E7840565D951"

        _signed = hashlib.md5(sign.encode('utf-8')).hexdigest().upper()
        sign = "advert-test.api.thejoyrun.com" + "1548233533"
        _signed = hashlib.md5(sign.encode('utf-8')).hexdigest().upper()
        print(_signed)
        if _signed == _sign:
            print("It's Rriht!!!")

def to_lower():
    from ..Python.reptile.hard.try_ import FileOperation

    fn=FileOperation()

    raw_list=fn.read_file("./robot/Config.py")

    for index in raw_list:
        index=index.lower()
        fn.write_file("./robot/")


if __name__ == "__main__":
    arg = "http://advert-test.api.thejoyrun.com/advert-list?signature=3D46E029E48D817BB4132D0B21E7ECDF&timestamp=1548233533"

    sign1 = arg.split('/')[-1]
    sign2 = arg.split('?')[-1]

    brute=BruteForce().check
    brute(sign1)
    brute(sign2)

