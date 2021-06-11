# coding: utf-8

import os
import ahocorasick


class QuestionClassifier:
    def __init__(self):
        cur_dir = '/'.join(os.path.abspath(__file__).replace('\\', '/').split('/')[:-1])
        # 特征词路径
        self.disease_path = os.path.join(cur_dir, 'dict/disease.txt')
        self.department_path = os.path.join(cur_dir, 'dict/department.txt')
        self.check_path = os.path.join(cur_dir, 'dict/check.txt')
        self.drug_path = os.path.join(cur_dir, 'dict/drug.txt')
        self.food_path = os.path.join(cur_dir, 'dict/food.txt')
        self.producer_path = os.path.join(cur_dir, 'dict/producer.txt')
        self.symptom_path = os.path.join(cur_dir, 'dict/symptom.txt')
        self.deny_path = os.path.join(cur_dir, 'dict/deny.txt')
        # 加载特征词
        self.disease_wds = [i.strip() for i in open(self.disease_path, encoding='UTF-8-sig') if i.strip()]
        self.department_wds = [i.strip() for i in open(self.department_path, encoding='UTF-8') if i.strip()]
        self.check_wds = [i.strip() for i in open(self.check_path, encoding='UTF-8') if i.strip()]
        self.drug_wds = [i.strip() for i in open(self.drug_path, encoding='UTF-8') if i.strip()]
        self.food_wds = [i.strip() for i in open(self.food_path, encoding='UTF-8') if i.strip()]
        self.producer_wds = [i.strip() for i in open(self.producer_path, encoding='UTF-8') if i.strip()]
        self.symptom_wds = [i.strip() for i in open(self.symptom_path, encoding='UTF-8') if i.strip()]
        self.keywords = set(
            self.department_wds + self.disease_wds + self.check_wds + self.drug_wds + self.food_wds + self.producer_wds + self.symptom_wds)
        self.deny_words = [i.strip() for i in open(self.deny_path, encoding='UTF-8') if i.strip()]
        # 构造关键词AC tree
        self.tree_index = 0
        self.keywords_tree = self.build_actree(list(self.keywords))
        # 构建每个关键词对应词类型的字典
        self.word_type_dict = self.build_word_type_dict()
        # 问句疑问词
        self.symptom_qwds = ['症状', '表征', '现象', '症候', '表现']
        self.cause_qwds = ['原因', '成因', '为什么', '怎么会', '怎样才', '咋样才', '怎样会', '如何会', '为啥', '为何', '如何才会', '怎么才会', '会导致',
                           '会造成']
        self.accompany_qwds = ['并发症', '并发', '一起发生', '一并发生', '一起出现', '一并出现', '一同发生', '一同出现', '伴随发生', '伴随', '共现']
        self.food_qwds = ['饮食', '饮用', '吃', '食', '伙食', '膳食', '喝', '菜', '忌口', '补品', '保健品', '食谱', '菜谱', '食用', '食物', '补品']
        self.drug_qwds = ['药', '药品', '用药', '胶囊', '口服液', '炎片']
        self.prevent_qwds = ['预防', '防范', '抵制', '抵御', '防止', '躲避', '逃避', '避开', '免得', '逃开', '避开', '避掉', '躲开', '躲掉', '绕开',
                             '怎样才能不', '怎么才能不', '咋样才能不', '咋才能不', '如何才能不',
                             '怎样才不', '怎么才不', '咋样才不', '咋才不', '如何才不',
                             '怎样才可以不', '怎么才可以不', '咋样才可以不', '咋才可以不', '如何可以不',
                             '怎样才可不', '怎么才可不', '咋样才可不', '咋才可不', '如何可不']
        self.last_time_qwds = ['周期', '多久', '多长时间', '多少时间', '几天', '几年', '多少天', '多少小时', '几个小时', '多少年']
        self.cure_way_qwds = ['怎么治疗', '如何医治', '怎么医治', '怎么治', '怎么医', '如何治', '医治方式', '疗法', '咋治', '怎么办', '咋办',
                              '治疗方法']
        self.cure_prob_qwds = ['多大概率能治好', '多大几率能治好', '治好希望大么', '几率', '几成', '比例', '可能性', '能治', '可治', '可以治', '可以医']
        self.easy_get_qwds = ['易感人群', '容易感染', '易发人群', '什么人', '哪些人', '感染', '染上', '得上']
        self.check_qwds = ['检查', '检查项目', '查出', '检查', '测出', '试出']
        self.belong_qwds = ['属于什么科', '属于', '什么科', '科室']
        self.cure_qwds = ['治疗什么', '治啥', '治疗啥', '医治啥', '治愈啥', '主治啥', '主治什么', '有什么用', '有何用', '用处', '用途',
                          '有什么好处', '有什么益处', '有何益处', '用来', '用来做啥', '用来作甚', '需要', '要']

        print('model init finished ......')

        return

    '''分类主函数'''

    def classify(self, question):
        data = {}
        keywords = self.check_keywords(question)
        if not keywords:
            return {}
        data['args'] = keywords
        # 收集问句当中所涉及到的实体类型
        word_types = []
        for t in keywords.values():
            word_types += t

        question_types = []

        # 疾病症状
        if self.check_words(self.symptom_qwds, question) and ('disease' in word_types):
            question_type = 'disease_symptom'
            question_types.append(question_type)

        # 症状对应疾病
        if self.check_words(self.symptom_qwds, question) and ('symptom' in word_types):
            question_type = 'symptom_disease'
            question_types.append(question_type)

        # 病因
        if self.check_words(self.cause_qwds, question) and ('disease' in word_types):
            question_type = 'disease_cause'
            question_types.append(question_type)

        # 并发症
        if self.check_words(self.accompany_qwds, question) and ('disease' in word_types):
            question_type = 'disease_accompany'
            question_types.append(question_type)

        # 食品
        if self.check_words(self.food_qwds, question) and ('disease' in word_types):
            deny_status = self.check_words(self.deny_words, question)
            if deny_status:
                question_type = 'disease_not_food'
            else:
                question_type = 'disease_do_food'
            question_types.append(question_type)

        # 已知食物找疾病
        if self.check_words(self.food_qwds + self.cure_qwds, question) and ('food' in word_types):
            deny_status = self.check_words(self.deny_words, question)
            if deny_status:
                question_type = 'food_not_disease'
            else:
                question_type = 'food_do_disease'
            question_types.append(question_type)

        # 治疗药物
        if self.check_words(self.drug_qwds, question) and ('disease' in word_types):
            question_type = 'disease_drug'
            question_types.append(question_type)

        # 药物对症
        if self.check_words(self.cure_qwds, question) and ('drug' in word_types):
            question_type = 'drug_disease'
            question_types.append(question_type)

        # 疾病检查
        if self.check_words(self.check_qwds, question) and ('disease' in word_types):
            question_type = 'disease_check'
            question_types.append(question_type)

        # 检查对症
        if self.check_words(self.check_qwds + self.cure_qwds, question) and ('check' in word_types):
            question_type = 'check_disease'
            question_types.append(question_type)

        # 疾病预防
        if self.check_words(self.prevent_qwds, question) and ('disease' in word_types):
            question_type = 'disease_prevent'
            question_types.append(question_type)

        # 疾病医疗周期
        if self.check_words(self.last_time_qwds, question) and ('disease' in word_types):
            question_type = 'disease_last_time'
            question_types.append(question_type)

        # 疾病治疗方式
        if self.check_words(self.cure_way_qwds, question) and ('disease' in word_types):
            question_type = 'disease_cure_way'
            question_types.append(question_type)

        # 疾病治愈可能性
        if self.check_words(self.cure_prob_qwds, question) and ('disease' in word_types):
            question_type = 'disease_cure_prob'
            question_types.append(question_type)

        # 疾病易感染人群
        if self.check_words(self.easy_get_qwds, question) and ('disease' in word_types):
            question_type = 'disease_easy_get'
            question_types.append(question_type)

        # 若没有查到相关的外部查询信息，那么则将该疾病的描述信息返回
        if question_types == [] and 'disease' in word_types:
            question_types = ['disease_desc']

        # 若没有查到相关的外部查询信息，那么则将该症状的对症返回
        if question_types == [] and 'symptom' in word_types:
            question_types = ['symptom_disease']

        data['question_types'] = question_types

        return data

    '''构造词对应的类型'''

    def build_word_type_dict(self):
        word_type_dict = dict()
        for word in self.keywords:
            word_type_dict[word] = []
            if word in self.disease_wds:
                word_type_dict[word].append('disease')
            if word in self.department_wds:
                word_type_dict[word].append('department')
            if word in self.check_wds:
                word_type_dict[word].append('check')
            if word in self.drug_wds:
                word_type_dict[word].append('drug')
            if word in self.food_wds:
                word_type_dict[word].append('food')
            if word in self.symptom_wds:
                word_type_dict[word].append('symptom')
            if word in self.producer_wds:
                word_type_dict[word].append('producer')
        return word_type_dict

    '''构造actree，加速匹配'''

    def build_actree(self, words):
        actree = ahocorasick.Automaton()
        for word in words:
            actree.add_word(word, (self.tree_index, word))
            self.tree_index += 1
        actree.make_automaton()
        return actree

    '''定位问句中的关键词'''

    def check_keywords(self, question):
        keywords = []
        for i in self.keywords_tree.iter(question):
            word = i[1][1]
            keywords.append(word)
        # 防止关键词的子串也被找到
        delete_words = []
        for word1 in keywords:
            for word2 in keywords:
                if word1 in word2 and word1 != word2:
                    delete_words.append(word1)
        final_wds = [i for i in keywords if i not in delete_words]
        final_dict = {i: self.word_type_dict.get(i) for i in final_wds}

        return final_dict

    '''基于提问特征词进行分类'''

    def check_words(self, wds, sentence):
        for wd in wds:
            if wd in sentence:
                return True
        return False

    def update_keywords(self, question_type, param1, param2):
        if question_type == "disease_symptom":
            if param1 not in self.disease_wds:
                self.disease_wds.append(param1)
                self.tree_add_word(param1)
            for word in param2:
                if word not in self.symptom_wds:
                    self.symptom_wds.append(word)
                    self.tree_add_word(word)
        elif question_type == "symptom_disease":
            if param1 not in self.symptom_wds:
                self.symptom_wds.append(param1)
                self.tree_add_word(param1)
            for word in param2:
                if word not in self.disease_wds:
                    self.disease_wds.append(word)
                    self.tree_add_word(word)
        elif question_type == "disease_accompany":
            if param1 not in self.disease_wds:
                self.disease_wds.append(param1)
                self.tree_add_word(param1)
            for word in param2:
                if word not in self.disease_wds:
                    self.disease_wds.append(word)
                    self.tree_add_word(word)
        elif question_type == "disease_not_food" or question_type == "disease_do_food":
            if param1 not in self.disease_wds:
                self.disease_wds.append(param1)
                self.tree_add_word(param1)
            for word in param2:
                if word not in self.food_wds:
                    self.food_wds.append(word)
                    self.tree_add_word(word)
        elif question_type == "food_not_disease" or question_type == "food_do_disease":
            if param1 not in self.food_wds:
                self.food_wds.append(param1)
                self.tree_add_word(param1)
            for word in param2:
                if word not in self.disease_wds:
                    self.disease_wds.append(word)
                    self.tree_add_word(word)
        elif question_type == "disease_drug":
            if param1 not in self.disease_wds:
                self.disease_wds.append(param1)
                self.tree_add_word(param1)
            for word in param2:
                if word not in self.drug_wds:
                    self.drug_wds.append(word)
                    self.tree_add_word(word)
        elif question_type == "drug_disease":
            if param1 not in self.drug_wds:
                self.drug_wds.append(param1)
                self.tree_add_word(param1)
            for word in param2:
                if word not in self.disease_wds:
                    self.disease_wds.append(word)
                    self.tree_add_word(word)
        elif question_type == "disease_check":
            if param1 not in self.disease_wds:
                self.disease_wds.append(param1)
                self.tree_add_word(param1)
            for word in param2:
                if word not in self.check_wds:
                    self.check_wds.append(word)
                    self.tree_add_word(word)
        elif question_type == "check_disease":
            if param1 not in self.check_wds:
                self.check_wds.append(param1)
                self.tree_add_word(param1)
            for word in param2:
                if word not in self.disease_wds:
                    self.disease_wds.append(word)
                    self.tree_add_word(word)
        elif question_type == "disease_prevent" or question_type == "disease_last_time" or question_type == "disease_cure_way" or question_type == "disease_cure_prob" or question_type == "disease_easy_get" or question_type == "disease_cause":
            if param1 not in self.disease_wds:
                self.disease_wds.append(param1)
                self.tree_add_word(param1)
        self.keywords_tree.make_automaton()
        param2.append(param1)
        for word in param2:
            self.word_type_dict[word] = []
            if word in self.disease_wds:
                self.word_type_dict[word].append('disease')
            if word in self.department_wds:
                self.word_type_dict[word].append('department')
            if word in self.check_wds:
                self.word_type_dict[word].append('check')
            if word in self.drug_wds:
                self.word_type_dict[word].append('drug')
            if word in self.food_wds:
                self.word_type_dict[word].append('food')
            if word in self.symptom_wds:
                self.word_type_dict[word].append('symptom')
            if word in self.producer_wds:
                self.word_type_dict[word].append('producer')

    def tree_add_word(self, word):
        self.keywords.add(word)
        self.keywords_tree.add_word(word, (self.tree_index, word))
        self.tree_index += 1


if __name__ == '__main__':
    handler = QuestionClassifier()
    while 1:
        user_question = input('input an question:')
        result = handler.classify(user_question)
        print(result)
