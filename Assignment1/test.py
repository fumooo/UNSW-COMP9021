'''
One evening as you are out for a stroll, you walk by a doorway labeled no normals
allowed. Some people are talking inside. Curious, you listen, and you hear Sir Paul
who says: "all of us are Knaves." "Exactly one of us is a Knight," replies Sir Jenny.
As for Sir John, who is also inside, he just keeps quiet. Who is a Knight, and who
is a Knave?

思路分情况
三个人的话 就是： 一人撒谎，两人撒谎，三人撒谎 （撒谎是0 Knave，不撒谎是1 Knight）
Jenny John Paul
Paul 真值为: Jenny + John + Paul == 0
Jenny 真值为: Jenny + John + Paul == 1 只有两种条件意味着

lan1 = (Jenny + John + Paul == 0)
lan2 = (Jenny + John + Paul == 1)

((Paul == 1 and Jenny + John + Paul == 0) or (Paul == 0 and Jenny + John + Paul != 0) or
(Jenny == 1 and Jenny + John + Paul == 1) or (Jenny == 0 and Jenny + John + Paul != 1))
'''
for Jenny in range(2):
    for John in range(2):
        for Paul in range(2):
            if (
                    (((Paul == 1 and Jenny + John + Paul == 0) or (Paul == 0 and Jenny + John + Paul != 0)) and
                     ((Jenny == 1 and Jenny + John + Paul == 1) or (Jenny == 0 and Jenny + John + Paul != 1)))
            ):
                print(Jenny,John,Paul)