from django import forms
from polls.models import User
from polls.models import Question, Choice


class QuestionForm(forms.ModelForm):
    MULTIPLE_CHOICES = [
        ('single', '单选'),
        ('multiple', '多选'),
    ]
    vote_type = forms.ChoiceField(choices=MULTIPLE_CHOICES, label='投票类型')

    class Meta:
        model = Question
        fields = ['question_text', 'vote_type']

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text']


class RegisterForm(forms.Form):
    username = forms.CharField(
        required=True,
        max_length=20,
        min_length=3,
        error_messages={
            'required': "用户名不能为空",
            'max_length': "用户名长度不能大于20",
            'min_length': "用户名长度不能小于3",
        }
    )
    password = forms.CharField(
        required=True,
        max_length=20,
        min_length=6,
        error_messages={
            'required': "密码不能为空",
            'max_length': "密码长度不能大于20",
            'min_length': "密码长度不能小于6",
        }
    )
    confirm_password = forms.CharField(
        required=True,
        max_length=20,
        min_length=6,
        widget=forms.PasswordInput,
        error_messages={
            'required': "确认密码不能为空",
            'max_length': "确认密码长度不能大于20",
            'min_length': "确认密码长度不能小于6",
        }
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("两次密码输入不一致！")

        return cleaned_data
 
    # 存入数据库
    def save(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        # 存入数据库
        user = User(username=username, password=password)
        user.save()


class LoginForm(forms.Form):
    # 用户名
    username = forms.CharField(
        required=True,  
        max_length=20,  
        min_length=3,  
        error_messages={
            'required': "用户名不能为空",
        }
    )
 
    # 密码
    password = forms.CharField(
        required=True,  
        max_length=20,  
        min_length=6,  
        error_messages={
            'required': "密码不能为空",
        }
    )
 
    # 校验
    def clean(self):
        # 获取输入的信息
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = User.objects.filter(username=username)  # 获得一个查询集，可以理解为一个列表
        if user.exists():
            if user[0].password != password:
                raise forms.ValidationError("密码错误")
        else:
            raise forms.ValidationError("用户不存在")
 
        return self.cleaned_data

