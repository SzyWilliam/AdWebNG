package adweb.userservice.service;

import adweb.userservice.domain.Question;
import adweb.userservice.repository.QuestionRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class QuestionService {


    private final QuestionRepository questionRepository;

    @Autowired
    public QuestionService(QuestionRepository questionRepository) {this.questionRepository = questionRepository;}


    public void putQuestion(Question question) {
        Question oldQ = questionRepository.findByQtypeAndParam1AndDescription(question.getQtype(),
                question.getParam1(), question.getDescription()).get(0);
        if (oldQ != null) {
            oldQ.setHot(oldQ.getHot() + 1);
            questionRepository.save(oldQ);
        } else {
            question.setHot(1);
            questionRepository.save(question);
        }
    }

    public List<Question> getPopularQuestions(int topk) {
        Sort sort = Sort.by(Sort.Direction.DESC, "hot");
        Pageable pageable = PageRequest.of(0, topk, sort);
        return questionRepository.find(pageable).toList();
    }
}
