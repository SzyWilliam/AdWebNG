package adweb.userservice.repository;

import adweb.userservice.domain.Question;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface QuestionRepository extends CrudRepository<Question, Long> {
    Question findByTypeAndParam1AndDescription(String type, String param1, String des);

    Page<Question> find(Pageable pageable);
}
