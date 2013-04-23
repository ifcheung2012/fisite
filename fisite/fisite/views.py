from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime
from fisite.forms import ContactForm
from fisite.mytop import MyTop
from fisite.topitems.models import TbkTpItem, TbkTpItemCat
from django.core import serializers
import json


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
    return render_to_response('admin/tbkitemlist.html')


def adminmainboard(request):
    return render_to_response('admin/adminindex.html')


def tbkitemcats(request):
    url = "gw.api.taobao.com"
    port = 80
    appkey = "21430097"
    secret = "b905348541f429bcb9215cf804f7df72"
    mytbk = MyTop(url, port, appkey, secret)
    cid = int(request.GET["cid"])
    return HttpResponse(mytbk.getitemcats(cid))


def tbkitemlistres(request):
    url = "gw.api.taobao.com"
    port = 80
    appkey = "21430097"
    secret = "b905348541f429bcb9215cf804f7df72"
    tbk = MyTop(url, port, appkey, secret)
    cid = int(request.POST['itemcat'])
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
    para["end_price"] = int(request.POST['end_price']) if request.POST['end_price'] else None
    para["mall_item"] = int(request.POST['mall_item']) if request.POST['mall_item'] else None
    para["guarantee"] = int(request.POST['guarantee']) if request.POST['guarantee'] else None
    para["sevendays_return"] = int(request.POST['sevendays_return']) if request.POST['sevendays_return']  else None
    para["real_describe"] = int(request.POST['real_describe']) if request.POST['real_describe']     else None
    para["cash_coupon"] = int(request.POST['cash_coupon']) if request.POST['cash_coupon']       else None

    html = tbk.getitemslist(cid, para)
    return HttpResponse(html)


'num_iid,title,nick,pic_url,price,click_url,shop_click_url,item_location,' \
'seller_credit_score,commission,commission_rate,commission_num,commission_volume,volume,promotion_price'


def tbkitempublish(request):
    repeatdata = []
    response = HttpResponse()
    res = request.POST['topublish']
    resdata = json.loads(res)

    cid = request.POST['cid']
    tpkitemcat = TbkTpItemCat.objects.get(cid=cid)
    catid = -1

    if not tpkitemcat.cid:
        repeatdata.append("itemcatid doesn\'t exsit in database!publish failed!")
        return HttpResponse(repeatdata)

    else:
        catid =tpkitemcat.cid

    leng = len(resdata)
    for i in range(leng):
        numid = resdata[i]['num_iid']

        if TbkTpItem.objects.filter(key_id=numid):
            repeatdata.append(numid)
        else:

            tpkitem = TbkTpItem()
            tpkitem.addtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            tpkitem.clickurl = resdata[i]['click_url']
            tpkitem.imgurl = resdata[i]['pic_url']
            tpkitem.intro = resdata[i]['nick']
            tpkitem.price = resdata[i]['price']
            tpkitem.key_id = numid
            tpkitem.title = resdata[i]['title']
            tpkitem.cmsrates = resdata[i]['commission_rate']
            tpkitem.catid_id = catid
            tpkitem.status = 1

            tpkitem.save()


    repeatstr = " [Already existed numid:" + str(repeatdata) + "]" if len(repeatdata) > 0 else ""
    response.write("ok" + repeatstr)
    return response


def managelistgrid(request):
    return render_to_response('admin/itemmanage.html')


def managelistres(request):
    itemlist = serializers.serialize("json", TbkTpItem.objects.all())
    itl = json.loads(itemlist)
    resp = json.dumps(itl, sort_keys=True, indent=4, ensure_ascii=False)
    return HttpResponse(resp)




