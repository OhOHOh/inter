/**
 * Created by runshen on 17-8-11.
 */

function ChooseBranch(id) {
    x = document.getElementById("Choose-Branch");
    x.innerHTML = id.text;
}

<!-- 检查表单函数 -->
function checkForm(obj) {
    // {#  alert("start"); #}
    if (obj.testaddress233.value === '') {
        alert("请输入测试版本");
        return false;
    }
    if (obj.testset233.value === '') {
        alert("请选择测试集");
        return false;
    }
    if (obj.testpatch233.value === '') {
        alert("请输入测试patch");
        return false;
    }
    return true;
}

<!-- 用于拖拽的JS函数 -->
function allowDrop(ev) {
    ev.preventDefault();
}
<!-- 源对象开始被拖动的时候调用 ondragstart -->
function drag(ev) {
    ev.dataTransfer.setData("Text", ev.target.id);
}
<!-- 源对象被拖动着在目标对象上方释放/松手 ondrop -->
function dropdiv2(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("Text");
    ev.target.appendChild(document.getElementById(data));

    x = document.getElementById("testsetinput");
    x.value += document.getElementById(data).textContent;
    x.value += ", ";
}
function dropdiv1(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("Text");
    ev.target.appendChild(document.getElementById(data));

    x = document.getElementById("testsetinput");
    del = document.getElementById(data).textContent + ", ";

    var val = x.value;
    val = val.replace(del, "");
    x.value = val;
}

<!-- 用于测试连接 TestMaster 的函数 -->
function connectTestMaster() { //在 form 表单的提交按钮上 设置的点击事件bui
    alert("开始连接TestMaster");
    // 进行 TestMaster 的连接:

    // 假设连接成功, 将表单内容提交到指定的视图函数中
    document.getElementById('submit').disabled = false;
    //window.location.href = "{% url 'test1:test1build' %}";
    alert("TestMaster连接成功!");

}
