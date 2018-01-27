# -*- coding: utf-8 -*-
from fallen.models.setting import Setting


class SettingsManager:
    __setting = None
    __dbpath = "sqlite:///"

    def __init__(self, dbpath=None):
        self.__dbpath = dbpath
        self.__setting = Setting

    def install(self) -> None:
        self.__setting.db.create_all()

    def uninstall(self) -> None:
        self.__setting.db.drop_all()

    def create_setting(self, name, value, active=True) -> any:
        """
        Creates settings to hold sensitive data
        :param str value: the value of the setting
        :param str name: The name of the setting
        :param bool active: is the setting active.
        """
        setting_value = Setting.query.filter_by(name=name).first()

        if setting_value is not None:
            setting_value.value = value
        else:
            setting = Setting(name=name, value=value, active=active)
            self.__setting.db.session.add(setting)

        return self.__setting.db.session.commit()

    @staticmethod
    def get_setting(name) -> dict:
        """
        Retrieves a setting from the database
        :param str name: name of the setting
        :returns dict
        """
        return Setting.query.filter_by(name=name).first()

    def remove_setting(self, name) -> None:
        """
        Removes a setting from the database
        :param str name: name of the setting to remove
        :returns exception|str
        """
        setting_value = Setting.query.filter_by(name=name).first()
        if setting_value is not None:
            self.__setting.db.session.delete(setting_value)
            self.__setting.db.session.commit()
