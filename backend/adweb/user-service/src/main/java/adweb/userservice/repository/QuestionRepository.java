package adweb.userservice.repository;

import adweb.userservice.domain.Question;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface QuestionRepository extends CrudRepository<Question, Long> {

    List<Question> findByQtypeAndParam1AndDescription(String type, String param1, String des);

    Page<Question> find(Pageable pageable);
}
