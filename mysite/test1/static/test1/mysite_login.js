<!-- AJAX -->
function showHint(id) {
    if (id.value.length === 0) {
        $(document).ready(function () {
            $(id).css('background-color', '#FFFFFF');
        });
        return;
    }
    $.ajax({
        url: "/test1/api/login/",
        type: 'POST',
        data: {'username': $(id).val()},

        <!-- 服务器成功返回数据 data -->
        success: function (data) {
            if (data === '1') {
                // alert("终于在数据库表中找到了" + str);绿色;
                $(document).ready(function () {
                    $(id).css('background-color', '#C1FFE4');
                });
            } else {
                // alert("还没有找到" + str);红色;
                $(document).ready(function () {
                    $(id).css('background-color', '#FF9797');
                });
            }
        }
    });
}
