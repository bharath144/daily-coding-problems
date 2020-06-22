def power_set(input_set: list):
    # TODO: Make sure that the input set does not have duplicate numbers
    # assert len(set(input_set)) == len(input_set), "Input must not contain duplicates"

    print(f"Input set: {input_set}")

    _power_set = list()

    input_set_len = len(input_set)
    _power_set_len = int(pow(2, input_set_len))

    for i in range(0, _power_set_len):
        sub_set = list()
        for j in range(0, input_set_len):
            if i & (1 << j):
                sub_set.append(input_set[j])
        _power_set.append(sub_set)

    print(f"Power set: {_power_set}")

    return _power_set


if __name__ == "__main__":
    pass
