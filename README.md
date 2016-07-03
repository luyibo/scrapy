# scrapy
1.如何给XPath选取内容设置默认值?

XPath选取节点内的文本时，如果节点内容为空，XPath不会返回一个空字符串，而是什么都不返回，对应到列表就是对应的列表项少一项，有时候需要这样的空字符串当默认值。XPath中有一个concat函数可以实现这种效果：

text = hxs.select(‘concat(//span/text(), “”)’).extract()
对于空span会返回一个空字符串
