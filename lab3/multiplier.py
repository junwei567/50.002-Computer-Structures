# used to generate multiplier code for jsim
# may have to adjust to fit the inputs for your full adder used
def multiplier_gen(file_handler):
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'aa', 'ab' , 'ac', 'ad', 'ae', 'af']
    file_handler.write('.subckt mult32 A[31:0] B[31:0] out[31:0] \n')
    file_handler.write('* every and gatesss \n')
    
    for i in range(0, 32):
        line = "Xand{0} A[{1}:0] B[{0}]#{2} and_{3}[{1}:0] and2".format(i, 31-i, 32-i, alphabets[i])
        file_handler.write(line + "\n")

    file_handler.write('* first bit output \n')
    file_handler.write('.connect out0 and_a0 \n')
    file_handler.write('\n')
    file_handler.write('Xfaa1 and_a1 and_b0 0 out1 co_b0 fa \n')
    file_handler.write('Xfab1 and_a[31:2] and_b[30:1] co_b[29:0] sum_b[29:0] co_b[30:1] fa \n')

    for i in range(2, 31):
        line = "Xfaa{0} sum_{1}0 and_{2}0 0 out{0} co_{2}0 fa".format(i, alphabets[i-1], alphabets[i])
        line2 = "Xfab{0} sum_{1}[{2}:1] and_{3}[{2}:1] co_{3}[{4}:0] sum_{3}[{4}:0] co_{3}[{2}:1] fa".format(i, alphabets[i-1], 31-i, alphabets[i], 30-i)
        file_handler.write(line + "\n")
        file_handler.write(line2 + "\n")

    file_handler.write('Xfaa31 sum_ae0 and_af0 0 out31 co_af fa \n')
    file_handler.write('.ends')
    

if __name__=="__main__":
    file = open("multiplier.jsim", "w")
    multiplier_gen(file)
    file.close()