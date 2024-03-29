from behave import given, then, when
from itertools import zip_longest

from kesi import Ku, TuiBeTse


@given(u'一句 {bun} 建立句仔')
def 建立句仔(context, bun):
    context.ku = Ku(bun)


@given(u'Kan-na傳 lomaji: {lomaji}建立句仔')
def step_impl(context, lomaji):
    context.ku = Ku(lomaji=lomaji)


@then('hanlo是 {hanlo}')
def hanlo是(context, hanlo):
    assert context.ku.hanlo == hanlo, context.ku.hanlo


@then('lomaji是 {lomaji}')
def lomaji是(context, lomaji):
    assert context.ku.lomaji == lomaji, context.ku.lomaji


@then('kiphanlo是 {kiphanlo}')
def kiphanlo是(context, kiphanlo):
    assert context.ku.kiphanlo == kiphanlo, context.ku.kiphanlo


@given(u'兩句 "{hanlo}" kah "{lomaji}" 做伙建立一 ê 句仔')
def 做伙建立句仔(context, hanlo, lomaji):
    context.ku = Ku(hanlo, lomaji)


@given(u'兩句 {hanlo} kah {lomaji} 做伙建立一 ê 句仔')
def 做伙建立句仔2(context, hanlo, lomaji):
    context.ku = Ku(hanlo, lomaji)


@then(u'詞仔是')
def 詞仔是(context):
    for su, tapan in zip_longest(context.ku, context.table):
        assert su.hanlo == tapan['hanlo'], 'su.hanlo={}'.format(su.hanlo)
        assert su.lomaji == tapan['lomaji'], 'su.lomaji={}'.format(su.lomaji)


@then(u'字仔是')
def 字仔是(context):
    for ji, tapan in zip_longest(context.ku.thianji(), context.table):
        assert ji.hanlo == tapan['hanlo'], ji.hanlo
        assert ji.lomaji == tapan['lomaji'], ji.lomaji


@then(u'詞仔 mā ē-tàng 提著字，像第{kui:d}詞攏總{jisoo:d}字，字仔是')
def 第幾詞ê字仔是(context, kui, jisoo):
    su = context.ku[kui]
    assert len(su) == jisoo
    for ji, tapan in zip_longest(su, context.table):
        assert ji.hanlo == tapan['hanlo']
        assert ji.lomaji == tapan['lomaji']


@when(u'{hanlo} kah {lomaji} 若欲對句仔會發錯誤')
def 若欲對句仔會發錯誤(context, hanlo, lomaji):
    u_tshongoo = False
    try:
        Ku(hanlo, lomaji)
    except TuiBeTse:
        u_tshongoo = True
    assert u_tshongoo


@then(u'轉出KIP句，伊 ê hanlo是 {hanlo}')
def 轉做KIP(context, hanlo):
    assert context.ku.KIP().hanlo == hanlo, context.ku.KIP().hanlo


@then(u'轉出POJ句，伊 ê hanlo是 {hanlo}')
def 轉做POJ(context, hanlo):
    assert context.ku.POJ().hanlo == hanlo, context.ku.POJ().hanlo


@then(u'原本ê句仔猶原是 {bun}')
def 原本ê句仔猶原是(context, bun):
    assert context.ku.hanlo == bun


@then(u'轉出POJ句，伊 ê lomaji是 {lomaji}')
def 轉出POJ句伊lomaji是(context, lomaji):
    assert context.ku.POJ().lomaji == lomaji, context.ku.POJ().lomaji


@then(u'轉出KIP句，伊 ê lomaji是 {lomaji}')
def 轉出KIP句伊lomaji是(context, lomaji):
    assert context.ku.KIP().lomaji == lomaji, context.ku.KIP().lomaji
