# types: float8 float32 double64



def get_signal(dec_num):
    if dec_num < 0:
        return 1
    else:
        return 0


def convert_int_to_bin(dec_num):
    str_num = str(dec_num)
    frac_num = "0"
    if "." in str_num:
        str_num = str_num.split(".")
        dec_num = float(str_num[0])
        frac_num = float("0."+str_num[1])
        print(str(dec_num), str(frac_num))
        frac_num = frac_to_bin(frac_num)    
    num_str = str(bin(int(dec_num)))
    if dec_num > 0:
        bin_num = num_str.replace("0b", "")
    else:
        bin_num = num_str.replace("-0b", "")
    return bin_num, frac_num


def get_exp(bin_num):
    return bin_num.count('0') + bin_num.count('1') - 1

def create_exp(bin_num, num_type):
    scy_exp = get_exp(bin_num)
    if num_type == "float8":
        exp = 7 + scy_exp
        return bin(exp).replace("0b", "")
    elif num_type == "float32":
        exp = 127 + scy_exp
        return bin(exp).replace("0b", "")
    elif num_type == "float64":
        exp = 1023 + scy_exp
        return bin(exp).replace("0b", "")

def create_mantissa(bin_num, type):
    float_man = str
    if type == "float8":
        float_man = bin_num[1:4]
        return float_man
    elif type == "float32":
        bin_num = str(bin_num) + str("0" * 24)
        float_man = bin_num[1:24]
        return float_man
    elif type == "float64":
        bin_num = str(bin_num) + str("0" * 53)
        float_man = bin_num[1:53]
        return float_man
    

def printNumero(signal,exp,mantissa):
    print("signal: " + str(signal) + " | expoent: " + str(exp) + " | mantissa: " + str(mantissa) + "\n")



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
       
    if resp == 2:
        print("you want to calculate IEE 745 single precision (32 bits) number")
        type = "float32" 

    if resp == 3:
        print("you want to calculate a IEE 745 double precision (64bits) number")
        print("you want to calculate IEE 745 single precision (32 bits) number")
        type = "float64"

    if resp == 4:
        print("you want to calculate all numbers")
    if resp == 0:
        print("bye !" + "\n" )



    num = float(input("enter a  decimal number number: "))
    bin_num, bin_frac = convert_int_to_bin(num)
    signal = get_signal(num)
    exp = create_exp(bin_num, type)
    mantissa = create_mantissa(bin_num, type)
    printNumero(signal,exp,mantissa)


#num = float(input("enter a number: "))
#bin_num = convert_int_to_bin(num)
#print(str(get_signal(num)) + " | " + str((create_exp(bin_num, "float8")) + " | " + str(create_mantissa(bin_num, "float8"))))
