import File1 as test

cases = [["1 + 1", "2"], ["1 + 2", "3"], ["1 - 1", "0"]]

for case in cases:
    assert str(test.run(case[0])) == case[1]

print("OK")