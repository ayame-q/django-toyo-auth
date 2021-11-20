from django_toyo_auth.providers.toyo.provider import ToyoProvider, ToyoMail, ToyoAccount


class INIADMail(ToyoMail):
    domain = r"iniad\.org"

    def get_entry_class(self): # n期
        if self.get_is_student():
            return self.get_entry_year() - 2016
        else:
            return None


class INIADAccount(ToyoAccount):
    toyo_mail_class = INIADMail

    def get_entry_class(self):
        toyo_mail = self.toyo_mail_class(self.account.extra_data.get("email"))
        return toyo_mail.get_entry_class()


class INIADProvider(ToyoProvider):
    id = 'iniad'
    name = "INIAD"
    account_class = INIADAccount
    toyo_mail_class = INIADMail

    def get_default_scope(self):
        return [
            'profile',
            'email',
        ]

    def get_auth_params(self, request, action):
        ret = super(INIADProvider, self).get_auth_params(request, action)
        if not ret["access_type"]:
            ret["access_type"] = "online"
        ret["hd"] = "iniad.org"
        return ret

    def extract_extra_data(self, data):
        ret = super(INIADProvider, self).extract_extra_data(data)
        toyo_mail = self.toyo_mail_class(data.get("email"))
        ret.update({
            "is_iniad_member": True,
            "entry_class": toyo_mail.get_entry_class(),
        })
        return ret


provider_classes = [INIADProvider]
