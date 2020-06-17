# types: float8 float32 double64
def get_signal(dec_num):
    if dec_num < 0:
        return 1
    else:
        return 0


def frac_to_bin(frac_num, numeric_type):
    if numeric_type == "float8":
        maxsize = 4
    elif numeric_type == "float32":
        maxsize = 23
    elif numeric_type == "double64":
        maxsize = 52
    binfrac = ""
    n = frac_num
    while len(binfrac) <= maxsize:
        n = n*2
        str_num = str(n).split(".")
        dec_num = int(str_num[0])
        binfrac += str(dec_num)
        n = float("0."+str_num[1])
      
        if n == 0:
            break
    return binfrac 


def convert_int_to_bin(dec_num, numeric_type):
    str_num = str(dec_num)
    frac_num = "0"
    if "." in str_num:
        str_num = str_num.split(".")
        dec_num = float(str_num[0])
        frac_num = float("0."+str_num[1])
        frac_num = frac_to_bin(frac_num, numeric_type)
    num_str = str(bin(int(dec_num)))

    if dec_num >= 0:
        binary_num = num_str.replace("0b", "")
    else:
        binary_num = num_str.replace("-0b", "")
    return binary_num, frac_num


def get_exp(binary_num):
    return binary_num.count('0') + binary_num.count('1') - 1


def create_exp(binary_num, numeric_type):
    scy_exp = get_exp(binary_num)
    if numeric_type == "float8":
        exp = 7 + scy_exp
        return bin(exp).replace("0b", "")
    elif numeric_type == "float32":
        exp = 127 + scy_exp
        return bin(exp).replace("0b", "")
    elif numeric_type == "double64":
        exp = 1023 + scy_exp
        return bin(exp).replace("0b", "")


def create_mantissa(binary_num, numeric_type):
    float_man = str
    if numeric_type == "float8":
        binary_num = str(binary_num) + str("0" * 5)
        float_man = binary_num[1:4]
        return float_man
    elif numeric_type == "float32":
        binary_num = str(binary_num) + str("0" * 24)
        float_man = binary_num[1:24]
        return float_man
    elif numeric_type == "double64":
        binary_num = str(binary_num) + str("0" * 53)
        float_man = binary_num[1:53]
        return float_man


def convert_to_hexa(binary_signal, binary_exp, bynayr_mantissa):
    final = str(binary_signal) + str(binary_exp) + str(bynayr_mantissa)
    hexa_num = '0x%0*X' % ((len(final) + 3) // 4, int(final, 2))
    return hexa_num


def print_number(binary_signal, binary_exp, bynayr_mantissa, hexa_num):
    return ("signal: " + str(binary_signal) + " | expoent: " + str(binary_exp) + " | mantissa: " + str(bynayr_mantissa) + " | hexadecimal: " + str(hexa_num) +
          "\n")

def main():
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
            num_type = "float8"
        
        if resp == 2:
            print("you want to calculate IEE 745 single precision (32 bits) number")
            num_type = "float32"

        if resp == 3:
            print("you want to calculate a IEE 745 double precision (64bits) number")
            print("you want to calculate IEE 745 single precision (32 bits) number")
            num_type = "double64"

        if resp == 4:
            print("you want to calculate all numbers")
        if resp == 0:
            print("bye !" + "\n")

        
        num = float(input("enter a  decimal number: "))
        bin_num, bin_frac = convert_int_to_bin(num, num_type)
        signal = get_signal(num)
        exp = create_exp(bin_num, num_type)
        mantissa = create_mantissa(bin_num+bin_frac, num_type)
        hexa_n = convert_to_hexa(signal, exp, mantissa)
        print(print_number(signal, exp, mantissa, hexa_n))

def conv(num,tipo ):
    num_type = tipo   
    num = float(num)
    bin_num, bin_frac = convert_int_to_bin(num, num_type)
    signal = get_signal(num)
    exp = create_exp(bin_num, num_type)
    mantissa = create_mantissa(bin_num+bin_frac, num_type)
    hexa_n = convert_to_hexa(signal, exp, mantissa)
    return  print_number(signal, exp, mantissa, hexa_n)

