package adweb.userservice.repository;

import adweb.userservice.domain.Action;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.repository.CrudRepository;

public interface ActionRepository extends CrudRepository<Action, Long> {
    Page<Action> findByEmail(String email, Pageable pageable);

}

