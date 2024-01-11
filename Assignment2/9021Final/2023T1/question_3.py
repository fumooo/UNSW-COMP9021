# You can assume that the function is called with a strictly positive
# integer as first argument and either True or False as second argument,
# if any.


def rhombus(size, shift_right=False):
    # '''
    # >>> rhombus(1)
    # A
    # >>> rhombus(1, True)
    # A
    # >>> rhombus(2)
    #  BA
    # CD
    # >>> rhombus(2, True)
    # AB
    #  DC
    # >>> rhombus(3)
    #   CBA
    #  DEF
    # IHG
    # >>> rhombus(3, True)
    # ABC
    #  FED
    #   GHI
    # >>> rhombus(4)
    #    DCBA
    #   EFGH
    #  LKJI
    # MNOP
    # >>> rhombus(4, True)
    # ABCD
    #  HGFE
    #   IJKL
    #    PONM
    # >>> rhombus(7)
    #       GFEDCBA
    #      HIJKLMN
    #     UTSRQPO
    #    VWXYZAB
    #   IHGFEDC
    #  JKLMNOP
    # WVUTSRQ
    # >>> rhombus(7, True)
    # ABCDEFG
    #  NMLKJIH
    #   OPQRSTU
    #    BAZYXWV
    #     CDEFGHI
    #      PONMLKJ
    #       QRSTUVW
    # '''
    # pass
    # REPLACE PASS ABOVE WITH YOUR CODE
    print(chr(65),chr(65+25))
    print(size,shift_right)
    str1 = ''
    tmp = 65
    for i in range(size):
        str1 = str1 + ' '*i
        str2 = ''
        for m in range(size):
            str2 = str2 + chr(tmp)
            tmp = tmp + 1
            if(tmp == 91):
                tmp = 65
        if (shift_right == True and i % 2 != 0):
            str2 = str2[::-1]
        if (shift_right == False and i % 2 == 0):
            str2 = str2[::-1]
        str1 =str1 + str2 + '\n'
    print(str1)
if __name__ == '__main__':

    rhombus(7)