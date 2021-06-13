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

    }

    public List<Question> getPopularQuestions(int topk) {
        return questionRepository.findTopK(topk);
    }
}
