说明，在点击图片上传的时候在LocalContractStorage里面记录一个Object：

{
    "image_name": "",
    "image_url": "",    // 此处的url为url后缀。  上链的数据
    "from": "" , 图片上传者的钱包地址
}

图片保存在服务器上， 服务器上保存三类的图片。1. 小缩略图 2. 大缩略图   3. 原图片


点赞跟下载是直接转账，即直接从下载者钱包转账到上传者钱包
