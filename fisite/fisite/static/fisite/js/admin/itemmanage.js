/**
 * Created with PyCharm.
 * User: ifcheung
 * Date: 13-4-12
 * Time: 下午3:01
 * To change this template use File | Settings | File Templates.
 */
var managelistgrid;
$(function () {
    managelistgrid = $('#managelistgrid').datagrid({
        url:"/managelistgrid/",
        title: '商品数据管理',
        iconCls: 'icon-save',
        methord: 'post',
        //sortName: 'nick',
        //sortOrder: 'desc',
        idField: 'key_id',
        pageSize: 20,
        toolbar:toolb,
        showFooter: true,
        nowrap:false,
        striped: true,
        frozenColumns: [[
            { field: 'ck', checkbox: true }

        ]],
        columns: [[
            { field: 'intro', title: '商家店铺', width: 100, sortable: true, rowspan: 2 , formatter: function (value, row, index) {
                return "<a href='" + row.click_url + "' width='300px' >"+ row.intro +"</a>";
            }},

            { title: '商品详细信息', colspan: 6 }
        ],[{ field: 'title', title: '商品名称', width: 300, formatter: function (value, row, index) {
            return "<a href='" + row.clickurl + "' width='300px' >"+ row.title +"</a>";
        }},
            { field: 'imgurl', title: '产品图片', width: 100,  align: 'center', formatter: function (value, row, index) {

                return "<img src='" + row.imgurl + "' alt='" + row.title + "' width='100px',higth='80px' />";
            }},
            { field: 'key_id', title: '产品编号', width: 90},
            { field: 'price', title: '商品价格', width: 50},
            { field: 'cmsrates', title: '佣金比率', width: 70, formatter: function (value, row, index) {
                return (row.cmsrates / 100) + '%'  //todo better to format it in jsondata
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
        onLoadSuccess: onLoadSuccess1
    });



    $('body').layout();
})

var toolb = [{
    text:'Add',
    iconCls:'icon-add',
    handler:function(){alert('add')}
},{
    text:'Cut',
    iconCls:'icon-cut',
    handler:function(){alert('cut')}
},'-',{
    text:'Save',
    iconCls:'icon-save',
    handler:function(){alert('save')}
}];


function onLoadSuccess1(data){
    /*var merges = [{
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
    }*/
}