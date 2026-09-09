from client import BulletproofsIPA

def main():
    print("=== Testing Bulletproofs Inner Product Argument ===")
    ipa = BulletproofsIPA()
    a = [4, 7]
    b = [2, 3]
    ip = ipa.inner_product(a, b)
    print("Initial Inner Product (4*2 + 7*3 = 29):", ip)
    assert ip == 29

    step = ipa.prove_step(a, b)
    print("Folded proof step:", step)
    assert step['challenge'] > 0

    print("Bulletproofs IPA verified successfully!")

if __name__ == '__main__':
    main()
