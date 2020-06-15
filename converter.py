# types: float8 float32 double64



def get_signal(dec_num):
    if dec_num < 0:
        return 1
    else:
        return 0


def convert_int_to_bin(dec_num):
    num_str = str(bin(int(dec_num)))
    if dec_num > 0:
        bin_num = num_str.replace("0b", "")
    else:
        bin_num = num_str.replace("-0b", "")
    return bin_num


def create_exp(bin_num, num_type):
    if num_type == "float8":
        scy_exp = bin_num.count('0') + bin_num.count('1') - 1
        exp = 7 + scy_exp
        return bin(exp).replace("0b", "")


def create_mantissa(bin_num, type):
    float8_man = str
    if type == "float8":
        float8_man = bin_num[1:4]
    return float8_man


resp = int
while resp != 0:
    resp = int(input("""what you want to do?: 
    1 - calculate a floating point (8bits);
    2 - calculate a IEE 745 single precision (32 bits) number; 
    3 - calculate a IEE 745 double precision (64bits) number;
    4 - all above;
    0 - exit.
    type your numeric answer here: """))
    if resp == 1:
        print("you want to calculate a floating point (8bits)")
        type = "float8"
        num = float(input("enter a  decimal number number: "))
        bin_num = convert_int_to_bin(num)
        signal = get_signal(num)
        exp = create_exp(bin_num, type)
        mantissa = create_mantissa(bin_num, type)
        print("signal: " + str(signal) + " | expoent: " + str(exp) + " | mantissa: " + str(mantissa) + "\n")
    if resp == 2:
        print("you want to calculate IEE 745 single precision (32 bits) number")
    if resp == 3:
        print("you want to calculate a IEE 745 double precision (64bits) number")
    if resp == 4:
        print("you want to calculate all numbers")
    if resp == 0:
        print("bye !" + "\n" + bye)


#num = float(input("enter a number: "))
#bin_num = convert_int_to_bin(num)
#print(str(get_signal(num)) + " | " + str((create_exp(bin_num, "float8")) + " | " + str(create_mantissa(bin_num, "float8"))))
