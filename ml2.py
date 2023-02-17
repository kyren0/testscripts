
def madlibfiller(*args):
    with open('madlib_blank.txt', 'r') as blank:
        madlib= blank.read()
    
    madlibfilled= madlib.format(*args)
    with open('madlib_filled.txt', 'w') as filled:
        filled.write(madlibfilled)

madlibfiller(str(input("noun?")),str(input("noun?")),str(input("noun?")),str(input("noun?")),str(input("verb (past tense)?")),str(input("verb (-ing)?")),str(input("noun?")),str(input("noun?")))




