import re

TIAUHO_TIAUHU_PIO = {
    '1': '',
    '2': '\u0301',
    '3': '\u0300',
    '4': '',
    '5': '\u0302',
    '6': '\u030c',
    '7': '\u0304',
    '8': '\u030d',
    '9': '\u0306'
}


class 臺羅數字調轉白話字():

    @classmethod
    def 轉白話字(cls, 聲, 韻, 調):
        白話字聲 = cls.轉白話字聲(聲)
        白話字韻 = cls.轉白話字韻(韻)
        白話字傳統調韻 = cls.白話字韻標傳統調(白話字韻, 調)
        print('白話字聲=', 白話字聲)
        print('白話字韻=', 白話字韻)
        print('白話字傳統調韻=', 白話字傳統調韻)

        return (
            白話字聲 +
            白話字傳統調韻
        )

    @classmethod
    def 轉白話字聲(cls, 聲):
        白話字聲 = None
        if 聲 == 'ts':
            白話字聲 = 'ch'
        elif 聲 == 'tsh':
            白話字聲 = 'chh'
        else:
            白話字聲 = 聲
        return 白話字聲

    @classmethod
    def 轉白話字韻(cls, un):
        un = (
            un
            .replace('nn', 'ⁿ')
            .replace('oo', 'o͘')
            .replace('ua', 'oa')
            .replace('ue', 'oe')
            .replace('ing', 'eng')
            .replace('ik', 'ek')
        )
        return un

    @classmethod
    def 白話字韻標傳統調(cls, 白話字韻無調, 調):
        該標調的字 = ''
        if 'o͘' in 白話字韻無調:
            該標調的字 = 'o͘'
        elif re.search('(iau)|(oai)', 白話字韻無調):
            # 三元音 攏標佇a面頂
            該標調的字 = 'a'
        elif re.search('[aeiou]{2}', 白話字韻無調):
            # 雙元音
            if 白話字韻無調[0] == 'i':
                該標調的字 = 白話字韻無調[1]
            elif 白話字韻無調[1] == 'i':
                該標調的字 = 白話字韻無調[0]
            elif len(白話字韻無調) == 2:
                # xx
                該標調的字 = 白話字韻無調[0]
            elif 白話字韻無調[-1] == 'ⁿ' and 白話字韻無調[-2:] != 'hⁿ':
                # xxⁿ
                該標調的字 = 白話字韻無調[0]
            else:
                # xxn, xxng, xxhⁿ
                該標調的字 = 白話字韻無調[1]
        elif re.search('[aeiou]', 白話字韻無調):
            # 單元音
            該標調的字 = 白話字韻無調[0]
        elif 'ng' in 白話字韻無調:
            # ng, mng
            該標調的字 = 'n'
        elif 'm' in 白話字韻無調:
            該標調的字 = 'm'
        print('白話字韻無調={}, 該標調的字={}, 調={}'.format(
            白話字韻無調, 該標調的字, 調))
        結果 = cls.加上白話字調符(白話字韻無調, 該標調的字, 調)
        return 結果

    @classmethod
    def 加上白話字調符(cls, 白話字韻無調, 標調字母, 調):
        if 調 == '\u030b':
            調 = '\u0306'
        return 白話字韻無調.replace(標調字母, 標調字母 + 調, 1)
