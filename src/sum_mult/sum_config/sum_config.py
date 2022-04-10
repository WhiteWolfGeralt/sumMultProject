def sum_config(x: int) -> int:
    with open("../config") as config:
        return int(config.readline()) + x
