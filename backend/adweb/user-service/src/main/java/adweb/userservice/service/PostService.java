package adweb.userservice.service;

import adweb.userservice.domain.Post;
import adweb.userservice.repository.PostRepository;
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
public class PostService {
    private final PostRepository postRepository;

    @Autowired
    public PostService(PostRepository postRepository) {this.postRepository = postRepository;}

    public Post createPost(Post post) {
        return postRepository.save(post);
    }

    public List<Post> getQuestions(int num) {
        Sort sort = Sort.by(Sort.Direction.DESC, "time");
        Pageable pageable = PageRequest.of(0, num, sort);
        return postRepository.findAllByType("question", pageable).toList();
    }

    public List<Post> getAnswer(long qid, int num) {
        Sort sort = Sort.by(Sort.Direction.DESC, "time");
        Pageable pageable = PageRequest.of(0, num, sort);
        return postRepository.findAllByQidAndType(qid, "answer", pageable).toList();
    }

    public Post getPost(long qid) {
        return postRepository.findById(qid);
    }
}
