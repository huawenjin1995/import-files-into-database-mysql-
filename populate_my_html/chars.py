#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
存放所有的字符分类
'''
##################### 汉字 #########################
_ZH_map={ # 汉字的集合
  '基本汉字':     set(chr(item) for item in range(0x4e00,   0x9fa6)), # 基本汉字，20902个汉字
  '基本汉字补充': set(chr(item) for item in range(0x9fa6,   0x9fcc)), # 基本汉字补充，38个汉字
  '汉字扩展A':    set(chr(item) for item in range(0x3400,   0x4db6)), # 汉字扩展A，6582 个汉字
  '汉字扩展B':    set(chr(item) for item in range(0x20000,  0x2a6d7)),# 汉字扩展B，42711 个汉字。大多数都是无法打印的方框。
  '汉字扩展C':    set(chr(item) for item in range(0x2a700,  0x2b735)),# 汉字扩展C，4149 个汉字。大多数都是无法打印的方框。
  '汉字扩展D':    set(chr(item) for item in range(0x2b740,  0x2b81e)),# 汉字扩展D，222 个汉字。大多数都是无法打印的方框。
  '康熙部首':     set(chr(item) for item in range(0x2f00,   0x2fd6)), # 康熙-部首，214 个。是偏旁部首。
  '康熙部首扩展': set(chr(item) for item in range(0x2e80,   0x2ef4)), # 康熙-部首扩展，116 个。是偏旁部首。
  '兼容汉字':     set(chr(item) for item in range(0xf900,   0xfada)), # 兼容汉字，474 个汉字，有一些无法打印的方框。
  '兼容汉字扩展': set(chr(item) for item in range(0x2f800,  0x2fa1e)),# 兼容扩展，542 个汉字，有一些无法打印的方框。
  'PUA_GBK_部件': set(chr(item) for item in range(0xe815,   0xe870)), # PUA(GBK)部件，91个字符。
  '部件扩展':     set(chr(item) for item in range(0xe400,   0xe5e9)), # 部件扩展，489个字符。包含了一些符号
  'PUA增补':      set(chr(item) for item in range(0xe600,   0xe6d0)), # PUA增补，208个字符。包含了一些符号
  '汉字笔画':     set(chr(item) for item in range(0x31c0,   0x31e4)), # 汉字笔画,一共 36个。是汉字笔画。
  '汉字结构':     set(chr(item) for item in range(0x2ff0,   0x2ffc)), # 汉字结构，一共12个。是汉字结构。
  '汉语注音':     set(chr(item) for item in range(0x3105,   0x3121)), # 汉语注音，一共 28个。是汉字注音。
  '汉语注音扩展': set(chr(item) for item in range(0x31a0,   0x31bb)), # 注音扩展，一共 27个。是注音扩展。
  '〇':           set(chr(item) for item in range(0x3007,   0x3008)), # 〇
}

CHChars = set() #所有的汉字
for item in ('基本汉字', '基本汉字补充', '汉字扩展A', '汉字扩展B', '汉字扩展C', '汉字扩展D', '兼容汉字', '兼容汉字扩展'):
  CHChars.update(_ZH_map[item])
CHChars.update(['○','咊',])# 手工补充的
CHCharInts=set(ord(item) for item in CHChars)
########################## 所有的拼音 （小写）########################
PyUnits=['a', 'ā', 'á', 'ǎ', 'à', 'āi', 'ái', 'ǎi', 'ài', 'ān', 'ǎn', 'àn', 'āng', 'áng', 'àng', 'āo', 'áo', 'ǎo', 'ào',
         'ba', 'bā', 'bá', 'bǎ', 'bà', 'bai', 'bāi', 'bái', 'bǎi', 'bài', 'bān', 'bǎn', 'bàn', 'bāng', 'bǎng', 'bàng',
         'bāo', 'báo', 'bǎo', 'bào', 'bei', 'bēi', 'běi', 'bèi', 'bēn', 'běn', 'bèn', 'bēng', 'béng', 'běng', 'bèng',
         'bī', 'bí', 'bǐ', 'bì', 'biān', 'biǎn', 'biàn', 'biāo', 'biǎo', 'biào', 'biē', 'bié', 'biě', 'biè', 'bīn', 'bìn',
         'bīng', 'bǐng', 'bìng', 'bo', 'bō', 'bó', 'bǒ', 'bò', 'bū', 'bú', 'bǔ', 'bù',
         'cā', 'cǎ', 'cāi', 'cái', 'cǎi', 'cài', 'cān', 'cán', 'cǎn', 'càn', 'cāng', 'cáng', 'cāo', 'cáo', 'cǎo', 'cào',
         'cè', 'cèi', 'cēn', 'cén', 'cēng', 'céng', 'cèng', 'chā', 'chá', 'chǎ', 'chà', 'chāi', 'chái', 'chǎi', 'chài',
         'chān', 'chán', 'chǎn', 'chàn', 'chāng', 'cháng', 'chǎng', 'chàng', 'chāo', 'cháo', 'chǎo', 'chào',
         'chē', 'chě', 'chè', 'chen', 'chēn', 'chén', 'chěn', 'chèn', 'chēng', 'chéng', 'chěng', 'chèng',
         'chī', 'chí', 'chǐ', 'chì', 'chōng', 'chóng', 'chǒng', 'chòng', 'chōu', 'chóu', 'chǒu', 'chòu',
         'chū', 'chú', 'chǔ', 'chù', 'chuā', 'chuāi', 'chuái', 'chuǎi', 'chuài', 'chuān', 'chuán', 'chuǎn', 'chuàn',
         'chuāng', 'chuáng', 'chuǎng', 'chuàng', 'chuī', 'chuí', 'chūn', 'chún', 'chǔn', 'chuō', 'chuò',
         'cī', 'cí', 'cǐ', 'cì', 'cōng', 'cóng', 'còu', 'cū', 'cú', 'cù', 'cuān', 'cuán', 'cuàn', 'cuī', 'cuǐ', 'cuì',
         'cūn', 'cún', 'cǔn', 'cùn', 'cuō', 'cuó', 'cuǒ', 'cuò',
         'da', 'dā', 'dá', 'dǎ', 'dà', 'dāi', 'dǎi', 'dài', 'dān', 'dǎn', 'dàn', 'dāng', 'dǎng', 'dàng',
         'dāo', 'dáo', 'dǎo', 'dào', 'de', 'dē', 'dé', 'dēi', 'děi', 'dèn', 'dēng', 'děng', 'dèng', 'dī', 'dí', 'dǐ', 'dì',
         'diǎ', 'diān', 'diǎn', 'diàn', 'diāo', 'diǎo', 'diào', 'diē', 'dié', 'dīng', 'dǐng', 'dìng', 'diū',
         'dōng', 'dǒng', 'dòng', 'dōu', 'dǒu', 'dòu', 'dū', 'dú', 'dǔ', 'dù', 'duān', 'duǎn', 'duàn',
         'duī', 'duì', 'dūn', 'dǔn', 'dùn', 'duō', 'duó', 'duǒ', 'duò',
         'e', 'ē', 'é', 'ě', 'è', 'ēi', 'éi', 'ěi', 'èi', 'ēn', 'èn', 'ēng', 'ér', 'ěr', 'èr',
         'fa', 'fā', 'fá', 'fǎ', 'fà', 'fān', 'fán', 'fǎn', 'fàn', 'fāng', 'fáng', 'fǎng', 'fàng',
         'fēi', 'féi', 'fěi', 'fèi', 'fēn', 'fén', 'fěn', 'fèn', 'fēng', 'féng', 'fěng', 'fèng', 'fó', 'fǒu', 'fū', 'fú', 'fǔ', 'fù',
         'gā', 'gá', 'gǎ', 'gà', 'gāi', 'gǎi', 'gài', 'gān', 'gǎn', 'gàn', 'gāng', 'gǎng', 'gàng', 'gāo', 'gǎo', 'gào',
         'gē', 'gé', 'gě', 'gè', 'gěi', 'gēn', 'gén', 'gěn', 'gèn', 'gēng', 'gěng', 'gèng', 'gōng', 'gǒng', 'gòng',
         'gōu', 'gǒu', 'gòu', 'gū', 'gǔ', 'gù', 'guā', 'guǎ', 'guà', 'guāi', 'guǎi', 'guài', 'guān', 'guǎn', 'guàn',
         'guāng', 'guǎng', 'guàng', 'guī', 'guǐ', 'guì', 'gǔn', 'gùn', 'guō', 'guó', 'guǒ', 'guò',
         'hā', 'há', 'hǎ', 'hà', 'hāi', 'hái', 'hǎi', 'hài', 'hān', 'hán', 'hǎn', 'hàn', 'hāng', 'háng', 'hàng',
         'hāo', 'háo', 'hǎo', 'hào', 'hē', 'hé', 'hè', 'hēi', 'hén', 'hěn', 'hèn', 'hēng', 'héng', 'hèng', 'hm', 'hng',
         'hōng', 'hóng', 'hǒng', 'hòng', 'hōu', 'hóu', 'hǒu', 'hòu', 'hū', 'hú', 'hǔ', 'hù', 'huā', 'huá', 'huà',
         'huai', 'huái', 'huài', 'huān', 'huán', 'huǎn', 'huàn', 'huāng', 'huáng', 'huǎng', 'huàng',
         'huī', 'huí', 'huǐ', 'huì', 'hūn', 'hún', 'hùn', 'huō', 'huó', 'huǒ', 'huò',
         'jī', 'jí', 'jǐ', 'jì', 'jiā', 'jiá', 'jiǎ', 'jià', 'jiān', 'jiǎn', 'jiàn',
         'jiāng', 'jiǎng', 'jiàng', 'jiāo', 'jiáo', 'jiǎo', 'jiào', 'jie', 'jiē', 'jié', 'jiě', 'jiè',
         'jīn', 'jǐn', 'jìn', 'jīng', 'jǐng', 'jìng', 'jiōng', 'jiǒng', 'jiu', 'jiū', 'jiǔ', 'jiù', 'jū', 'jú', 'jǔ', 'jù',
         'juān', 'juǎn', 'juàn', 'juē', 'jué', 'juě', 'juè', 'jūn', 'jùn',
         'kā', 'kǎ', 'kāi', 'kǎi', 'kài', 'kān', 'kǎn', 'kàn', 'kāng', 'káng', 'kàng', 'kāo', 'kǎo', 'kào',
         'kē', 'ké', 'kě', 'kè', 'kēi', 'kěn', 'kèn', 'kēng', 'kōng', 'kǒng', 'kòng', 'kōu', 'kǒu', 'kòu',
         'kū', 'kǔ', 'kù', 'kuā', 'kuǎ', 'kuà', 'kuǎi', 'kuài', 'kuān', 'kuǎn', 'kuāng', 'kuáng', 'kuǎng', 'kuàng',
         'kuī', 'kuí', 'kuǐ', 'kuì', 'kūn', 'kǔn', 'kùn', 'kuò',
         'la', 'lā', 'lá', 'lǎ', 'là', 'lai', 'lái', 'lài', 'lán', 'lǎn', 'làn', 'lāng', 'láng', 'lǎng', 'làng',
         'lāo', 'láo', 'lǎo', 'lào', 'le', 'lē', 'lè', 'lei', 'lēi', 'léi', 'lěi', 'lèi', 'lēng', 'léng', 'lěng', 'lèng',
         'li', 'lī', 'lí', 'lǐ', 'lì', 'liǎ', 'lián', 'liǎn', 'liàn', 'liáng', 'liǎng', 'liàng',
         'liāo', 'liáo', 'liǎo', 'liào', 'lie', 'liē', 'liě', 'liè', 'līn', 'lín', 'lǐn', 'lìn', 'líng', 'lǐng', 'lìng',
         'liū', 'liú', 'liǔ', 'liù', 'lo', 'lōng', 'lóng', 'lǒng', 'lòng', 'lou', 'lōu', 'lóu', 'lǒu', 'lòu',
         'lu', 'lū', 'lú', 'lǔ', 'lù', 'luán', 'luǎn', 'luàn', 'lūn', 'lún', 'lǔn', 'lùn', 'luo', 'luō', 'luó', 'luǒ', 'luò',
         'lǘ', 'lǚ', 'lǜ', 'lüè',
         'ma', 'mā', 'má', 'mǎ', 'mà', 'mái', 'mǎi', 'mài', 'mān', 'mán', 'mǎn', 'màn', 'māng', 'máng', 'mǎng',
         'māo', 'máo', 'mǎo', 'mào', 'me', 'méi', 'měi', 'mèi', 'men', 'mēn', 'mén', 'mèn', 'mēng', 'méng', 'měng', 'mèng',
         'mī', 'mí', 'mǐ', 'mì', 'mián', 'miǎn', 'miàn', 'miāo', 'miáo', 'miǎo', 'miào', 'miē', 'miè', 'mín', 'mǐn',
         'míng', 'mǐng', 'mìng', 'miù', 'mō', 'mó', 'mǒ', 'mò', 'mōu', 'móu', 'mǒu', 'mú', 'mǔ', 'mù',
         'ń', 'ň', 'na', 'nā', 'ná', 'nǎ', 'nà', 'nǎi', 'nài', 'nān', 'nán', 'nǎn', 'nàn', 'nāng', 'náng', 'nǎng', 'nàng',
         'nāo', 'náo', 'nǎo', 'nào', 'ne', 'né', 'nè', 'něi', 'nèi', 'nèn', 'néng', 'ńg', 'ňg', 'nī', 'ní', 'nǐ', 'nì',
         'niān', 'nián', 'niǎn', 'niàn', 'niáng', 'niàng', 'niǎo', 'niào', 'niē', 'nié', 'niè', 'nín', 'níng', 'nǐng', 'nìng',
         'niū', 'niú', 'niǔ', 'niù', 'nóng', 'nòng', 'nòu', 'nú', 'nǔ', 'nù', 'nuǎn', 'nún', 'nuó', 'nuò',
         'nǚ', 'nǜ', 'nüè',
         'ō', 'ó', 'ǒ', 'ò', 'ōu', 'óu', 'ǒu', 'òu',
         'pā', 'pá', 'pà', 'pāi', 'pái', 'pǎi', 'pài', 'pān', 'pán', 'pàn', 'pāng', 'páng', 'pǎng', 'pàng',
         'pāo', 'páo', 'pǎo', 'pào', 'pēi', 'péi', 'pèi', 'pēn', 'pén', 'pèn', 'pēng', 'péng', 'pěng', 'pèng',
         'pī', 'pí', 'pǐ', 'pì', 'piān', 'pián', 'piǎn', 'piàn', 'piāo', 'piáo', 'piǎo', 'piào', 'piē', 'piě', 'piè',
         'pīn', 'pín', 'pǐn', 'pìn', 'pīng', 'píng', 'po', 'pō', 'pó', 'pǒ', 'pò', 'pōu', 'póu', 'pǒu', 'pū', 'pú', 'pǔ',
         'pù', 'qī', 'qí', 'qǐ', 'qì', 'qiā', 'qiá', 'qiǎ', 'qià', 'qiān', 'qián', 'qiǎn', 'qiàn',
         'qiāng', 'qiáng', 'qiǎng', 'qiàng', 'qiāo', 'qiáo', 'qiǎo', 'qiào', 'qiē', 'qié', 'qiě', 'qiè',
         'qīn', 'qín', 'qǐn', 'qìn', 'qīng', 'qíng', 'qǐng', 'qìng', 'qióng', 'qiū', 'qiú', 'qiǔ',
         'qu', 'qū', 'qú', 'qǔ', 'qù', 'quān', 'quán', 'quǎn', 'quàn', 'quē', 'qué', 'què', 'qūn', 'qún',
         'rán', 'rǎn', 'rāng', 'ráng', 'rǎng', 'ràng', 'ráo', 'rǎo', 'rào', 'rě', 'rè', 'rén', 'rěn', 'rèn', 'rēng', 'réng',
         'rì', 'róng', 'rǒng', 'róu', 'ròu', 'rú', 'rǔ', 'rù', 'ruá', 'ruán', 'ruǎn',
         'ruí', 'ruǐ', 'ruì', 'rún', 'rùn', 'ruó', 'ruò',
         'sā', 'sǎ', 'sà', 'sāi', 'sài', 'sān', 'sǎn', 'sàn', 'sāng', 'sǎng', 'sàng', 'sāo', 'sǎo', 'sào',
         'sè', 'sēn', 'sēng', 'shā', 'shá', 'shǎ', 'shà', 'shāi', 'shǎi', 'shài', 'shān', 'shǎn', 'shàn',
         'shang', 'shāng', 'shǎng', 'shàng', 'shāo', 'sháo', 'shǎo', 'shào', 'shē', 'shé', 'shě', 'shè', 'shéi',
         'shēn', 'shén', 'shěn', 'shèn', 'shēng', 'shéng', 'shěng', 'shèng', 'shi', 'shī', 'shí', 'shǐ', 'shì',
         'shōu', 'shóu', 'shǒu', 'shòu', 'shū', 'shú', 'shǔ', 'shù', 'shuā', 'shuǎ', 'shuà', 'shuāi', 'shuǎi', 'shuài',
         'shuān', 'shuàn', 'shuāng', 'shuǎng', 'shuí', 'shuǐ', 'shuì', 'shǔn', 'shùn', 'shuō', 'shuò',
         'sī', 'sǐ', 'sì', 'sōng', 'sóng', 'sǒng', 'sòng', 'sōu', 'sǒu', 'sòu', 'sū', 'sú', 'sù', 'suān', 'suàn',
         'suī', 'suí', 'suǐ', 'suì', 'sūn', 'sǔn', 'suō', 'suǒ',
         'tā', 'tǎ', 'tà', 'tāi', 'tái', 'tǎi', 'tài', 'tān', 'tán', 'tǎn', 'tàn', 'tāng', 'táng', 'tǎng', 'tàng',
         'tāo', 'táo', 'tǎo', 'tào', 'te', 'tè', 'tēi', 'tēng', 'téng', 'tī', 'tí', 'tǐ', 'tì',
         'tiān', 'tián', 'tiǎn', 'tiàn', 'tiāo', 'tiáo', 'tiǎo', 'tiào', 'tiē', 'tiě', 'tiè', 'tīng', 'tíng', 'tǐng', 'tìng',
         'tōng', 'tóng', 'tǒng', 'tòng', 'tōu', 'tóu', 'tǒu', 'tòu', 'tū', 'tú', 'tǔ', 'tù', 'tuān', 'tuán', 'tuǎn', 'tuàn',
         'tuī', 'tuí', 'tuǐ', 'tuì', 'tūn', 'tún', 'tǔn', 'tùn', 'tuō', 'tuó', 'tuǒ', 'tuò',
         'wa', 'wā', 'wá', 'wǎ', 'wà', 'wāi', 'wǎi', 'wài', 'wān', 'wán', 'wǎn', 'wàn', 'wāng', 'wáng', 'wǎng', 'wàng',
         'wēi', 'wéi', 'wěi', 'wèi', 'wēn', 'wén', 'wěn', 'wèn', 'wēng', 'wěng', 'wèng',
         'wō', 'wǒ', 'wò', 'wū', 'wú', 'wǔ', 'wù',
         'xī', 'xí', 'xǐ', 'xì', 'xiā', 'xiá', 'xià', 'xiān', 'xián', 'xiǎn', 'xiàn', 'xiāng', 'xiáng', 'xiǎng', 'xiàng',
         'xiāo', 'xiáo', 'xiǎo', 'xiào', 'xiē', 'xié', 'xiě', 'xiè', 'xīn', 'xín', 'xǐn', 'xìn', 'xīng', 'xíng', 'xǐng', 'xìng',
         'xiōng', 'xióng', 'xiòng', 'xiū', 'xiǔ', 'xiù', 'xu', 'xū', 'xú', 'xǔ', 'xù',
         'xuān', 'xuán', 'xuǎn', 'xuàn', 'xuē', 'xué', 'xuě', 'xuè', 'xūn', 'xún', 'xùn',
         'ya', 'yā', 'yá', 'yǎ', 'yà', 'yān', 'yán', 'yǎn', 'yàn', 'yāng', 'yáng', 'yǎng', 'yàng', 'yāo', 'yáo', 'yǎo', 'yào',
         'yē', 'yé', 'yě', 'yè', 'yī', 'yí', 'yǐ', 'yì', 'yīn', 'yín', 'yǐn', 'yìn', 'yīng', 'yíng', 'yǐng', 'yìng',
         'yo', 'yō', 'yōng', 'yóng', 'yǒng', 'yòng', 'yōu', 'yóu', 'yǒu', 'yòu', 'yū', 'yú', 'yǔ', 'yù',
         'yuān', 'yuán', 'yuǎn', 'yuàn', 'yuē', 'yuě', 'yuè', 'yūn', 'yún', 'yǔn', 'yùn',
         'zā', 'zá', 'zǎ', 'zāi', 'zǎi', 'zài', 'zan', 'zān', 'zán', 'zǎn', 'zàn', 'zāng', 'zǎng', 'zàng',
         'zāo', 'záo', 'zǎo', 'zào', 'zé', 'zè', 'zéi', 'zěn', 'zèn', 'zēng', 'zèng', 'zha', 'zhā', 'zhá', 'zhǎ', 'zhà',
         'zhāi', 'zhái', 'zhǎi', 'zhài', 'zhān', 'zhǎn', 'zhàn', 'zhāng', 'zhǎng', 'zhàng',
         'zhāo', 'zháo', 'zhǎo', 'zhào', 'zhe', 'zhē', 'zhé', 'zhě', 'zhè', 'zhèi',
         'zhēn', 'zhěn', 'zhèn', 'zhēng', 'zhěng', 'zhèng', 'zhī', 'zhí', 'zhǐ', 'zhì',
         'zhōng', 'zhǒng', 'zhòng', 'zhōu', 'zhóu', 'zhǒu', 'zhòu', 'zhū', 'zhú', 'zhǔ', 'zhù',
         'zhuā', 'zhuǎ', 'zhuāi', 'zhuǎi', 'zhuài', 'zhuān', 'zhuǎn', 'zhuàn', 'zhuāng', 'zhuǎng', 'zhuàng',
         'zhuī', 'zhuì', 'zhūn', 'zhǔn', 'zhuō', 'zhuó', 'zī', 'zǐ', 'zì', 'zōng', 'zǒng', 'zòng',
         'zōu', 'zǒu', 'zòu', 'zū', 'zú', 'zǔ', 'zuān', 'zuǎn', 'zuàn', 'zuī', 'zuǐ', 'zuì',
         'zūn', 'zǔn', 'zùn', 'zuō', 'zuó', 'zuǒ', 'zuò',
         ### 补充的
         'ǹ','án','fiào','fóu','nóu','qiōng','suǎn','suò','bian','tou','zi','pěn','jia','sha',
              'guo','eng','keum','ḿ','m','zuo','duǐ','yi','cǔ','roe','xiú','zí','qi','ńg','ng',
              'ń','ta','pěi','er','shíkě','qiānkè','gōngfēn',
              'háokè','bǎikè','gōnglǐ','būn','mangmi','guái','yīngchǐ','jiālún','sǎi',
              'mē','mè','pǎn','cà','diè','dóu','nuán','hua','biáo','nái','ěn',
              'chuì','còng','nǐn','wěi','ré','sùn','zēn','zhùn','zang','cang','zhuǐ',
              'hǎilǐ','shuàng','xiǒng','bǎiwǎ','líwǎ','kěng','dang','ruàn','ròng','nǒng','něng',
              'ra','tiao','nuǒ','lǎi','zhán','càng','lié','xiǎ','sa','tèng',
              'rǒu','shūn','huang','yīnglǐ','ran','wu','yue','zhan','zhu','rèng','hǎixún','yu','zhai',
              'duo','huo','ji','si','huai','chang','chuo','dian','jin','ju','da','liang','qian','san',
              'pen','sang','sui','suo','nang','lu','zhou','tun','qie','gú','ǹg',]

PyUnits=  set(item.lower() for item in PyUnits) #所有的拼音 （小写）
#################### 拼音中出现的字符（包含大小写） ###################
PyCharInts=set(ord(char) for char in  (''.join(PyUnits)+''.join(PyUnits).upper())) #拼音中出现的字符的编码值
PyChars=set(chr(item) for item in PyCharInts)# 拼音字符
################### 英文字符（包含大小写）  #################
ENGChars=set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') #英文字符（半角）
ENGCharList = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
ENGCharInts=set(ord(item) for item in ENGChars) #英文字符（半角）编码值

ENGChars2=set('ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ') #英文字符（全角）
ENGCharList2 = list('ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ')
ENGCharInts2=set(ord(item) for item in ENGChars2) #英文字符（半全角）编码值
####################### 数字  ######################
NUMChars=set('0123456789') # 数字（半角）
NUMCharList=list('0123456789')
NUMCharInts=set(ord(item) for item in NUMChars) #数字编码值

NUMChars2=set('０１２３４５６７８９') #  数字（全角）
NUMCharList2=list('０１２３４５６７８９')
NUMCharInts2=set(ord(item) for item in NUMChars2) #数字（全角）编码值

NUMChars3=set('ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩⅪⅫⅬⅭⅮⅯ') #  数字（罗马）
NUMCharsList3=list('ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩⅪⅫⅬⅭⅮⅯ')
NUMCharInts3=set(ord(item) for item in NUMChars3) #数字（罗马）编码值

NUMChars4=set('ⅰⅱⅲⅳⅴⅵⅶⅷⅸⅹⅺⅻⅼⅽⅾⅿ') #  数字（罗马）
NUMCharsList4=list('ⅰⅱⅲⅳⅴⅵⅶⅷⅸⅹⅺⅻⅼⅽⅾⅿ')
NUMCharInts4=set(ord(item) for item in NUMChars4) #数字（罗马）编码值

##################### 编号 #################
SerialNumChars1=set('①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳㉑㉒㉓㉔㉕㉖㉗㉘㉙㉚㉛㉜㉝㉞㉟') #数字编号：① ~ ⑳ : 9312 ~ 9331 ㉑ ~ ㉟ ：12881 ~ 12895
SerialNumCharInts1=set(ord(item) for item in SerialNumChars1) #数字编号：① ~ ⑳ : 9312 ~ 9331

SerialNumChars2=set('⑴⑵⑶⑷⑸⑹⑺⑻⑼⑽⑾⑿⒀⒁⒂⒃⒄⒅⒆⒇') #数字编号：⑴ ~ ⒇ : 9332 ~ 9351
SerialNumCharInts2=set(ord(item) for item in SerialNumChars2) #数字编号：⑴ ~ ⒇ : 9332 ~ 9351

SerialNumChars3=set('⒈⒉⒊⒋⒌⒍⒎⒏⒐⒑⒒⒓⒔⒕⒖⒗⒘⒙⒚⒛') #数字编号：⒈ ~ ⒛: 9352 ~ 9371
SerialNumCharInts3=set(ord(item) for item in SerialNumChars3) #数字编号：⒈ ~ ⒛: 9352 ~ 9371

SerialNumChars7=set('⓪⓵⓶⓷⓸⓹⓺⓻⓼⓽⓾⓫⓬⓭⓮⓯⓰⓱⓲⓳⓴⓿') #数字编号：⓪ ~ ⓿: 9450 ~ 9471
SerialNumCharInts7=set(ord(item) for item in SerialNumChars7) #数字编号：⓪ ~ ⓿: 9450 ~ 9471

SerialNumChars4=set('⒜⒝⒞⒟⒠⒡⒢⒣⒤⒥⒦⒧⒨⒩⒪⒫⒬⒭⒮⒯⒰⒱⒲⒳⒴⒵') #字母编号：⒜ ~ ⒵: 9372 ~ 9397
SerialNumCharInts4=set(ord(item) for item in SerialNumChars4) #字母编号：⒜ ~ ⒵: 9372 ~ 9397

SerialNumChars5=set('ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ') #字母编号：Ⓐ ~ Ⓩ: 9398 ~ 9423
SerialNumCharInts5=set(ord(item) for item in SerialNumChars5) #字母编号：Ⓐ ~ Ⓩ: 9398 ~ 9423

SerialNumChars6=set('ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ') #字母编号：ⓐ ~ ⓩ: 9424 ~ 9449
SerialNumCharInts6=set(ord(item) for item in SerialNumChars6) #字母编号：ⓐ ~ ⓩ: 9424 ~ 9449

SerialNumChars9=set('㈠㈡㈢㈣㈤㈥㈦㈧㈨') #汉字编号 ㈠ ~ ㈩ ：12832 ~ 12841
SerialNumCharInts9=set(ord(item) for item in SerialNumChars9) #汉字编号 ㈠ ~ ㈩ ：12832 ~ 12841

SerialNumChars8=set('㉈㉉㉊㉋㉌㉍㉎㉏') #汉字编号 ㉈ ~ ㉏ ：12872 ~ 12897
SerialNumCharInts8=set(ord(item) for item in SerialNumChars8) #汉字编号 ㉈ ~ ㉏ ：12872 ~ 12879


###################### 标点 ##########################
ENGPuncChars=set('{}()[].,:;?!\'"<>|/') #英文标点
ENGPuncCharInts=set(ord(item) for item in ENGPuncChars) #英文标点编码值
CHPuncChars=set('。？！，、；：．“”‘’「」『』〔〕［］〖〗（）【】——…～……《》〈〉﹏·・｛｝｀／︱｜―﹑＿')# 中文标点
CHPuncCharInts=set(ord(item) for item in CHPuncChars) #中文标点编码值
##################### 符号　###########################
ENGSymbolChars=set('^@¥#&$%*-=+~\\') #英文符号
CHSymbolChars=set('＠＃￥％……＆×－—＝＋_'
                  ''
                  '﹋‖'
                  '☰☷☳☴☵☲☶☱⚊⚋' #八卦
                  '〡〢〣〤〥〦〧〨〩十〸'#中文数字
                  '一丨丿丶乛亅㇏㇂⺂㇟' #汉字笔画
                  '﹃￢﹄﹂' #竖排的引号
                  '㇀ê⌞⌝Ăềế') #中文符号，有些看起来相同，但是编码不同。
CHMusicSymbols='♯♭♮＜＞⌒'
CHPhoneticSymbolChars=set('ㄅㄆㄇㄈㄪㄉㄊㄋㄌㄍㄎㄫㄏㄐㄑㄬㄒㄓㄔㄕㄖㄗㄘㄙㄧㄨㄩㄚㄛㄜㄝㄞㄟㄠㄡㄢㄣㄤㄥㄦ') #中文注音
CHTonSymbolChars=set('ˉˊˇ˘ˋ')# 中文声调
CHTonValueSymChars=set('ʨʤɣəɕ')#音值
GreekSymbolChars=set('αΑβΒγΓΖζΙιΚκΧχΗηΝνΟοτΤΡρΕεΜμ∧λΩωΨψΦφΘθ∑σς∏πδΔΞξΥυ') #希腊字母
MathSymbolChars=set('±÷≠≌≡≈≮≯＜＞≤≥‰∞√∝∵∴∠△⊥∪∩∫∑″′˚°℃π℉⊆ΚΤ∶')#数学符号
PhysicalSymbolChars=set('Å⇌') #物理符号
ForignSymbolChars=set('かвḤṅДйецоśгṇасИыЛиṣṃñĔшкКудГчлнбзöɦмрВṭьптらБ')#外文
##################### 其它符号 ###########################
SymbolChars=set('®□▲●→≌≈＜＞∷⌒⊙○☽◎⫏│ʔ☉')





