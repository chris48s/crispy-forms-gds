from django import forms

from crispy_forms_gds.helper import FormHelper
from crispy_forms_gds.layout import HTML, Button, Div, Layout


class ButtonsForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ButtonsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(Button.primary("add", "Add contact")),
            Div(Button.secondary("find", "Find address")),
            Div(Button.secondary("win", "Win lottery", disabled=True)),
            Div(Button.warning("delete", "Delete account")),
        )

    def get_button(self):
        if "add" in self.data:
            return "Add contact"
        elif "find" in self.data:
            return "Find address"
        elif "delete" in self.data:
            return "Delete account"
        else:
            return "Win lottery"

    def valid_layout(self):
        message = 'You clicked the "%s" button.' % self.get_button()
        self.helper.layout = Layout(HTML.p(message), Button("continue", "Continue"))
