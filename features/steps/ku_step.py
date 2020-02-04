from behave import given, when, then
from kesi import Ku
from itertools import zip_longest


@given(u'一句 {bun} 建立句仔')
def 建立句仔(context, bun):
    context.ku = Ku(bun)


@then(u'hanlo是 {hanlo}')
def hanlo是(context, hanlo):
    assert context.ku.hanlo == hanlo


@then(u'lomaji是 {lomaji}')
def lomaji是(context, lomaji):
    assert context.ku.lomaji == lomaji


@given(u'兩句 {hanlo} kah {lomaji} 做伙建立一 ê 句仔')
def 做伙建立句仔(context, hanlo, lomaji):
    context.ku = Ku(hanlo, lomaji)


@then(u'詞仔是')
def 詞仔是(context):
    for su, tapan in zip_longest(context.ku, context.table):
        assert su.hanlo == tapan['hanlo']
        assert su.lomaji == tapan['lomaji']


@then(u'字仔是')
def 字仔是(context):
    for ji, tapan in zip_longest(context.ku.thianji(), context.table):
        assert ji.hanlo == tapan['hanlo']
        assert ji.lomaji == tapan['lomaji']


@then(u'第 {kui} 詞 ê 字仔是')
def 第幾詞ê字仔是(context, kui):
    su = context.ku[kui]
    for ji, tapan in zip_longest(su, context.table):
        assert ji.hanlo == tapan['hanlo']
        assert ji.lomaji == tapan['lomaji']


@then(u'轉出TL句，伊 ê hanlo是 {hanlo}')
def 轉做TL(context, hanlo):
    assert context.ku.TL().hanlo == hanlo


@then(u'轉出POJ句，伊 ê hanlo是 {hanlo}')
def 轉做POJ(context, hanlo):
    assert context.ku.POJ().hanlo == hanlo


@then(u'原本ê句仔猶原是 {bun}')
def 原本ê句仔猶原是(context, bun):
    assert context.ku.hanlo == bun
