from typing import List, Tuple


TestList = List[int] # type aloas for test list of one million numbers


def linear_contains(tl: TestList, key: int) -> Tuple[bool, int]:
    hop_count: int = 0
    for i in tl:
        hop_count += 1
        if i == key:
            return True, hop_count
    return False, hop_count


def binary_contains(tl: TestList, key: int) -> Tuple[bool, int]:
    sorted_tl = sorted(tl) # Binary search requires list be sorted
    low: int = 0
    high: int = len(sorted_tl) - 1
    hop_count = 0
    while low <= high:
        hop_count += 1
        mid: int = (low + high) // 2
        if sorted_tl[mid] < key:
            low = mid + 1
        elif sorted_tl[mid] > key:
            high = mid - 1
        else:
            return True, hop_count
    return False, hop_count

