# mypackage/arrangement/arrange.py


def sort_list(data, mode=1):
    """
    Sắp xếp list theo mode
    mode = 0 : giảm dần (lớn -> bé)
    mode = 1 : tăng dần (bé -> lớn)
    """

    if not isinstance(data, list):
        raise TypeError("Tham số data phải là list")

    if mode == 0:
        return sorted(data, reverse=True)
    elif mode == 1:
        return sorted(data)
    else:
        raise ValueError("mode chỉ nhận 0 (giảm dần) hoặc 1 (tăng dần)")
