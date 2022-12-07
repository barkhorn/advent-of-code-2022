
# class Ringbuffer(object):
#     def __init__(self, rblength: int):
#         self.rblength = rblength
#         self.rbdata = [None for _ in range(rblength)]
#         self.rbindex = 0
#
#     def is_start(self):
#         return len(set(self.rbdata)) == self.rblength and None not in self.rbdata
#
#     def add(self, c: str):
#         self.rbdata[self.rbindex] = c
#         self.rbindex = (self.rbindex + 1) % self.rblength
#
#
# def first_start_index(s: str, rblength=14):
#     rb = Ringbuffer(rblength=rblength)
#     for i, c in enumerate(s):
#         rb.add(c)
#         if rb.is_start():
#             return i + 1
#     return None


def first_start_index2(s: str, seqlen: int):
    for i in range(seqlen, len(s)):
        if len(set(s[i-seqlen:i])) == seqlen:
            return i
    return None


if __name__ == '__main__':
    with open("day06.txt") as f:
        data = f.readline().strip()
    print(f"first packet: {first_start_index2(data, 4)}")
    print(f"first message: {first_start_index2(data, 14)}")
