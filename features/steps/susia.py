from behave import given, then
from kesi import Ku


@given(u'一句 {bun}')
def 一句(context, bun):
    context.mih = Ku(bun)


@then(u'書寫轉POJ會生做 {POJ}')
def 書寫轉POJ會生做(context, POJ):
    poj = context.mih.POJ()
    assert poj.hanlo == POJ, poj.hanlo
    assert poj.lomaji == POJ, poj.lomaji


@then(u'書寫轉KIP會生做 {KIP}')
def 書寫轉KIP會生做(context, KIP):
    tailo = context.mih.KIP()
    assert tailo.hanlo == KIP, tailo.hanlo
    assert tailo.lomaji == KIP, tailo.lomaji
    assert tailo == context.mih.TL()
