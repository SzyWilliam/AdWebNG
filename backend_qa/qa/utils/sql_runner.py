# coding: utf-8

from py2neo import Graph


class SQLRunner:
    def __init__(self):
        self.g = Graph("http://localhost:7474", auth=("neo4j", "000720"))  # 连接neo4j
        self.num_limit = 20

    '''执行cypher查询，并返回相应结果'''

    def run_sql(self, parser_result, sql_type):
        if sql_type == "query":
            final_answers = []
            for query in parser_result:
                question_type = query['question_type']
                sqls = query['sql']
                answers = []
                for sql in sqls:
                    result = self.g.run(sql).data()
                    answers += result
                final_answer = self.answer_prettify(question_type, answers)
                if final_answer:
                    final_answers.append(final_answer)
            return final_answers
        else:
            t = False
            for query in parser_result:
                sqls = query['sql']
                for sql in sqls:
                    result = self.g.run(sql).data()
                    for r in result:
                        if r and any(r.values()):
                            t = True
                            break
            return t

    '''根据对应的question_type，调用相应的回复模板'''

    def answer_prettify(self, question_type, answers):
        if not answers or not any(answers):
            return ''
        if question_type == 'disease_symptom':
            desc = [i['n.name'] for i in answers]
            if desc == [None]:
                return ''
            subject = answers[0]['m.name']
            return '{0}的症状包括：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))

        elif question_type == 'symptom_disease':
            desc = [i['m.name'] for i in answers]
            if desc == [None]:
                return ''
            subject = answers[0]['n.name']
            return '症状{0}可能染上的疾病有：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))

        elif question_type == 'disease_cause':
            desc = [i['m.cause'] for i in answers]
            if desc == [None]:
                return ''
            desc = [';'.join(i) if isinstance(i, list) else i for i in desc]
            subject = answers[0]['m.name']
            return '{0}可能的成因有：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))

        elif question_type == 'disease_prevent':
            desc = [i['m.prevent'] for i in answers]
            if desc == [None]:
                return ''
            desc = [';'.join(i) if isinstance(i, list) else i for i in desc]
            subject = answers[0]['m.name']
            return '{0}的预防措施包括：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))

        elif question_type == 'disease_last_time':
            desc = [i['m.cure_lasttime'] for i in answers]
            if desc == [None]:
                return ''
            desc = [';'.join(i) if isinstance(i, list) else i for i in desc]
            subject = answers[0]['m.name']
            return '{0}治疗可能持续的周期为：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))

        elif question_type == 'disease_cure_way':
            desc = [i['m.cure_way'] for i in answers]
            if desc == [None]:
                return ''
            desc = [';'.join(i) if isinstance(i, list) else i for i in desc]
            subject = answers[0]['m.name']
            return '{0}可以尝试如下治疗：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))

        elif question_type == 'disease_cure_prob':
            desc = [i['m.cured_prob'] for i in answers]
            if desc == [None]:
                return ''
            desc = [';'.join(i) if isinstance(i, list) else i for i in desc]
            subject = answers[0]['m.name']
            return '{0}治愈的概率为（仅供参考）：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))

        elif question_type == 'disease_easy_get':
            desc = [i['m.easy_get'] for i in answers]
            if desc == [None]:
                return ''
            desc = [';'.join(i) if isinstance(i, list) else i for i in desc]
            subject = answers[0]['m.name']
            return '{0}的易感人群包括：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))

        elif question_type == 'disease_desc':
            desc = [i['m.desc'] for i in answers]
            if desc == [None]:
                return ''
            desc = [';'.join(i) if isinstance(i, list) else i for i in desc]
            subject = answers[0]['m.name']
            return '{0}：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))

        elif question_type == 'disease_accompany':
            desc1 = [i['n.name'] for i in answers]
            desc2 = [i['m.name'] for i in answers]
            subject = answers[0]['m.name']
            desc = [i for i in desc1 + desc2 if i != subject]
            if desc == [None]:
                return ''
            return '{0}的并发症包括：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))

        elif question_type == 'disease_not_food':
            desc = [i['n.name'] for i in answers]
            if desc == [None]:
                return ''
            subject = answers[0]['m.name']
            return '{0}忌食的食物包括：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))

        elif question_type == 'disease_do_food':
            do_desc = [i['n.name'] for i in answers if i['r.name'] == '宜吃']
            recommend_desc = [i['n.name'] for i in answers if i['r.name'] == '推荐食谱']
            if do_desc == [None] and recommend_desc == [None]:
                return ''
            subject = answers[0]['m.name']
            if recommend_desc == [None]:
                return '{0}宜食的食物包括：{1}'.format(subject, ';'.join(list(set(do_desc))[:self.num_limit]))
            elif do_desc == [None]:
                return '{0}推荐食谱包括：{1}'.format(subject, ';'.join(list(set(recommend_desc))[:self.num_limit]))
            else:
                return '{0}宜食的食物包括有：{1}\n推荐食谱包括有：{2}'.format(subject, ';'.join(list(set(do_desc))[:self.num_limit]),
                                                             ';'.join(list(set(recommend_desc))[:self.num_limit]))

        elif question_type == 'food_not_disease':
            desc = [i['m.name'] for i in answers]
            if desc == [None]:
                return ''
            subject = answers[0]['n.name']
            return '患有{0}的人最好不要吃{1}'.format('；'.join(list(set(desc))[:self.num_limit]), subject)

        elif question_type == 'food_do_disease':
            desc = [i['m.name'] for i in answers]
            if desc == [None]:
                return ''
            subject = answers[0]['n.name']
            return '患有{0}的人建议多试试{1}'.format('；'.join(list(set(desc))[:self.num_limit]), subject)

        elif question_type == 'disease_drug':
            desc = [i['n.name'] for i in answers]
            if desc == [None]:
                return ''
            subject = answers[0]['m.name']
            return '{0}通常的使用的药品包括：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))

        elif question_type == 'drug_disease':
            desc = [i['m.name'] for i in answers]
            if desc == [None]:
                return ''
            subject = answers[0]['n.name']
            return '{0}主治的疾病有{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))

        elif question_type == 'disease_check':
            desc = [i['n.name'] for i in answers]
            if desc == [None]:
                return ''
            subject = answers[0]['m.name']
            return '{0}通常可以通过以下方式检查出来：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))

        elif question_type == 'check_disease':
            desc = [i['m.name'] for i in answers]
            if desc == [None]:
                return ''
            subject = answers[0]['n.name']
            return '通常可以通过{0}检查出来的疾病有{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit]))

        return ""


if __name__ == '__main__':
    searcher = SQLRunner()
