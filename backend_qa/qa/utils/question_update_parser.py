# coding: utf-8


class QuestionUpdateParser:
    """构建类型到关键词的字典"""

    def build_type_keywords_dict(self, args):
        entity_dict = {}
        for arg, types in args.items():
            for t in types:
                if t not in entity_dict:
                    entity_dict[t] = [arg]
                else:
                    entity_dict[t].append(arg)

        return entity_dict

    '''解析主函数'''

    def update_parse(self, classify_result, answer, answer_keywords):
        args = classify_result['args']
        type_keywords = self.build_type_keywords_dict(args)
        type_answer_keywords = self.build_type_keywords_dict(answer_keywords)
        question_types = classify_result['question_types']
        if len(question_types) != 1:
            return []
        results = []
        for question_type in question_types:
            result = {'question_type': question_type}
            sql = []
            if question_type == 'disease_symptom':
                sql = self.sql_transfer(question_type, type_keywords.get('disease'),
                                        type_answer_keywords.get('symptom'))

            elif question_type == 'symptom_disease':
                sql = self.sql_transfer(question_type, type_keywords.get('symptom'),
                                        type_answer_keywords.get('disease'))

            elif question_type == 'disease_cause':
                sql = self.sql_transfer(question_type, type_keywords.get('disease'), answer)

            elif question_type == 'disease_accompany':
                sql = self.sql_transfer(question_type, type_keywords.get('disease'),
                                        type_answer_keywords.get('disease'))

            elif question_type == 'disease_not_food':
                sql = self.sql_transfer(question_type, type_keywords.get('disease'), type_answer_keywords.get('food'))

            elif question_type == 'disease_do_food':
                sql = self.sql_transfer(question_type, type_keywords.get('disease'), type_answer_keywords.get('food'))

            elif question_type == 'food_not_disease':
                sql = self.sql_transfer(question_type, type_keywords.get('food'), type_answer_keywords.get('disease'))

            elif question_type == 'food_do_disease':
                sql = self.sql_transfer(question_type, type_keywords.get('food'), type_answer_keywords.get('disease'))

            elif question_type == 'disease_drug':
                sql = self.sql_transfer(question_type, type_keywords.get('disease'), type_answer_keywords.get('drug'))

            elif question_type == 'drug_disease':
                sql = self.sql_transfer(question_type, type_keywords.get('drug'), type_answer_keywords.get('disease'))

            elif question_type == 'disease_check':
                sql = self.sql_transfer(question_type, type_keywords.get('disease'), type_answer_keywords.get('check'))

            elif question_type == 'check_disease':
                sql = self.sql_transfer(question_type, type_keywords.get('check'), type_answer_keywords.get('disease'))

            elif question_type == 'disease_prevent':
                sql = self.sql_transfer(question_type, type_keywords.get('disease'), answer)

            elif question_type == 'disease_last_time':
                sql = self.sql_transfer(question_type, type_keywords.get('disease'), answer)

            elif question_type == 'disease_cure_way':
                sql = self.sql_transfer(question_type, type_keywords.get('disease'), answer)

            elif question_type == 'disease_cure_prob':
                sql = self.sql_transfer(question_type, type_keywords.get('disease'), answer)

            elif question_type == 'disease_easy_get':
                sql = self.sql_transfer(question_type, type_keywords.get('disease'), answer)

            elif question_type == 'disease_desc':
                sql = self.sql_transfer(question_type, type_keywords.get('disease'), answer)

            if sql:
                result['sql'] = sql

                results.append(result)
        return results

    '''针对不同的问题，分开进行处理'''

    def sql_transfer(self, question_type, keywords, answer):
        if not keywords or not answer:
            return []

        sql = []
        # 病因
        if question_type == 'disease_cause':
            sql = ["MATCH (m:Disease) where m.name = '{0}' SET m.cause = {1} RETURN m.cause".format(i, answer) for i in
                   keywords]

        # 预防
        elif question_type == 'disease_prevent':
            sql = ["MATCH (m:Disease) where m.name = '{0}' SET m.prevent = {1} RETURN m.prevent".format(i, answer) for i
                   in keywords]

        # 持续时间
        elif question_type == 'disease_last_time':
            sql = ["MATCH (m:Disease) where m.name = '{0}' SET m.cure_lasttime = {1} RETURN m.cure_lasttime".format(i,
                                                                                                                    answer)
                   for i in keywords]

        # 治愈概率
        elif question_type == 'disease_cure_prob':
            sql = ["MATCH (m:Disease) where m.name = '{0}' SET m.cured_prob = {1} RETURN m.cured_prob".format(i, answer)
                   for i in keywords]

        # 治疗方式
        elif question_type == 'disease_cure_way':
            sql = ["MATCH (m:Disease) where m.name = '{0}' SET m.cure_way = {1} RETURN m.cure_way".format(i, answer) for
                   i in keywords]

        # 易发人群
        elif question_type == 'disease_easy_get':
            sql = ["MATCH (m:Disease) where m.name = '{0}' SET m.easy_get = {1} RETURN m.easy_get".format(i, answer) for
                   i in keywords]

        # 疾病介绍
        elif question_type == 'disease_desc':
            sql = ["MATCH (m:Disease) where m.name = '{0}' SET m.desc = {1} RETURN m.desc".format(i, answer) for i in
                   keywords]

        # 疾病症状
        elif question_type == 'disease_symptom':
            sql = [
                "MATCH (m:Disease)-[r:has_symptom]->(n:Symptom) where m.name = '{0}' WITH r, r.name AS t DELETE r RETURN t".format(
                    i) for i in keywords]
            for i in keywords:
                for j in answer:
                    sql.append(
                        "MATCH (m:Disease), (n:Symptom) where m.name = '{0}' and n.name = '{1}' CREATE (m)-[r:has_symptom{{name:'症状'}}]->(n) RETURN r.name".format(
                            i, j))

        # 症状对症
        elif question_type == 'symptom_disease':
            sql = [
                "MATCH (m:Disease)-[r:has_symptom]->(n:Symptom) where n.name = '{0}' WITH r, r.name AS t DELETE r RETURN t".format(
                    i) for i in keywords]
            for i in keywords:
                for j in answer:
                    sql.append(
                        "MATCH (m:Disease), (n:Symptom) where m.name = '{0}' and n.name = '{1}' CREATE (m)-[r:has_symptom{{name:'症状'}}]->(n) RETURN r.name".format(
                            j, i))

        # 并发症
        elif question_type == 'disease_accompany':
            sql1 = [
                "MATCH (m:Disease)-[r:accompany_with]->(n:Disease) where m.name = '{0}' WITH r, r.name AS t DELETE r RETURN t".format(
                    i) for i in keywords]
            sql2 = [
                "MATCH (m:Disease)-[r:accompany_with]->(n:Disease) where n.name = '{0}' WITH r, r.name AS t DELETE r RETURN t".format(
                    i) for i in keywords]
            sql = sql1 + sql2
            for i in keywords:
                for j in answer:
                    sql.append(
                        "MATCH (m:Disease), (n:Disease) where m.name = '{0}' and n.name = '{1}' CREATE (m)-[r:accompany_with{{name:'并发症'}}]->(n) RETURN r.name".format(
                            i, j))

        # 忌口
        elif question_type == 'disease_not_food':
            sql = [
                "MATCH (m:Disease)-[r:no_eat]->(n:Food) where m.name = '{0}' WITH r, r.name AS t DELETE r RETURN t".format(
                    i) for i in keywords]
            for i in keywords:
                for j in answer:
                    sql.append(
                        "MATCH (m:Disease), (n:Food) where m.name = '{0}' and n.name = '{1}' CREATE (m)-[r:no_eat{{name:'忌吃'}}]->(n) RETURN r.name".format(
                            i, j))

        # 宜食
        elif question_type == 'disease_do_food':
            sql1 = [
                "MATCH (m:Disease)-[r:do_eat]->(n:Food) where m.name = '{0}' WITH r, r.name AS t DELETE r RETURN t".format(
                    i) for i in keywords]
            sql2 = [
                "MATCH (m:Disease)-[r:recommend_eat]->(n:Food) where m.name = '{0}' WITH r, r.name AS t DELETE r RETURN t".format(
                    i) for i in keywords]
            for i in keywords:
                for j in answer:
                    sql.append(
                        "MATCH (m:Disease), (n:Food) where m.name = '{0}' and n.name = '{1}' CREATE (m)-[r:do_eat{{name:'宜吃'}}]->(n) RETURN r.name".format(
                            i, j))
            sql = sql1 + sql2

        # 忌口对症
        elif question_type == 'food_not_disease':
            sql = [
                "MATCH (m:Disease)-[r:no_eat]->(n:Food) where n.name = '{0}' WITH r, r.name AS t DELETE r RETURN t".format(
                    i) for i in keywords]
            for i in keywords:
                for j in answer:
                    sql.append(
                        "MATCH (m:Disease), (n:Food) where m.name = '{0}' and n.name = '{1}' CREATE (m)-[r:no_eat{{name:'忌吃'}}]->(n) RETURN r.name".format(
                            j, i))

        # 宜食对症
        elif question_type == 'food_do_disease':
            sql1 = [
                "MATCH (m:Disease)-[r:do_eat]->(n:Food) where n.name = '{0}' WITH r, r.name AS t DELETE r RETURN t".format(
                    i) for i in keywords]
            sql2 = [
                "MATCH (m:Disease)-[r:recommend_eat]->(n:Food) where n.name = '{0}' WITH r, r.name AS t DELETE r RETURN t".format(
                    i) for i in keywords]
            sql = sql1 + sql2
            for i in keywords:
                for j in answer:
                    sql.append(
                        "MATCH (m:Disease), (n:Food) where m.name = '{0}' and n.name = '{1}' CREATE (m)-[r:do_eat{{name:'宜吃'}}]->(n) RETURN r.name".format(
                            j, i))

        # 治疗药物
        elif question_type == 'disease_drug':
            sql1 = [
                "MATCH (m:Disease)-[r:common_drug]->(n:Drug) where m.name = '{0}' WITH r, r.name AS t DELETE r RETURN t".format(
                    i) for i in keywords]
            sql2 = [
                "MATCH (m:Disease)-[r:recommend_drug]->(n:Drug) where m.name = '{0}' WITH r, r.name AS t DELETE r RETURN t".format(
                    i) for i in keywords]
            sql = sql1 + sql2
            for i in keywords:
                for j in answer:
                    sql.append(
                        "MATCH (m:Disease), (n:Drug) where m.name = '{0}' and n.name = '{1}' CREATE (m)-[r:common_drug{{name:'常用药品'}}]->(n) RETURN r.name".format(
                            i, j))

        # 药物对症
        elif question_type == 'drug_disease':
            sql1 = [
                "MATCH (m:Disease)-[r:common_drug]->(n:Drug) where n.name = '{0}' WITH r, r.name AS t DELETE r RETURN t".format(
                    i) for i in keywords]
            sql2 = [
                "MATCH (m:Disease)-[r:recommend_drug]->(n:Drug) where n.name = '{0}' WITH r, r.name AS t DELETE r RETURN t".format(
                    i) for i in keywords]
            sql = sql1 + sql2
            for i in keywords:
                for j in answer:
                    sql.append(
                        "MATCH (m:Disease), (n:Drug) where m.name = '{0}' and n.name = '{1}' CREATE (m)-[r:common_drug{{name:'常用药品'}}]->(n) RETURN r.name".format(
                            j, i))

        # 疾病检查
        elif question_type == 'disease_check':
            sql = [
                "MATCH (m:Disease)-[r:need_check]->(n:Check) where m.name = '{0}' WITH r, r.name AS t DELETE r RETURN t".format(
                    i) for i in keywords]
            for i in keywords:
                for j in answer:
                    sql.append(
                        "MATCH (m:Disease), (n:Check) where m.name = '{0}' and n.name = '{1}' CREATE (m)-[r:need_check{{name:'诊断检查'}}]->(n) RETURN r.name".format(
                            i, j))

        # 检查对症
        elif question_type == 'check_disease':
            sql = [
                "MATCH (m:Disease)-[r:need_check]->(n:Check) where n.name = '{0}' WITH r, r.name AS t DELETE r RETURN t".format(
                    i) for i in keywords]
            for i in keywords:
                for j in answer:
                    sql.append(
                        "MATCH (m:Disease), (n:Check) where m.name = '{0}' and n.name = '{1}' CREATE (m)-[r:need_check{{name:'诊断检查'}}]->(n) RETURN r.name".format(
                            j, i))
        return sql
