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
var sortCombobox;
var itemcat1;
var itemcat2;
var itemcat3;
var cid,precid;
$(function () {
    grid = $('#tbklistgrid').datagrid({
        title: '淘宝数据管理',
        iconCls: 'icon-save',
        methord: 'post',
        //sortName: 'nick',
        //sortOrder: 'desc',
        idField: 'num_iid',
        pageSize: 20,
        toolbar:toolbar,
        showFooter: true,
        nowrap:false,
        striped: true,
        frozenColumns: [[
            { field: 'ck', checkbox: true}

        ]],
        columns: [[
            { field: 'nick', title: '商家店铺', width: 100, sortable: true, rowspan: 2 , formatter: function (value, row, index) {
                return "<a href='" + row.shop_click_url + "' width='300px' >"+ row.nick +"</a>";
            }},
            { field: 'item_location', title: '地点', width: 70, sortable: true, rowspan: 2 },
            { title: '商品详细信息', colspan: 12 }
        ],[{ field: 'title', title: '商品名称', width: 300, formatter: function (value, row, index) {
                return "<a href='" + row.click_url + "' width='300px' >"+ row.title +"</a>";
            }},
            { field: 'pic_url', title: '产品图片', width: 100,  align: 'center', formatter: function (value, row, index) {

                return "<img src='" + row.pic_url + "' alt='" + row.title + "' width='100px',higth='80px' />";
            }},
            { field: 'num_iid', title: '产品编号', width: 90},
            { field: 'price', title: '商品价格', width: 50},
            { field: 'promotion_price', title: '促销折让', width: 50},
            { field: 'commission', title: '佣金', width: 50},
            { field: 'commission_num', title: '累计成交量', width: 70},
            { field: 'commission_volume', title: '累计总支出佣金量', width: 70},
            { field: 'volume', title: '30天内交易量', width: 70},
            { field: 'commission_rate', title: '佣金比率', width: 70, formatter: function (value, row, index) {
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
    sortCombobox = $('#sortcomb').combobox({
        url: '../static/fisite/js/admin/combobox_data1.json',
        valueField: 'id',
        textField: 'text',
        panelWidth: 350,
        panelHeight: 'auto',
        formatter: formatItem
    });
    itemcat1 = $('#itemcat1').combobox({
        url: '/tbkitemcats/?cid=0',
        valueField: 'cid',
        panelWidth: 'auto',
        textField: 'name',
        onSelect:function(record){
            var ul='/tbkitemcats/?cid='+$('#itemcat1').combobox('getValue');
            $('#itemcat2').combobox('reload',ul);
            precid = $('#itemcat1').combobox('getValue');
            catid = $('#itemcat2').combobox('getValue');
            cid = (catid==null||catid=="")?precid:catid;
            $('#itemcat2').combobox({visible:true});
        }
    });
    itemcat2 = $('#itemcat2').combobox({
        valueField: 'cid',
        panelWidth: 'auto',
        textField: 'name',
        visibility:"visible",
        onSelect:function(record){
            var ul='/tbkitemcats/?cid='+$('#itemcat2').combobox('getValue');
            $('#itemcat3').combobox('reload',ul);
            precid = $('#itemcat2').combobox('getValue');
            catid = $('#itemcat3').combobox('getValue');
            cid = (catid==null||catid=="")?precid:catid;
        }

    });
    itemcat3 = $('#itemcat3').combobox({
        valueField: 'cid',
        panelWidth: 'auto',
        textField: 'name',
        onSelect:function(record){
            precid = $('#itemcat2').combobox('getValue');
            catid = $('#itemcat3').combobox('getValue');
            cid = (catid==null||catid=="")?precid:catid;
        }
    });

    $('body').layout();
})

function OpensearchWin() {
    searchWin.window('open');
    searchForm.form('clear');
}

function formatItem(row){
    var s = '<span style="font-weight:bold">' + row.text + '</span><br/>' +
        '<span style="color:#888">' + row.desc + '</span>';
    return s;
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

var toolbar;
toolbar = [
    {
        text: '数据采集',
        iconCls: 'icon-search',
        handler: OpensearchWin
    },
    '-',
    {
        text: '入商品库',
        iconCls: 'icon-add',
        handler: function () {
            var rows = $('#tbklistgrid').datagrid('getSelections');
            pubRow = new Object();
            pubRow["topublish"] = JSON.stringify(rows);
            pubRow["cid"] = cid;
            /*$.post(
                "http://127.0.0.1:8000/tbkitempublish",
                pubRow,
                function(res){
                    alert( res );
            },"text").error(function(){
                    $.messager.alert("message","error when post!");
                });//操作成功后的操作！msg是后台传过来的值*/
            var dt = {'topublish':'yes2pub'};
            $.ajax({
                type: 'POST',
                url: "/tbkitempublish/",
                data: pubRow,
                success: function(msg) { alert("second success"+msg); },
                error: function(status) { alert("post error" + status); }
            });
        }

    }
];

function getSelections(){
    var ss = [];
    var rows = $('#tbklistgrid').datagrid('getSelections');

    rcount=rows.length-1;
    //alert(JSON.stringify(rows));
    /*for(var i=0; i<rows.length; i++){
        var row = rows[i];

        if(i==0){
            ss.push('[{"click_url":"'+row.click_url+'","pic_url":"'+row.pic_url+'","num_iid":"'+row.num_iid+'","title":"'+row.title+'","price":"'+row.price+'"},');
        }
        else if(i==rcount){
            ss.push('{"click_url":"'+row.click_url+'","pic_url":"'+row.pic_url+'","num_iid":"'+row.num_iid+'","title":"'+row.title+'","price":"'+row.price+'"}]');
        }else{
            ss.push('{"click_url":"'+row.click_url+'","pic_url":"'+row.pic_url+'","num_iid":"'+row.num_iid+'","title":"'+row.title+'","price":"'+row.price+'"}');
        }

    }*/
    return ss
    //$.messager.alert('Info', ss);
}

function showAll(){
    grid.datagrid({
        url: '/tbkitemlistres/'
    })
}

function SearchOK() {

    searchWin.window('close');
    grid.datagrid({ url: '/tbkitemlistres/' ,
        queryParams: {
            start_commissionRate: $("#start_commissionRate").val(),                         
            end_commissionRate  : $("#end_commissionRate").val(),                           
            start_commissionNum : $("#start_commissionNum").val(),                          
            end_commissionNum   : $("#end_commissionNum").val(),                            
            start_totalnum      : $("#start_totalnum").val(),                               
            end_totalnum        : $("#end_totalnum").val(),                                 
            start_credit        : $("#start_credit").combobox("getValue"),                  
            end_credit          : $('#end_credit').combobox('getValue'),                    
            start_price         : $("#start_price").val(),                                  
            end_price           : $("#end_price").val(),                                    
            mall_item           : ($("#mall_item").attr("checked")=="checked")?1:0 ,        
            guarantee           : ($("#guarantee").attr("checked")=="checked")?1:0 ,        
            sevendays_return    : ($("#sevendays_return").attr("checked")=="checked")?1:0  ,
            real_describe       : ($("#real_describe").attr("checked")=="checked")?1:0   ,  
            cash_coupon         : ($("#cash_coupon").attr("checked")=="checked")?1:0     ,  
            sortby              : $("#sortcomb").combobox("getValue")   ,
            itemcat             : cid

        }
    });
}

function closeSearchWindow() {
    searchWin.window('close');
}
function clearform(){
    alert($("#sortcomb").combobox("getValue") ) ;
    searchForm.form('clear');
}