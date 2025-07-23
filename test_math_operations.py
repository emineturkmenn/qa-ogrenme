def topla(a,b):
    return a+b

def test_topla():
    assert topla(2,3) == 5
    assert topla(-1,1) == 0
    assert topla(0,0) == 0
    # assert topla(2, 3) == 6, "Toplama hatalı sonuç verdi"

test_topla()
print("Tüm testler geçti ✅")
