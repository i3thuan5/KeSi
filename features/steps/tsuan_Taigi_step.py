from behave import given, then
from kesi.butkian.ji import Ji


@given(u'一字 {bun}')
def 一字(context, bun):
    context.ji = Ji(bun)


@then(u'書寫轉POJ會生做 {POJ}')
def 書寫轉POJ會生做(context, POJ):
    ji_poj = context.ji.POJ()
    assert ji_poj.hanlo == POJ, ji_poj.hanlo
    assert ji_poj.lomaji == POJ, ji_poj.lomaji
