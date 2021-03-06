# coding: utf-8

from py2neo import Graph


class SQLRunner:
    def __init__(self):
        self.g = Graph("http://34.196.176.30:7474", auth=("neo4j", "000720"))  # 连接neo4j
        self.g1 = Graph("http://localhost:7474", auth=("neo4j", "000720"))
        self.num_limit = 20

    '''执行cypher查询，并返回相应结果'''

    def run_sql(self, parser_result, sql_type):
        if sql_type == "query_small":
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
        elif sql_type == "query_big":
            final_answers = []
            for query in parser_result:
                question_type = query['question_type']
                sqls = query['sql']
                answers = []
                for sql in sqls:
                    result = self.g1.run(sql).data()
                    answers += result
                final_answer = self.get_answers(question_type, answers)
                if final_answer:
                    final_answers += final_answer
            return final_answers
        elif sql_type == "query_relation":
            sql = "MATCH (m{{name:'{0}'}})-[r]->(n) RETURN r.name, n.name".format(parser_result)
            result = self.g.run(sql).data()
            return result
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
            return ['{0}的症状包括：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit])),
                    '{0}的症状是什么？'.format(subject), subject]

        elif question_type == 'symptom_disease':
            desc = [i['m.name'] for i in answers]
            if desc == [None]:
                return ''
            subject = answers[0]['n.name']
            return ['症状{0}可能染上的疾病有：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit])),
                    '症状为{0}的病有哪些？'.format(subject), subject]

        elif question_type == 'disease_cause':
            desc = [i['m.cause'] for i in answers]
            if desc == [None]:
                return ''
            desc = [';'.join(i) if isinstance(i, list) else i for i in desc]
            subject = answers[0]['m.name']
            return ['{0}可能的成因有：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit])),
                    '{0}的病因可能有哪些？'.format(subject), subject]

        elif question_type == 'disease_prevent':
            desc = [i['m.prevent'] for i in answers]
            if desc == [None]:
                return ''
            desc = [';'.join(i) if isinstance(i, list) else i for i in desc]
            subject = answers[0]['m.name']
            return ['{0}的预防措施包括：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit])),
                    '{0}的预防措施有哪些？'.format(subject), subject]

        elif question_type == 'disease_last_time':
            desc = [i['m.cure_lasttime'] for i in answers]
            if desc == [None]:
                return ''
            desc = [';'.join(i) if isinstance(i, list) else i for i in desc]
            subject = answers[0]['m.name']
            return ['{0}治疗可能持续的周期为：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit])),
                    '{0}需要治疗多长时间？'.format(subject), subject]

        elif question_type == 'disease_cure_way':
            desc = [i['m.cure_way'] for i in answers]
            if desc == [None]:
                return ''
            desc = [';'.join(i) if isinstance(i, list) else i for i in desc]
            subject = answers[0]['m.name']
            return ['{0}可以尝试如下治疗：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit])),
                    "{0}的治疗方法有哪些？".format(subject), subject]

        elif question_type == 'disease_cure_prob':
            desc = [i['m.cured_prob'] for i in answers]
            if desc == [None]:
                return ''
            desc = [';'.join(i) if isinstance(i, list) else i for i in desc]
            subject = answers[0]['m.name']
            return ['{0}治愈的概率为（仅供参考）：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit])),
                    "{0}的治愈概率大概有多少？".format(subject), subject]

        elif question_type == 'disease_easy_get':
            desc = [i['m.easy_get'] for i in answers]
            if desc == [None]:
                return ''
            desc = [';'.join(i) if isinstance(i, list) else i for i in desc]
            subject = answers[0]['m.name']
            return ['{0}的易感人群包括：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit])),
                    "{0}的易感人群有哪些？".format(subject), subject]

        elif question_type == 'disease_desc':
            desc = [i['m.desc'] for i in answers]
            if desc == [None]:
                return ''
            desc = [';'.join(i) if isinstance(i, list) else i for i in desc]
            subject = answers[0]['m.name']
            return ['{0}：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit])), "{0}的简介？".format(subject),
                    subject]

        elif question_type == 'disease_accompany':
            desc1 = [i['n.name'] for i in answers]
            desc2 = [i['m.name'] for i in answers]
            subject = answers[0]['m.name']
            desc = [i for i in desc1 + desc2 if i != subject]
            if desc == [None]:
                return ''
            return ['{0}的并发症包括：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit])),
                    "{0}的并发症有哪些？".format(subject), subject]

        elif question_type == 'disease_not_food':
            desc = [i['n.name'] for i in answers]
            if desc == [None]:
                return ''
            subject = answers[0]['m.name']
            return ['{0}忌食的食物包括：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit])),
                    "得{0}时忌吃的食物有哪些？".format(subject), subject]

        elif question_type == 'disease_do_food':
            do_desc = [i['n.name'] for i in answers if i['r.name'] == '宜吃']
            recommend_desc = [i['n.name'] for i in answers if i['r.name'] == '推荐食谱']
            if do_desc == [None] and recommend_desc == [None]:
                return ''
            subject = answers[0]['m.name']
            if recommend_desc == [None]:
                return ['{0}宜食的食物包括：{1}'.format(subject, ';'.join(list(set(do_desc))[:self.num_limit])),
                        "得{0}时宜吃的食物有哪些？".format(subject), subject]
            elif do_desc == [None]:
                return ['{0}推荐食谱包括：{1}'.format(subject, ';'.join(list(set(recommend_desc))[:self.num_limit])),
                        "得{0}时宜吃的食物有哪些？".format(subject), subject]
            else:
                return ['{0}宜食的食物包括有：{1}\n推荐食谱包括有：{2}'.format(subject, ';'.join(list(set(do_desc))[:self.num_limit]),
                                                              ';'.join(list(set(recommend_desc))[:self.num_limit])),
                        "得{0}时宜吃的食物有哪些？".format(subject), subject]

        elif question_type == 'food_not_disease':
            desc = [i['m.name'] for i in answers]
            if desc == [None]:
                return ''
            subject = answers[0]['n.name']
            return ['患有{0}的人最好不要吃{1}'.format('；'.join(list(set(desc))[:self.num_limit]), subject),
                    "生哪些病时不能吃{0}？".format(subject), subject]

        elif question_type == 'food_do_disease':
            desc = [i['m.name'] for i in answers]
            if desc == [None]:
                return ''
            subject = answers[0]['n.name']
            return ['患有{0}的人建议多试试{1}'.format('；'.join(list(set(desc))[:self.num_limit]), subject),
                    "生哪些病时建议吃{0}？".format(subject), subject]

        elif question_type == 'disease_drug':
            desc = [i['n.name'] for i in answers]
            if desc == [None]:
                return ''
            subject = answers[0]['m.name']
            return ['{0}通常的使用的药品包括：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit])),
                    "{0}常用的治疗药物有哪些？".format(subject), subject]

        elif question_type == 'drug_disease':
            desc = [i['m.name'] for i in answers]
            if desc == [None]:
                return ''
            subject = answers[0]['n.name']
            return ['{0}主治的疾病有{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit])),
                    "{0}这种药主要用来治什么病？".format(subject), subject]

        elif question_type == 'disease_check':
            desc = [i['n.name'] for i in answers]
            if desc == [None]:
                return ''
            subject = answers[0]['m.name']
            return ['{0}通常可以通过以下方式检查出来：{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit])),
                    "{0}主要的检查方式有哪些？".format(subject), subject]

        elif question_type == 'check_disease':
            desc = [i['m.name'] for i in answers]
            if desc == [None]:
                return ''
            subject = answers[0]['n.name']
            return ['通常可以通过{0}检查出来的疾病有{1}'.format(subject, '；'.join(list(set(desc))[:self.num_limit])),
                    "{0}可以检查的疾病有哪些？".format(subject), subject]

        return ""

    def get_answers(self, question_type, answers):
        if not answers or not any(answers):
            return []
        if question_type == 'disease_symptom':
            desc = [i['n.name'] for i in answers]
            if desc == [None]:
                return []
            else:
                return desc

        elif question_type == 'symptom_disease':
            desc = [i['m.name'] for i in answers]
            if desc == [None]:
                return []
            else:
                return desc

        elif question_type == 'disease_cause':
            desc = [i['m.cause'] for i in answers]
            result = []
            for d in desc:
                if isinstance(d, list):
                    result += d
                else:
                    result.append(d)
            if result == [None]:
                return []
            else:
                return result

        elif question_type == 'disease_prevent':
            desc = [i['m.prevent'] for i in answers]
            result = []
            for d in desc:
                if isinstance(d, list):
                    result += d
                else:
                    result.append(d)
            if result == [None]:
                return []
            else:
                return result

        elif question_type == 'disease_last_time':
            desc = [i['m.cure_lasttime'] for i in answers]
            result = []
            for d in desc:
                if isinstance(d, list):
                    result += d
                else:
                    result.append(d)
            if result == [None]:
                return []
            else:
                return result

        elif question_type == 'disease_cure_way':
            desc = [i['m.cure_way'] for i in answers]
            result = []
            for d in desc:
                if isinstance(d, list):
                    result += d
                else:
                    result.append(d)
            if result == [None]:
                return []
            else:
                return result

        elif question_type == 'disease_cure_prob':
            desc = [i['m.cured_prob'] for i in answers]
            result = []
            for d in desc:
                if isinstance(d, list):
                    result += d
                else:
                    result.append(d)
            if result == [None]:
                return []
            else:
                return result

        elif question_type == 'disease_easy_get':
            desc = [i['m.easy_get'] for i in answers]
            result = []
            for d in desc:
                if isinstance(d, list):
                    result += d
                else:
                    result.append(d)
            if result == [None]:
                return []
            else:
                return result

        elif question_type == 'disease_desc':
            desc = [i['m.desc'] for i in answers]
            result = []
            for d in desc:
                if isinstance(d, list):
                    result += d
                else:
                    result.append(d)
            if result == [None]:
                return []
            else:
                return result

        elif question_type == 'disease_accompany':
            desc1 = [i['n.name'] for i in answers]
            desc2 = [i['m.name'] for i in answers]
            subject = answers[0]['m.name']
            desc = [i for i in desc1 + desc2 if i != subject]
            if desc == [None]:
                return []
            else:
                return desc

        elif question_type == 'disease_not_food':
            desc = [i['n.name'] for i in answers]
            if desc == [None]:
                return []
            else:
                return desc

        elif question_type == 'disease_do_food':
            desc = [i['n.name'] for i in answers if i['r.name'] == '宜吃' or i['r.name'] == '推荐食谱']
            if desc == [None]:
                return []
            else:
                return desc

        elif question_type == 'food_not_disease':
            desc = [i['m.name'] for i in answers]
            if desc == [None]:
                return []
            else:
                return desc

        elif question_type == 'food_do_disease':
            desc = [i['m.name'] for i in answers]
            if desc == [None]:
                return []
            else:
                return desc

        elif question_type == 'disease_drug':
            desc = [i['n.name'] for i in answers]
            if desc == [None]:
                return []
            else:
                return desc

        elif question_type == 'drug_disease':
            desc = [i['m.name'] for i in answers]
            if desc == [None]:
                return []
            else:
                return desc

        elif question_type == 'disease_check':
            desc = [i['n.name'] for i in answers]
            if desc == [None]:
                return []
            else:
                return desc

        elif question_type == 'check_disease':
            desc = [i['m.name'] for i in answers]
            if desc == [None]:
                return []
            else:
                return desc

        return ""


if __name__ == '__main__':
    searcher = SQLRunner()
