from behave import given, then

from kesi import Ku


@given(u'一句漢字是 {bun} ê字')
def 一句漢字(context, bun):
    context.ku = Ku(bun)


@given(u'一句編碼是 {pianbe} ê字')
def 一句編碼(context, pianbe):
    bun = ''.join(map(lambda x: chr(int(x, 16)), pianbe.split(',')))
    context.ku = Ku(bun)


@then(u'書寫ê編碼是 {pianbe}')
def 書寫ê編碼是(context, pianbe):
    ku_unicode_list = [hex(ord(ji)) for ji in context.ku.hanlo]
    # 轉做hex，khah好比對
    pianbe_list = [hex(int(ji, 16)) for ji in pianbe.split(',')]
    assert ku_unicode_list == pianbe_list, ku_unicode_list


@then(u'書寫ê漢字mài變做 {bun}')
def step_impl(context, bun):
    assert bun not in context.ku.hanlo, context.ku.hanlo
