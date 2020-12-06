# 'BBFFBBFRLL'
def get_col(boarding_pass: str):
    return int(boarding_pass[7:].replace('L', '0').replace('R', '1'), 2)


def get_row(boarding_pass: str):
    return int(boarding_pass[:7].replace('B', '1').replace('F', '0'), 2)


def checksum(boarding_pass:str):
    return get_row(boarding_pass) * 8 + get_col(boarding_pass)


lines = open("../inputs/day5.txt").read().splitlines()

print(max(checksum(line) for line in lines))

checksums = sorted([checksum(line) for line in lines])
print([checksum for index, checksum in enumerate(checksums[:-1]) if checksums[index+1] == checksum + 2])
