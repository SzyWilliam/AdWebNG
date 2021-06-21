# coding: utf-8


class QuestionInsertParser:
    """解析主函数"""

    def insert_parse(self, question_type, param1, param2):
        result = {'question_type': question_type}
        sql = []
        if question_type == 'disease_symptom':
            sql = self.sql_transfer(question_type, param1, param2)

        elif question_type == 'symptom_disease':
            sql = self.sql_transfer(question_type, param1, param2)

        elif question_type == 'disease_cause':
            sql = self.sql_transfer(question_type, param1, param2)

        elif question_type == 'disease_accompany':
            sql = self.sql_transfer(question_type, param1, param2)

        elif question_type == 'disease_not_food':
            sql = self.sql_transfer(question_type, param1, param2)

        elif question_type == 'disease_do_food':
            sql = self.sql_transfer(question_type, param1, param2)

        elif question_type == 'food_not_disease':
            sql = self.sql_transfer(question_type, param1, param2)

        elif question_type == 'food_do_disease':
            sql = self.sql_transfer(question_type, param1, param2)

        elif question_type == 'disease_drug':
            sql = self.sql_transfer(question_type, param1, param2)

        elif question_type == 'drug_disease':
            sql = self.sql_transfer(question_type, param1, param2)

        elif question_type == 'disease_check':
            sql = self.sql_transfer(question_type, param1, param2)

        elif question_type == 'check_disease':
            sql = self.sql_transfer(question_type, param1, param2)

        elif question_type == 'disease_prevent':
            sql = self.sql_transfer(question_type, param1, param2)

        elif question_type == 'disease_last_time':
            sql = self.sql_transfer(question_type, param1, param2)

        elif question_type == 'disease_cure_way':
            sql = self.sql_transfer(question_type, param1, param2)

        elif question_type == 'disease_cure_prob':
            sql = self.sql_transfer(question_type, param1, param2)

        elif question_type == 'disease_easy_get':
            sql = self.sql_transfer(question_type, param1, param2)

        elif question_type == 'disease_desc':
            sql = self.sql_transfer(question_type, param1, param2)

        if sql:
            result['sql'] = sql

        return [result]

    '''针对不同的问题，分开进行处理'''

    def sql_transfer(self, question_type, param1, param2):
        if not param1 or not param2:
            return []

        if len(param2) == 1:
            answer = "\'" + str(param2[0]) + "\'"
        else:
            answer = "["
            for i, a in enumerate(param2):
                if i != 0:
                    answer += ","
                answer = answer + "\'" + str(a) + "\'"
            answer += "]"

        sql = []
        # 病因
        if question_type == 'disease_cause':
            sql = ["MERGE (m:Disease{{name:'{0}'}}) SET m.cause = {1} RETURN m.cause".format(param1, answer)]

        # 预防
        elif question_type == 'disease_prevent':
            sql = ["MERGE (m:Disease{{name:'{0}'}}) SET m.prevent = {1} RETURN m.prevent".format(param1, answer)]

        # 持续时间
        elif question_type == 'disease_last_time':
            sql = ["MERGE (m:Disease{{name:'{0}'}}) SET m.cure_lasttime = {1} RETURN m.cure_lasttime".format(param1,
                                                                                                             answer)]

        # 治愈概率
        elif question_type == 'disease_cure_prob':
            sql = ["MERGE (m:Disease{{name:'{0}'}}) SET m.cured_prob = {1} RETURN m.cured_prob".format(param1, answer)]

        # 治疗方式
        elif question_type == 'disease_cure_way':
            sql = ["MERGE (m:Disease{{name:'{0}'}}) SET m.cure_way = {1} RETURN m.cure_way".format(param1, answer)]

        # 易发人群
        elif question_type == 'disease_easy_get':
            sql = ["MERGE (m:Disease{{name:'{0}'}}) SET m.easy_get = {1} RETURN m.easy_get".format(param1, answer)]

        # 疾病介绍
        elif question_type == 'disease_desc':
            sql = ["MERGE (m:Disease{{name:'{0}'}}) SET m.desc = {1} RETURN m.desc".format(param1, answer)]

        # 疾病症状
        elif question_type == 'disease_symptom':
            sql = [
                "MERGE (m:Disease{{name:'{0}'}}) MERGE (n:Symptom{{name:'{1}'}}) MERGE (m)-[r:has_symptom{{name:'症状'}}]->(n) RETURN r.name".format(
                    param1, i) for i in param2]

        # 症状对症
        elif question_type == 'symptom_disease':
            sql = [
                "MERGE (m:Disease{{name:'{0}'}}) MERGE (n:Symptom{{name:'{1}'}}) MERGE (m)-[r:has_symptom{{name:'症状'}}]->(n) RETURN r.name".format(
                    i, param1) for i in param2]

        # 并发症
        elif question_type == 'disease_accompany':
            sql = [
                "MERGE (m:Disease{{name:'{0}'}}) MERGE (n:Disease{{name:'{1}'}}) MERGE (m)-[r:accompany_with{{name:'并发症'}}]->(n) RETURN r.name".format(
                    param1, i) for i in param2]

        # 忌口
        elif question_type == 'disease_not_food':
            sql = [
                "MERGE (m:Disease{{name:'{0}'}}) MERGE (n:Food{{name:'{1}'}}) MERGE (m)-[r:no_eat{{name:'忌吃'}}]->(n) RETURN r.name".format(
                    param1, i) for i in param2]

        # 宜食
        elif question_type == 'disease_do_food':
            sql = [
                "MERGE (m:Disease{{name:'{0}'}}) MERGE (n:Food{{name:'{1}'}}) MERGE (m)-[r:do_eat{{name:'宜吃'}}]->(n) RETURN r.name".format(
                    param1, i) for i in param2]

        # 忌口对症
        elif question_type == 'food_not_disease':
            sql = [
                "MERGE (m:Disease{{name:'{0}'}}) MERGE (n:Food{{name:'{1}'}}) MERGE (m)-[r:no_eat{{name:'忌吃'}}]->(n) RETURN r.name".format(
                    i, param1) for i in param2]

        # 宜食对症
        elif question_type == 'food_do_disease':
            sql = [
                "MERGE (m:Disease{{name:'{0}'}}) MERGE (n:Food{{name:'{1}'}}) MERGE (m)-[r:do_eat{{name:'宜吃'}}]->(n) RETURN r.name".format(
                    i, param1) for i in param2]

        # 治疗药物
        elif question_type == 'disease_drug':
            sql = [
                "MERGE (m:Disease{{name:'{0}'}}) MERGE (n:Drug{{name:'{1}'}}) MERGE (m)-[r:common_drug{{name:'常用药品'}}]->(n) RETURN r.name".format(
                    param1, i) for i in param2]

        # 药物对症
        elif question_type == 'drug_disease':
            sql = [
                "MERGE (m:Disease{{name:'{0}'}}) MERGE (n:Drug{{name:'{1}'}}) MERGE (m)-[r:common_drug{{name:'常用药品'}}]->(n) RETURN r.name".format(
                    i, param1) for i in param2]

        # 疾病检查
        elif question_type == 'disease_check':
            sql = [
                "MERGE (m:Disease{{name:'{0}'}}) MERGE (n:Check{{name:'{1}'}}) MERGE (m)-[r:need_check{{name:'诊断检查'}}]->(n) RETURN r.name".format(
                    param1, i) for i in param2]

        # 检查对症
        elif question_type == 'check_disease':
            sql = [
                "MERGE (m:Disease{{name:'{0}'}}) MERGE (n:Check{{name:'{1}'}}) MERGE (m)-[r:need_check{{name:'诊断检查'}}]->(n) RETURN r.name".format(
                    i, param1) for i in param2]

        return sql
