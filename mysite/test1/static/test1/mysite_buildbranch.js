/**
 * Created by runshen on 17-8-11.
 */

$(function () {
    $("#accordion").accordion({
        collapsible: true,
        heightStyle: "content"
    });
});

<!-- 编译 按钮的点击响应 -->
function click666(id) {
    alert('click!');
    $(document).ready(function () {
        $(id).css('background', 'url("{% static "images/loading.gif" %}") no-repeat')
    });
}
<!-- 开始 按钮的点击响应 -->
function click667(id) {
    $(document).ready(function () {
        $(id).css('background', 'url("{% static "images/loading.gif" %}") no-repeat')
    });
    <!-- 发送 "运行" 指令给 TestMaster , 并从 TestMaster 获取机器的运行情况 -->
    alert("发送 '运行' 指令给 TestMaster , 并从 TestMaster 获取机器的运行情况, 并运行情况显示在 Machines Info 界面上, 跳转到 Machines Info 界面");


    window.location.href = "{% url 'test1:test1machines' %}";
}
