# coding: utf-8

import threading

from qa.utils.question_classifier import *
from qa.utils.question_query_parser import *
from qa.utils.question_delete_parser import *
from qa.utils.question_update_parser import *
from qa.utils.question_insert_parser import *
from qa.utils.sql_runner import *

'''问答类'''


class KGUtil:
    _instance_lock = threading.Lock()
    _init_flag = False

    def __init__(self):
        if not self._init_flag:
            self._init_flag = True
            self.classifier = QuestionClassifier()
            self.query_parser = QuestionQueryParser()
            self.delete_parser = QuestionDeleteParser()
            self.update_parser = QuestionUpdateParser()
            self.insert_parser = QuestionInsertParser()
            self.runner = SQLRunner()

    def __new__(cls):
        if not hasattr(cls, '_instance'):
            with KGUtil._instance_lock:
                if not hasattr(cls, '_instance'):
                    KGUtil._instance = super().__new__(cls)

        return KGUtil._instance

    def kg_query(self, question):
        classify_result = self.classifier.classify(question)
        if not classify_result:
            return None
        parser_result = self.query_parser.query_parse(classify_result)
        answer = self.runner.run_sql(parser_result, "query")
        if not answer:
            return None
        else:
            result_dict = {"result": "ok", "type": classify_result["question_types"][0], "param1": answer[0][2],
                           "description": answer[0][1]}
            answers = []
            for a in answer:
                answers.append(a[0])
            result_dict["answer"] = answers
            return result_dict

    def kg_delete(self, question):
        classify_result = self.classifier.classify(question)
        if not classify_result:
            return False
        parser_result = self.delete_parser.delete_parse(classify_result)
        return self.runner.run_sql(parser_result, "delete")

    def kg_update(self, question, answers):
        classify_result = self.classifier.classify(question)
        if not classify_result:
            return False
        if not answers or len(answers) == 0:
            return False
        elif len(answers) == 1:
            answer = "\'" + str(answers[0]) + "\'"
        else:
            answer = "["
            for i, a in enumerate(answers):
                if i != 0:
                    answer += ","
                answer = answer + "\'" + str(a) + "\'"
            answer += "]"
        answer_keywords = self.classifier.classify(answer)
        if "args" in answer_keywords:
            answer_keywords = answer_keywords["args"]
        else:
            answer_keywords = {}
        parser_result = self.update_parser.update_parse(classify_result, answer, answer_keywords)
        return self.runner.run_sql(parser_result, "update")

    def kg_insert(self, question_type, param1, param2):
        self.classifier.update_keywords(question_type, param1, param2)
        parser_result = self.insert_parser.insert_parse(question_type, param1, param2)
        return self.runner.run_sql(parser_result, "insert")
