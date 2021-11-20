from allauth.socialaccount.providers.google.provider import GoogleProvider, GoogleAccount
import re

class ToyoMail:
    email = ""
    domain = r"toyo\.jp"

    def __init__(self, email, domain=None):
        self.email = email
        if domain:
            self.domain = domain.replace(".", r"\.")

    def match(self):
        return re.match(r"s(?P<student_id>(?P<major>([0-9])([0-9a-z])([0-9a-z]{2}))((?P<entry_year>[0-9]{2})[0-9]{4}))[0-9]{1}@" + self.domain, self.email)

    def get_is_student(self):
        if self.match():
            return True

    def get_student_id(self):
        if self.match():
            return self.match().group("student_id").upper()

    def get_major(self): # 学部学科専攻
        majors = {
            "1110": {"faculty": "文学部", "department": "哲学科"},
            "1120": {"faculty": "文学部", "department": "インド哲学科"},
            "2120": {"faculty": "文学部", "department": "インド哲学科 イブニングコース"},
            "1130": {"faculty": "文学部", "department": "中国哲学文学科"},
            "1140": {"faculty": "文学部", "department": "日本文学文化学科"},
            "2140": {"faculty": "文学部", "department": "日本文学文化学科 イブニングコース"},
            "1150": {"faculty": "文学部", "department": "英米文学科"},
            "1160": {"faculty": "文学部", "department": "史学科"},
            "1171": {"faculty": "文学部", "department": "教育学科", "course": "人間発達専攻"},
            "1172": {"faculty": "文学部", "department": "教育学科", "course": "初等教育専攻"},
            "2170": {"faculty": "文学部", "department": "教育学科 イブニングコース"},
            "1180": {"faculty": "文学部", "department": "英語コミュニケーション学科"},
            "1190": {"faculty": "文学部", "department": "東洋思想文化学科"},
            "2190": {"faculty": "文学部", "department": "東洋思想文化学科 イブニングコース"},
            "11a0": {"faculty": "文学部", "department": "国際文化コミュニケーション学科"},
            "1210": {"faculty": "経済学部", "department": "経済学科"},
            "2210": {"faculty": "経済学部", "department": "経済学科 イブニングコース"},
            "1220": {"faculty": "経済学部", "department": "国際経済学科"},
            "1230": {"faculty": "経済学部", "department": "総合政策学科"},
            "1310": {"faculty": "経営学部", "department": "経営学科"},
            "2310": {"faculty": "経営学部", "department": "経営学科 イブニングコース"},
            "1320": {"faculty": "経営学部", "department": "マーケティング学科"},
            "1330": {"faculty": "経営学部", "department": "会計ファイナンス学科"},
            "1410": {"faculty": "法学部", "department": "法律学科"},
            "2410": {"faculty": "法学部", "department": "法律学科 イブニングコース"},
            "1420": {"faculty": "法学部", "department": "企業法学科"},
            "1510": {"faculty": "社会学部", "department": "社会学科"},
            "2510": {"faculty": "社会学部", "department": "社会学科 イブニングコース"},
            "1520": {"faculty": "社会学部", "department": "社会文化システム学科"},
            "1530": {"faculty": "社会学部", "department": "社会福祉学科"},
            "2530": {"faculty": "社会学部", "department": "社会福祉学科 イブニングコース"},
            "1540": {"faculty": "社会学部", "department": "メディアコミュニケーション学科"},
            "1550": {"faculty": "社会学部", "department": "社会心理学科"},
            "1810": {"faculty": "国際地域学部", "department": "国際地域学科"},
            "2810": {"faculty": "国際地域学部", "department": "国際地域学科 イブニングコース"},
            "1820": {"faculty": "国際地域学部", "department": "国際観光学科"},
            "1D10": {"faculty": "国際学部", "department": "グローバル･イノベーション学科"},
            "1D20": {"faculty": "国際学部", "department": "国際地域学科"},
            "2D20": {"faculty": "国際学部", "department": "国際地域学科 イブニングコース"},
            "1e10": {"faculty": "国際観光学部", "department": "国際観光学科"},
            "1a11": {"faculty": "ライフデザイン学部", "department": "生活支援学科", "course": "生活支援学専攻"},
            "1a12": {"faculty": "ライフデザイン学部", "department": "生活支援学科", "course": "子ども支援学専攻"},
            "1a20": {"faculty": "ライフデザイン学部", "department": "健康スポーツ学科"},
            "1a30": {"faculty": "ライフデザイン学部", "department": "人間環境デザイン学科"},
            "16a0": {"faculty": "理工学部", "department": "機械工学科"},
            "16b0": {"faculty": "理工学部", "department": "生体医工学科"},
            "16c0": {"faculty": "理工学部", "department": "電気電子情報工学科"},
            "16d0": {"faculty": "理工学部", "department": "応用化学科"},
            "16e0": {"faculty": "理工学部", "department": "都市環境デザイン学科"},
            "16f0": {"faculty": "理工学部", "department": "建築学科"},
            "1b10": {"faculty": "総合情報学部", "department": "総合情報学科"},
            "1f10": {"faculty": "情報連携学部", "department": "情報連携学科"},
            "1910": {"faculty": "生命科学部", "department": "生命科学科"},
            "1920": {"faculty": "生命科学部", "department": "応用生物科学科"},
            "1930": {"faculty": "生命科学部", "department": "食環境科学科"},
            "1c11": {"faculty": "食環境科学部", "department": "食環境科学科", "course": "フードサイエンス専攻"},
            "1c12": {"faculty": "食環境科学部", "department": "食環境科学科", "course": "スポーツ･食品機能専攻"},
            "1c20": {"faculty": "食環境科学部", "department": "健康栄養学科"},
        }
        if self.match():
            return majors[self.match().group("major").lower()]
        else:
            return None

    def get_faculty(self): # 学部
        if self.get_major():
            return self.get_major()["faculty"]
        else:
            return None

    def get_department(self): # 学科
        if self.get_major():
            return self.get_major()["department"]
        else:
            return None

    def get_course(self): # 専攻
        if self.get_major():
            return self.get_major().get("course")
        else:
            return None

    def get_entry_year(self):
        if self.match():
            return int(self.match().group("entry_year")) + 2000


class ToyoAccount(GoogleAccount):
    toyo_mail_class = ToyoMail

    def get_is_toyo_member(self):
        return self.account.extra_data.get("is_toyo_member")

    def get_is_iniad_member(self):
        return self.account.extra_data.get("is_iniad_member")

    def get_is_student(self):
        return self.account.extra_data.get("is_student")

    def get_student_id(self):
        return self.account.extra_data.get("student_id")

    def get_entry_year(self):
        return self.account.extra_data.get("entry_year")

    def get_faculty(self):
        return self.account.extra_data.get("faculty")

    def get_department(self):
        return self.account.extra_data.get("department")

    def get_course(self):
        return self.account.extra_data.get("course")

    def get_full_major(self):
        return self.get_faculty() + self.get_department() + (self.get_course() if self.get_course() else "")


class ToyoProvider(GoogleProvider):
    id = 'toyo'
    name = "Toyo"
    account_class = ToyoAccount
    toyo_mail_class = ToyoMail

    def get_default_scope(self):
        return [
            'profile',
            'email',
        ]

    def get_auth_params(self, request, action):
        ret = super(ToyoProvider, self).get_auth_params(request, action)
        if not ret["access_type"]:
            ret["access_type"] = "online"
        ret["hd"] = "toyo.jp"
        return ret

    def extract_extra_data(self, data):
        ret = super(ToyoProvider, self).extract_extra_data(data)
        toyo_mail = self.toyo_mail_class(data.get("email"))
        ret.update({
            "is_toyo_member": True,
            "is_iniad_member": False,
            "is_student": toyo_mail.get_is_student(),
            "student_id": toyo_mail.get_student_id(),
            "faculty": toyo_mail.get_faculty(),
            "department": toyo_mail.get_department(),
            "course": toyo_mail.get_course(),
            "entry_year": toyo_mail.get_entry_year(),
        })
        return ret


provider_classes = [ToyoProvider]
