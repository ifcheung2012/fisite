/**
 * Created with PyCharm.
 * User: ifcheung
 * Date: 13-4-9
 * Time: 下午1:02
 * To change this template use File | Settings | File Templates.
 */
function qq(value,name){
    alert(value+":"+name)
}

var searchWin;
var searchForm;
var grid;

$(function () {
    grid = $('#tbklistgrid').datagrid({
        title: '淘宝数据管理',
        iconCls: 'icon-save',
        methord: 'post',

        sortName: 'nick',
        sortOrder: 'desc',
        idField: 'num_iid',
        pageSize: 20,
        toolbar:toolbar,
        showFooter: true,
        nowrap:false,
        striped: true,
        frozenColumns: [[
            { field: 'ck', checkbox: true, rowspan: 2 }

        ]],
        columns: [[
            { field: 'nick', title: '商家店铺', width: 100, sortable: true, rowspan: 2 , formatter: function (value, row, index) {
                return "<a href='" + row.shop_click_url + "' width='300px' >"+ row.nick +"</a>";
            }},
            { field: 'item_location', title: '地点', width: 70, sortable: true, rowspan: 2 },
            { title: '商品详细信息', colspan: 12 }
        ],[{ field: 'title', title: '商品名称', width: 300, sortable: true, formatter: function (value, row, index) {
                return "<a href='" + row.click_url + "' width='300px' >"+ row.title +"</a>";
            }},
            { field: 'pic_url', title: '产品图片', width: 100,  align: 'center', formatter: function (value, row, index) {

                return "<img src='" + row.pic_url + "' alt='" + row.title + "' width='100px',higth='80px' />";
            }},
            { field: 'num_iid', title: '产品编号', width: 90, sortable: true},
            { field: 'price', title: '商品价格', width: 50, sortable: true},
            { field: 'promotion_price', title: '促销折让', width: 50, sortable: true},
            { field: 'commission', title: '佣金', width: 50, sortable: true},
            { field: 'commission_num', title: '累计成交量', width: 70, sortable: true},
            { field: 'commission_volume', title: '累计总支出佣金量', width: 70, sortable: true},
            { field: 'volume', title: '30天内交易量', width: 70, sortable: true},
            { field: 'commission_rate', title: '佣金比率', width: 70, sortable: true, formatter: function (value, row, index) {
                return (row.commission_rate / 100) + '%'  //todo better to format it in jsondata
            }},
            { field: 'status', title: '状态', width: 50,  formatter: function (value, row, index) {
                if (row.price >100) {

                    return "不错";
                } else {

                    return "还行";
                }
            }, styler: function (value, row, index) {
                if (row.price >100) {
                    return 'background-color:#ffee00;color:red;';
                }
            }

            }]
        ],
        fit: true,
        pagination: true,
        rownumbers: true,
        fitColumns: true,
        singleSelect: false,
        onLoadSuccess: onLoadSuccess
    });
    searchWin = $('#search-window').window({
        iconCls: 'icon-search',
        closed: true,
        modal: true
    });
    searchForm = searchWin.find('searchform');

    $('body').layout();
})

function OpensearchWin() {
    searchWin.window('open');
    searchForm.form('clear');
}


function onLoadSuccess(data){
    var merges = [{
        index: 2,
        rowspan: 2
    },{
        index: 5,
        rowspan: 2
    },{
        index: 7,
        rowspan: 2
    }];
    for(var i=0; i<merges.length; i++){
        $(this).datagrid('mergeCells',{
            index: merges[i].index,
            field: 'nick',
            rowspan: merges[i].rowspan
        }).datagrid('mergeCells',{
                index: merges[i].index,
                field: 'item_location',
                rowspan: merges[i].rowspan
            });
    }
}

function pagerFilter(data){
    if (typeof data.length == 'number' && typeof data.splice == 'function'){	// is array
        data = {
            total: data.length,
            rows: data
        }
    }
    var dg = $(this);
    var opts = dg.datagrid('options');
    var pager = dg.datagrid('getPager');
    pager.pagination({
        onSelectPage:function(pageNum, pageSize){
            opts.pageNumber = pageNum;
            opts.pageSize = pageSize;
            pager.pagination('refresh',{
                pageNumber:pageNum,
                pageSize:pageSize
            });
            dg.datagrid('loadData',data);
        }
    });
    if (!data.originalRows){
        data.originalRows = (data.rows);
    }
    var start = (opts.pageNumber-1)*parseInt(opts.pageSize);
    var end = start + parseInt(opts.pageSize);
    data.rows = (data.originalRows.slice(start, end));
    return data;
}

var toolbar = [{
    text: '数据采集',
    iconCls: 'icon-search',
    handler: OpensearchWin
    }, '-',{
    text:'入商品库',
    iconCls:'icon-add',
    handler:function(){alert('add')}
    }];


function showAll(){
    grid.datagrid({
        url: 'http://127.0.0.1:8000/tbkitemlistres/'
    })
}
function SearchOK() {
    var start_commissionRate = $("#start_commissionRate").val();
    var end_commissionRate = $("#end_commissionRate").val();
    var start_commissionNum = $("#start_commissionNum").val();
    var end_commissionNum = $("#end_commissionNum").val();
    var start_totalnum = $("#start_totalnum").val();
    var end_totalnum = $("#end_totalnum").val();
    var start_credit = $("#start_credit").combobox("getValue");
    var end_credit = $('#end_credit').combobox('getValue');
    var start_price = $("#start_price").val();
    var end_price = $("#end_price").val();
    var mall_item         =   ($("#mall_item").attr("checked")=="checked")?1:0 ;
    var guarantee         =   ($("#guarantee").attr("checked")=="checked")?1:0 ;
    var sevendays_return  =   ($("#sevendays_return").attr("checked")=="checked")?1:0  ;
    var real_describe     =   ($("#real_describe").attr("checked")=="checked")?1:0   ;
    var cash_coupon       =   ($("#cash_coupon").attr("checked")=="checked")?1:0     ;


    searchWin.window('close');
    grid.datagrid({ url: 'http://127.0.0.1:8000/tbkitemlistres/' ,
        queryParams: {
            start_commissionRate: start_commissionRate,
            end_commissionRate  : end_commissionNum,
            start_commissionNum : start_commissionNum,
            end_commissionNum   : end_commissionNum,
            start_totalnum      : start_totalnum,
            end_totalnum        : end_totalnum,
            start_credit        : start_credit,
            end_credit          : end_credit,
            start_price         : start_price,
            end_price           : end_price,
            mall_item           : mall_item,
            guarantee           : guarantee,
            sevendays_return    : sevendays_return,
            real_describe       : real_describe,
            cash_coupon         : cash_coupon

        }
    });
}
function closeSearchWindow() {
    searchWin.window('close');
}
function clearform(){
    alert(($("#mall_item").attr("checked")=="checked")?1:0) ;
    searchForm.form('clear');
}