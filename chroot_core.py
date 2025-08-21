class GeopsChroot:
    def __init__(self, sequence):
        self.raw = list(str(sequence))
        self.core = []

    def phase_match(self, a, b):
        return abs(int(a) - int(b)) == 1

    def collapse(self):
        stack = []
        for digit in self.raw:
            if stack and self.phase_match(stack[-1], digit):
                stack.pop()
            else:
                stack.append(digit)
        self.core = stack

    def output_core(self):
        return ''.join(self.core)

    def chroot(self):
        print(f"[GeopsChroot] Core extracted: {self.output_core()}")
