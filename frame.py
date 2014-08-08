
# coding: utf-8

from bottle import static_file

HEAD = '''
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">        

<html>

<head>
<style type="text/css">
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

.wrapper {
    padding: 15px;
    width: 320px;
    position: relative;
    overflow: hidden;
} 

.boxa{
    position: relative;
    float:right;
    width: 250px;
    background: #6f0;
    margin-bottom: 1px;
    border: 1px solid #0f0;
}

.boxa:after {
    left: 100%;
    top: 50%;
    border: solid transparent;
    content: " ";
    height: 0;
    width: 0;

    position: absolute;

    pointer-events: none;

    border-color: rgba(116, 213, 19, 0);

    border-left-color: #6f0;

    border-width: 10px;

    margin-top: -10px;

}



.boxb

{

    position: relative;

    float:left;

    background: #ccc;

    width: 200px;

    margin-bottom: 1px;

    border: 1px solid #999;

}



.boxb:after {

    right: 100%;

    top: 50%;

    border: solid transparent;

    content: " ";

    height: 0;

    width: 0;

    position: absolute;

    pointer-events: none;

    border-color: rgba(116, 213, 19, 0);

    border-right-color: #ccc;

    border-width: 10px;

    margin-top: -10px;

}



/*.box:before {

content: '';

position: absolute;

border-top: 10px solid #999;

border-right: 5px solid transparent;

border-left: 5px solid transparent;

bottom: -11px;

left: 5px;

}*/

//-->

</style>

<script language="JavaScript"><!--
function reload(){
    location.reload();
}
//-->
</script>



<meta http-equiv="Content-Type" content="text/html; charset=Utf-8">

<title>[LINE]</title>



</head>



<body onLoad="setInterval('reload()', 1000*5)">

<!--↓↓ここからサイトの表示部分です↓↓-->



<p><img src="/image/talk.png" alt="トーク"width="350" usemap="navibar"> </p>

<map name="navibar">

    <area shape="rect" coords="0,0,150,120" href="talk_itiran.html" alt="戻る">

        　

        <div style="position:relative; left:20px; height:400px; width:350px; overflow-y:scroll; scrollbar-base-color:#ffffff ; scrollbar-arrow-color:#ffffff;">



            <table border=0 height="100" width="300" bgcolor="#ffffff" overflow="hidden"><tr><td>
'''

TAIL = """
        </div>

        <img src="/image/message_form1.png" alt="スタンプ">

        　<form method="post" action="/message" style="display:inline;">

            <input type="text" />　　<input type="submit" value="送信">

        </form>

        <br clear="all">

    </div> <!--allの終了タグ-->
    </body>
    </html>
"""

SELF_FRONT = """
<!-- 自分のLINE発言っぽいやつ -->
<p>
<div class="wrapper">
    <div class="boxa">
    """

SELF_TAIL = """
    </div>
</div>
</p>
<!-- 自分のLINE発言っぽいやつ ここまで -->
"""


PARTNER_FRONT = """
<!-- 自分のLINE発言っぽいやつ -->
<p>
<div class="wrapper">
    <div class="boxb">
    """

PARTNER_TAIL = """
    </div>
</div>
</p>
<!-- 自分のLINE発言っぽいやつ ここまで -->
"""

