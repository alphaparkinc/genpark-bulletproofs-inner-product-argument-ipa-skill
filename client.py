import hashlib

PRIME = 21888242871839275222246405745257275088548364400416034343698204186575808495617

class BulletproofsIPA:
    """Bulletproofs Inner Product Argument (IPA) Halving Step."""
    def __init__(self):
        self.p = PRIME

    def inner_product(self, a, b):
        return sum((x * y) % self.p for x, y in zip(a, b)) % self.p

    def prove_step(self, a, b):
        n = len(a)
        assert n == 2
        a_L, a_R = a[0], a[1]
        b_L, b_R = b[0], b[1]

        c_L = (a_L * b_R) % self.p
        c_R = (a_R * b_L) % self.p

        x = int(hashlib.sha256(f"{c_L}_{c_R}".encode()).hexdigest(), 16) % self.p
        inv_x = pow(x, self.p - 2, self.p)

        a_folded = [(a_L * x + a_R * inv_x) % self.p]
        b_folded = [(b_L * inv_x + b_R * x) % self.p]
        c_folded = (a_folded[0] * b_folded[0]) % self.p

        return {
            'c_L': c_L,
            'c_R': c_R,
            'challenge': x,
            'a_folded': a_folded,
            'b_folded': b_folded,
            'inner_product': c_folded
        }
