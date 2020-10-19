import random
import string


def random_string(n=1):
    """[summary]
        文字数nを与えるとその長さのランダムな英数字の文字列を作成する
    Args:
        n ([int]): 文字数(初期値=1)

    Returns:
        [str]: 作成された文字
    """
    randlst = [
        random.choice(
            string.ascii_letters +
            string.digits) for i in range(n)]
    return ''.join(randlst)


if __name__ == "__main__":
    print(random_string())
