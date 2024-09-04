$(document).ready(function() {
    $('#id_username').on('input', function() {
        var username = $(this).val();
        var feedback = $('#username-feedback');

        // 检查用户名是否为空
        if (username === '') {
            feedback.text('用户名不能为空').css('color', 'red');
            return;
        }

        // 检查用户名长度是否小于3
        if (username.length < 3) {
            feedback.text('用户名长度不能小于3').css('color', 'red');
            return;
        }

        if (username.length > 20) {
            feedback.text('用户名长度不能大于20').css('color', 'red');
            return;
        }

        // 发送 AJAX 请求检查用户名是否已存在
        $.ajax({
            url: '/polls/ajax/check_username/',
            data: {
                'username': username
            },
            dataType: 'json',
            success: function(data) {
                if (data.is_taken) {
                    feedback.text('用户名已存在').css('color', 'red');
                } else {
                    feedback.text('用户名可用').css('color', 'green');
                }
            }
        });
    });
    $('#id_password, #id_confirm_password').on('input', function() {
        var password = $('#id_password').val();
        var confirmPassword = $('#id_confirm_password').val();
        var feedback = $('#password-feedback');
        var confirmFeedback = $('#confirm-password-feedback');

        var strengthBar = $('#strengthBar');

        // 检查密码长度
        if (password.length < 6) {
            feedback.text('密码长度不能小于6').css('color', 'red');
        } 
        else if (password.length > 20) {
            feedback.text('密码长度不能大于20').css('color', 'red');
        } 
        else {
            feedback.text('');
        }

        // 检查确认密码是否与密码一致
        if (confirmPassword !== password) {
            confirmFeedback.text('请与上方密码输入一致').css('color', 'blue');
        } else {
            confirmFeedback.text('密码一致').css('color', 'green');
        }

        // 检查密码强度
        var strength = 0;
        if (password.match(/[a-z]+/)) strength += 1;
        if (password.match(/[A-Z]+/)) strength += 1;
        if (password.match(/[0-9]+/)) strength += 1;
        if (password.match(/[$@#&!]+/)) strength += 1;

        switch (strength) {
            case 1:
                strengthBar.val(25);
                break;
            case 2:
                strengthBar.val(50);
                break;
            case 3:
                strengthBar.val(75);
                break;
            case 4:
                strengthBar.val(100);
                break;
            default:
                strengthBar.val(0);
        }
    });

});