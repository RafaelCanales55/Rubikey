import time
import sys
from random import randint

msg1=str("UN4 LL4V3 QU3 48R3 CU4LQU13R C4ND4D0 35 UN4 LL4V3 M4357R4, P3R0 CU4ND0 353 C4ND4D0 L0 48R3 CU4LQU13R LL4V3, 53 D353CH4.")

A=True
B=False
C=False

A2=True
B2=True
C2=False


def neg(p:bool)-> bool:

    if p:
        return False
    else:
        return True

def y(p:bool, q:bool)-> bool:

    if p:
        return q
    else:
        return False

def o(p:bool, q:bool)-> bool:
    if p:
        return True
    else:
        return q

def EDO():
    _C=neg(C)
    _B=neg(B)
    _B_C=y(_B,_C)
    D=y(A,_B_C)
    if D==True:
        msg=str("Se desbloquea.")
        return D, msg
    else:
        msg="No se pasa a la Cerradura 1, la Cerradura 2 está bloqueada."
        return D, msg

def EDO1(D):
    if D==True:
        AB=y(A2,B2)
        _C=neg(C2)
        _CAB=y(neg(_C),AB)
        DAB_C=y(neg(_C),y(D,AB))
        ABo_CAB=o(AB,_CAB)
        ABo_CABoDAB_C=o(ABo_CAB,DAB_C)
        if ABo_CABoDAB_C==True:
            return ABo_CABoDAB_C, msg1
        else:
            msg="Error: Cerradura inválida."
            return ABo_CABoDAB_C,msg
    else:
        msg="Error: Cerradura inválida."
        return D,msg
    
    
    
def main() -> int:
    D,mgs3 = EDO()
    print(mgs3)
    e,pi=EDO1(D)
    print(pi)
    return 0

if __name__=="__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit(0)