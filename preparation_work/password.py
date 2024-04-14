import sha512_crypt


class Password:
    rounds = 10000
    prefix = f"$6$rounds={rounds}$"

    @classmethod
    async def encrypt(cls, password: str) -> str:
        hash_password = sha512_crypt.encrypt(password, rounds=cls.rounds)
        split_parts = hash_password.split("$", 3)
        return split_parts[-1]

    @classmethod
    async def verify(cls, encrypt_password: str, password: str) -> bool:
        return sha512_crypt.verify(password, cls.prefix + encrypt_password)


async def main():
    password = "123456789"
    print(f"{password}: {await Password.encrypt(password)}")

    password = "0987654321"
    print(f"{password}: {await Password.encrypt(password)}")

    password = "135792468"
    print(f"{password}: {await Password.encrypt(password)}")

    # 123456789: cNnpg26D2W2fXs.G$kZq9v/2yYY2cj0F1Y.Snv2zBU8SiOveKtLv3i8rRCWV7D8qd1tPvRBB99tXE9qelo71K.uCB9y1K02e1OTi/V0
    # 0987654321: s6xObIOvtm7Op25k$Hd.w0xZ2J.XqU98o0Q7EZ.inDvb5iQWPP3LGvd/BmcSNXZSvt1KBUVbxxCyf4XsskM5PTswqEkHJC03B1XLCx1
    # 135792468: 2D3JVJbAhrEZ.xCR$KnxJOBQahBWE7P2G2Q766YUh1TWqs58.apoa6WTw4ctOY6VW5cN2unYbZL1E..d/0vT.rb92S8QeA6VhWdVvJ.


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
