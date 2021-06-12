package adweb.userservice.repository;

import adweb.userservice.domain.Post;
import javafx.geometry.Pos;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.repository.CrudRepository;

public interface PostRepository extends CrudRepository<Post, Long> {
    Page<Post> findAllByType(String type, Pageable pageable);
    Page<Post> findAllByQidAndType(long qid, String type, Pageable pageable);
    Post findById(long qid);
}
