__author__ = 'john'

class Url(object):
    @classmethod
    def shorten(cls, full_url):
        """전체 url 줄이기"""

    # Url 클래스의 인스턴스 생성
    instance = cls()
    instance.full_url = full_url
    instance_short_url = instance.__create_short_url()
    Url.__save_url_mapping(instance)
    return instance

    @classmethod
    def get_by_short_url(cls, short_url):
        """shor_url에 일치하는 Url 인스턴스 반환"""
        url_mapping = Url.load_url_mapping()
        return url_mapping.get(short_url)

    def __create_short_url(self):
        """짧은 url 생성 저장 후 반환"""
        last_short_url = Url.__load_last_short_url()
        short_url = self.__increment_string(last_short_url)
        Url.__save_last_short_url(short_url)