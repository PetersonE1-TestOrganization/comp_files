import File2 as test

cases = [["9 8 11", "2572"], ["1 3 9", "757"], ["5 11 13", "3653"]]

for case in cases:
    assert str(test.run(case[0])) == case[1]

print("OK")