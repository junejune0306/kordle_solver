from jamo import h2j, j2hcj

dic = (
    ('ㄲ','ㄱㄱ'),
    ('ㄸ','ㄷㄷ'),
    ('ㅃ','ㅂㅂ'),
    ('ㅆ','ㅅㅅ'),
    ('ㅉ','ㅈㅈ'),
    ('ㅐ','ㅏㅣ'),
    ('ㅒ','ㅑㅣ'),
    ('ㅔ','ㅓㅣ'),
    ('ㅖ','ㅕㅣ'),
    ('ㅘ','ㅗㅏ'),
    ('ㅙ','ㅗㅏㅣ'),
    ('ㅚ','ㅗㅣ'),
    ('ㅝ','ㅜㅓ'),
    ('ㅞ','ㅜㅓㅣ'),
    ('ㅟ','ㅜㅣ'),
    ('ㅢ','ㅡㅣ'),
    ('ㄳ','ㄱㅅ'),
    ('ㄵ','ㄴㅈ'),
    ('ㄶ','ㄴㅎ'),
    ('ㄺ','ㄹㄱ'),
    ('ㄻ','ㄹㅁ'),
    ('ㄼ','ㄹㅂ'),
    ('ㄽ','ㄹㅅ'),
    ('ㄾ','ㄹㅌ'),
    ('ㄿ','ㄹㅍ'),
    ('ㅀ','ㄹㅎ'),
    ('ㅄ','ㅂㅅ')
    )
asci = tuple(chr(i) for i in range(0x20, 0x7f))

words = []
words += open("words1.txt", "rb").read().decode("utf-8").split("\x0d\n")
words += open("words2.txt", "rb").read().decode("utf-8").split("\x0d\n")
# 순수 한글 외 다른 단어 제거
for i in range(len(words)):
    for c in asci:
        if c in words[i]:
            words[i] = None
            break
words = [i for i in words if i != None]
words = list(set(words))


disas = []
for i in words:
    if len(i) < 7:
        jamo_str = j2hcj(h2j(i))
        for fr, to in dic:
            jamo_str = jamo_str.replace(fr, to)
        if len(jamo_str) == 12:
            disas.append(jamo_str)
disas = sorted(list(set(disas)))


f = open("modified.txt", "w")
for i in disas:
    f.write(i + "\n")
f.close()
