from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime
from fisite.forms import ContactForm
from fisite.mytop import MyTop
from fisite.topitems.models import TbkTpItem,TbkTpItemCat


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            return HttpResponseRedirect('/contact/')
    else:
        form = ContactForm()
    return render_to_response('contact_form.html', {'form': form})


def hello(request):
    # now=datetime.datetime.now()
    # meta=request.META['HTTP_USER_AGENT']
    # return HttpResponse("Hello world %s \n " % meta)
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td></tr><tr><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))


def search_form(request):
    return render_to_response('search_form.html')


def search(request):
    if 'q' in request.POST:
        message = 'you search for:%r' % request.POST['q']
    else:
        message = 'you submitted an empty form.'
    return HttpResponse(message)


def current_datetime(request):
    import pdb

    pdb.set_trace()  # XXX BREAKPOINT
    now = datetime.datetime.now()
    # t=get_template('current_datetime.html')
    # html=t.render(Context({'current_date':now}))
    # return HttpResponse(html)
    return render_to_response('current_datetime.html', {'current_date': now})


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    # assert True
    html = "<html><body>In %s hour(s),it will be %s.</body></html>" % (
        offset, dt)
    return HttpResponse(html)


def tbkitemlist(request):
    #url = "gw.api.taobao.com"
    #port = 80
    #appkey = "21430097"
    #secret = "b905348541f429bcb9215cf804f7df72"
    #tbk = MyTop(url, port, appkey, secret)
    #cid = 50020808
    #html = tbk.getitemslist(cid)
    return render_to_response('tbkitemlist.html')


def adminmainboard(request):
    return render_to_response('adminindex.html')


def tbkitemlistres(request):
    url = "gw.api.taobao.com"
    port = 80
    appkey = "21430097"
    secret = "b905348541f429bcb9215cf804f7df72"
    tbk = MyTop(url, port, appkey, secret)
    #cid = 50020808
    cid = 50004889
    para = {}
    para["start_commissionRate"] = request.POST['start_commissionRate']
    para["end_commissionNum"] = request.POST['end_commissionRate']
    para["start_commissionNum"] = request.POST['start_commissionNum']
    para["end_commissionNum"] = request.POST['end_commissionNum']
    para["start_totalnum"] = request.POST['start_totalnum']
    para["end_totalnum"] = request.POST['end_totalnum']
    para["start_credit"] = request.POST['start_credit']
    para["end_credit"] = request.POST['end_credit']
    para["start_price"] = request.POST['start_price']
    para["sort"] = request.POST['sortby']
    para["end_price"] = int(request.POST['end_price'])
    para["mall_item"] = int(request.POST['mall_item'])
    para["guarantee"] = int(request.POST['guarantee'])
    para["sevendays_return"] = int(request.POST['sevendays_return'])
    para["real_describe"] = int(request.POST['real_describe'])
    para["cash_coupon"] = int(request.POST['cash_coupon'])

    html = tbk.getitemslist(cid, para)
    return HttpResponse(html)

'num_iid,title,nick,pic_url,price,click_url,shop_click_url,item_location,' \
'seller_credit_score,commission,commission_rate,commission_num,commission_volume,volume,promotion_price'
def tbkitempublish(request):
    #tbkitem = TbkTpItem()
    #tbkitem.addtime = datetime.datetime.now()
    #tbkitem.clickurl =  request.GET['click_url']
    #tbkitem.imgurl  =   request.GET['pic_url']
    #tbkitem.key_id  =   request.GET['num_iid']
    #tbkitem.title   =   request.GET['title']
    #tbkitem.price   =   request.GET['price']
    #tbkitem.save()
    result = request.GET['res']
    return HttpResponse("success:"+result)




