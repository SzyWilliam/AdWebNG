package adweb.userservice.service;

import adweb.userservice.domain.Action;
import adweb.userservice.repository.ActionRepository;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Service;

import java.util.List;

/**
 * @author yanhua
 */
@Service
public class ActionService {
    private final ActionRepository actionRepository;

    @Autowired
    public ActionService(ActionRepository actionRepository) {this.actionRepository = actionRepository;}


    public List<Action> getUserActions(String email, int num){
        Sort sort = Sort.by(Sort.Direction.DESC,"time");
        Pageable pageable =PageRequest.of(0, num, sort);
        return actionRepository.findByEmail(email, pageable).toList();
    }


}

