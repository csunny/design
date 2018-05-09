/**
 * Created by magic on 2016/11/16.
 */

// ToDO use broserify Refactor

$(function(){
    /*导航跳转效果插件*/
    $('.nav').singlePageNav({
        offset:70
    });
    /*小屏幕导航点击关闭菜单*/
    $('.navbar-collapse a').click(function(){
        $('.navbar-collapse').collapse('hide');
    });

    new WOW().init();

    $.ajaxSetup({
        data: {csrfmiddlewaretoken: '{{ csrf_token }}' }
    });
});

var WebDomain = "http://daydreamaker.net"

var NebPay = require("nebpay");     //https://github.com/nebulasio/nebPay
var nebPay = new NebPay();
//var dappAddress = "n1tzoWc2XW1Xmt1qXEz8DGT32vAKwkb39kG";    // 智能合约的地址 测试网络  hash="cef32b5099f9ccd2cddf06bee2b24972a57168a9db71c5a1b535a5146bceb68a"
var dappAddress = "n1m1bgxfgzcuo3TERGzkEe9ohUywS1DwHmY"   // 智能合约地址 主网 hash 353b7067f1f4d0a08011a83e5ac436b523e5bea7707c0f21a00066b2445da6bd

var uploader = new plupload.Uploader({
    runtimes: 'html5, html4, flash, silverlight',
    browse_button: 'selectfiles',
    container: document.getElementById('uploader'),
    filters : {
        prevent_duplicates: true,
        max_file_size : '200mb',
        mime_types: [
            {title : "Image files", extensions : "jpg,jpeg,gif,png,tif"}
        ],

    },
    url: WebDomain + '/imshare/upload',

    // flash settings
    flash_swf_url: "{% static 'js/Moxie.swf' %}",

    // Silverlight settings
    silverlight_xap_url : "{% static 'js/Moxie.xap' %}",

    init: {
        PostInit: function() {
            document.getElementById('ossfile').innerHTML = '';

        },

        FilesAdded: function(up, files) {
            plupload.each(files, function(file) {
                if (uploader.files.length > 1){
                    uploader.removeFile(up.files[0]);
                    document.getElementById('ossfile').innerHTML = ''
                }
                document.getElementById('ossfile').innerHTML += '<div id="' + file.id + '">' + file.name + ' (' + plupload.formatSize(file.size) + ')<b></b>'
                    +'<div class="progress"><div class="progress-bar" style="width: 0%"></div></div>'
                    +'</div>';
            });
        },

        UploadProgress: function(up, file) {
            var d = document.getElementById(file.id);
            d.getElementsByTagName('b')[0].innerHTML = '<span>' + file.percent + "%</span>";
            var prog = d.getElementsByTagName('div')[0];
            var progBar = prog.getElementsByTagName('div')[0]
            progBar.style.width= 9*file.percent+'px';
            progBar.setAttribute('aria-valuenow', file.percent);
        },

        FileUploaded: function(up, file, info) {
            if (info.status==200)
            {
                document.getElementById(file.id).getElementsByTagName('b')[0].innerHTML = '&nbsp;&nbsp;上传成功';
                setTimeout("$('#choose_file').modal('hide')", 200);

                // Todo 上传成功之后跳转到详情页面
                // 执行合约
                contract()
            }
            else
            {
                document.getElementById(file.id).getElementsByTagName('b')[0].innerHTML = info.response;
            }
        },

        Error: function(up, err) {
//            set_upload_param(up, result);
            document.getElementById('console').appendChild(document.createTextNode("\nError xml:" + err.response));
        }
    }
});

uploader.init();

// ajax upload entry_code and files
$('#commit').click(function(){

    var name = $('#name').val();
    var timestamp = Date.parse(new Date());

    img_lis = uploader.files[0].name.split('.')
    var image_name = timestamp + 'image_1.' + img_lis[img_lis.length-1];

    new_multipart_params = {
        'image_name': image_name,
        'name': name
    };
    uploader.setOption({
        'multipart_params': new_multipart_params
    });

    uploader.start();


});

function contract(){
    //     todo生成参数，并将数据保存到链上

    var name = $('#name').val();
    var timestamp = Date.parse(new Date());

    img_lis = uploader.files[0].name.split('.')
    var image_name = timestamp + 'image_1.' + img_lis[img_lis.length-1];
    var to = dappAddress;    // 调用合约，指定合约地址
    var value = '0';
    var callFunction = 'save'
    var callArgs = "[\"" + name + "\", \"" + image_name + "\"]"

    nebPay.call(to, value, callFunction, callArgs, {
        callback: save_image
    })
}
// get test.jpg and render to template, the same time update the img detail information
function save_image(resp){
    // todo 记录合约信息到数据库. 根据此信息来更新图片上传者，后续图片下载直接通过此来转账。
    resp['name'] = $('#name').val();
    resp['type'] = 'txhash';
    $.ajax({
        type: "post",
        async: true,
        url: "/imshare/update",
        dataType: 'json',
        data: resp,
        success: function(result){
            console.log(result)
        }
    })
    window.location.replace(WebDomain)
}

// 点赞
$('#love').click(function(){
    var name = $("#hide_name")[0].innerHTML;
    $.ajax({
        type: "post",
        async: true,
        url: "/imshare/update",
        dataType: 'json',
        data: {'name': name, "type": 'like'},
        success: function(result){
            // todo set like count
            $("#count")[0].innerHTML = result['love_count'];
        }
    })
});

$('#download').click(function(){
    var name = $("#hide_name")[0].innerHTML;

    // todo 触发智能合约完成转账操作. 设定每次下载图片需要
    $.ajax({
        type: "post",
        async: true,
        url: "/imshare/query",
        dataType: 'json',
        data: {'name': name},
        success: function(result){
            console.log(result)

            // 调用支付
            var to = result['tx_info']['result']['from'];
            var value = 0.01
            nebPay.pay(to, value, {
                callback: setTimeout(getImage, 20000)
            })
            // todo transfer and get download url
        }
    })
});

function getImage(resp){
    // todo 出现一个modal框用于图片下载

    $('#image_address').removeClass('hide');

    var address = $('#hide_image')[0].innerHTML;
    console.log(address);
    $('#image_address')[0].href = WebDomain + "/" + address
}

// commit user commit information
$(function(){
    $("#comment_info").on('submit', function(event){

//        console.log($this.serialize());
        console.log(event)
        $.ajax({
            type: "post",
            async: true,
            url: '/imshare/contact',
            dataType: 'json',
            data: $this.serialize(),
            success: function(result){
                console.log(result);
            }
        })
    });
});




