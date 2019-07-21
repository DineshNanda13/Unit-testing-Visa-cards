# ======================================================================================================================
# Enter team members here:
# Name:
# ID:
# Name:
# ID:
# ======================================================================================================================

import pytransact


def test_is_visa():
    input_output = [
        ("4234567891234",True),
        ("423456789123a",False),
        ("4234567891*!/",False),
        ("4234567891234567",True),
        ("423456789123456A",False),
        ("1234567891234",False),
        ("4234-567 891234",True),
        ("45678",False)
    ]

    for input, expected_output in input_output:
        output = pytransact.is_visa(input)
        assert output == expected_output, "{} -> {} (expected: {})".format(input, output, expected_output)

    print("text_is_visa: OK")
    ...


def test_is_valid_expiration():
    input_output = [
        ("02/23", True),
        ("1/23",False),
        ("01/9",False),
        ("aa/bb",False),
        (" 2/23",False),
        ("0223",False),
        ("02 23",False),
        ("02-23",False),
        ("13/23",False),
        ("12/100",False),
        ("03/12",True),
        ("10/01",True),
        ("!&/6%",False),
        ("31/12", False),
        ("", False)
    ]

    for input, expected_output in input_output:
        output = pytransact.is_valid_expiration(input)
        assert output == expected_output, "{} -> {} (expected: {})".format(input, output, expected_output)

    print("text_is_valid_expiration: OK")
    ...


def test_random_visa():
    outputs = []
    for _ in range(10000):
        outputs.append(pytransact.random_visa())

    test_len_13 = False
    test_len_16 = False

    for card in outputs:
        assert pytransact.is_visa(card), "error {}".format(card)

        if len(card)==13:
            test_len_13 = True
        elif len(card) == 16:
            test_len_16 = True

    assert test_len_13 == True and test_len_16 == True,"Error: Not found 13 or 16 digit No.s"


    print("test_random_visa: OK")

    ...


if __name__ == "__main__":
    test_is_visa()
    test_is_valid_expiration()
    test_random_visa()