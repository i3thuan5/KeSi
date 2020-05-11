from behave import given, then
from kesi.butkian.ji import Ji
from kesi import Ku


@given(u'一字 {bun}')
def 一字(context, bun):
    context.mih = Ji(bun)


@given(u'一句 {bun}')
def 一句(context, bun):
    context.mih = Ku(bun)


@then(u'書寫轉POJ會生做 {POJ}')
def 書寫轉POJ會生做(context, POJ):
    poj = context.mih.POJ()
    assert poj.hanlo == POJ, poj.hanlo
    assert poj.lomaji == POJ, poj.lomaji


@then(u'書寫轉TL會生做 {TL}')
def 書寫轉TL會生做(context, TL):
    tailo = context.mih.TL()
    assert tailo.hanlo == TL, tailo.hanlo
    assert tailo.lomaji == TL, tailo.lomaji
