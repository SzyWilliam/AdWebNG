package adweb.userservice.repository;

import adweb.userservice.domain.Question;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface QuestionRepository extends CrudRepository<Question, Long> {
    Question findByTypeAndParam1AndDescription(String type, String param1, String des);

    @Query(nativeQuery = true, value = "SELECT * FROM Question ORDER BY hot desc LIMIT ?1")
    List<Question> findTopK(int topk);
}
