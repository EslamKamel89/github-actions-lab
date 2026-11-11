from app import calculate_total


def main():
    assert calculate_total(25, 4) == 100
    assert calculate_total(0, 10) == 0

    try:
        calculate_total(-1, 2)
    except ValueError:
        pass
    else:
        raise AssertionError("Negative price should fail")

    print("All validations passed")


if __name__ == "__main__":
    main()
