from behave import given, when, then


@given(u'一句 "{bun}"')
def utsitku(context, bun):
    context.bun = bun


@when(u'建立句物件')
def kianlipku(context):
    context.ku = Ku(context.bun)


@then(u'taibun是 "{taibun}"')
def taibun_si(context, taibun):
    assert context.ku.taibun == taibun


@then(u'lomaji是 "{lomaji}"')
def lomaji_si(context, lomaji):
    assert context.ku.lomaji == lomaji


@then(u'hanji是 "{hanji}"')
def hanji_si(context, hanji):
    assert context.ku.hanji == hanji


@given(u'兩句 "{hanlo}" kah "{tsuanlo}"')
def step_impl(context, hanlo, tsuanlo):
    context.hanlo = hanlo
    context.tsuanlo = tsuanlo


@when(u'做伙建立一 ê 句物件')
def tsohue_kianlip(context):
    context.ku = Ku(context.hanlo, context.tsuanlo)


@then(u'攏總 "{kui}" 詞')
def su_longtsong(context, kui):
    assert len(context.ku.網出詞陣列()) == kui


@then(u'攏總 "{kui}" 字')
def ji_longtsong(context, kui):
    assert len(context.ku.篩出字陣列()) == kui


@when(u'選擇 uì 第 "{kui}" ê 詞斷做兩句')
def tngku(context, kui):
    sutin = context.ku.網出詞陣列()
    it = Ku(sutin[:kui])
    ji = Ku(sutin[kui:])
    context.ku_tin = [it, ji]


@then(u'第{kui}句taibun是 "{taibun}"')
def giamtsitku(context, kui, taibun):
    assert context.ku_tin[kui].taibun == taibun


@when(u'提 TL')
def theh_tailo(context):
    context.lomaji = context.ku.TL()


@when(u'提 POJ')
def theh_poj(context):
    context.lomaji = context.ku.POJ()


@when(u'轉做 TL 傳統調')
def tsuan_tailo(context):
    context.tailo = context.ku.轉音('TL')


@given(u'一段聲 "test_Kaldi.wav"')
def tsitsiann(context):
    raise NotImplementedError(u'STEP: Given 一段聲 "test_Kaldi.wav"')


@when(u'接 TauPhahJi')
def tsiap_tauphahji(context):
    context.ku = tauphahji(context.bun)


@when(u'接 Kaldi')
def tsiap_kaldi(context):
    raise NotImplementedError(u'STEP: When 接 Kaldi')
