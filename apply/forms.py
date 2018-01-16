from django import forms
from .models import Apply
from multiupload.fields import MultiFileField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, HTML, Field
from crispy_forms.bootstrap import (
    PrependedText,
    PrependedAppendedText,
    FormActions
)

class ApplyForm(forms.ModelForm):
    attachments = MultiFileField(label = "Обоснование проекта, резюме, смета, рекомендации (максмум - 5 файлов)", min_num=1, max_num=5)
    email = forms.EmailField(required=True)
    def __init__(self, *args, **kwargs):
        super(ApplyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(Fieldset(
        "Отправте заявку, воспользовавшись формой:",
        'second_name',
        'first_name',
        'email',
        HTML("""
        <p>Пожалуйста, используйте текстовой формат для файла проекта (rtf, doc, docx, odt)</p>
        """),
        Field('attachments', css_class='file', type='file', data_show_upload="false", data_show_preview="false", data_msg_placeholder="Выбирите файлы для загрузки"), HTML("{% csrf_token %}"),
        FormActions(Submit('purchase', 'ОТПРАВИТЬ', css_class='btn-primary btn-block'))
        ))
    class Meta:
        model = Apply
        fields = [
        "first_name",
        "second_name",
        "email",
        "attachments",
        ]
