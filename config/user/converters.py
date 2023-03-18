class YearConverter:
    # 正则，匹配url上面的内容
    regex = '[0-9]{4}'  # 自定义匹配的规则

    # 数据的类型的转换
    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%04d' % value
