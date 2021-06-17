package adweb.userservice.controller;

import adweb.userservice.controller.requests.AnswerRequest;
import adweb.userservice.controller.requests.PostRequest;
import adweb.userservice.domain.Post;
import adweb.userservice.service.ActionService;
import adweb.userservice.service.PostService;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * @author yanhua
 */
@RestController
@RequestMapping("/user")
public class UserActionController {
    private final ActionService actionService;
    private final PostService postService;

    public UserActionController(ActionService actionService, PostService postService) {
        this.actionService = actionService;
        this.postService = postService;
    }


    @RequestMapping(path = "/logs", method = RequestMethod.GET)
    @ResponseBody
    public Map<String, Object> userActions(int num, String email) {
        Map<String, Object> res = new HashMap<>();
        res.put("logs", actionService.getUserActions(email, num));
        return res;
    }

    @RequestMapping(path = "/newquestion", method = RequestMethod.POST)
    @ResponseBody
    public Post createPost(@RequestBody PostRequest request) {
        Post post = new Post();
        post.setDetail(request.getDetail());
        post.setTitle(request.getTitle());
        post.setEmail(request.getEmail());
        post.setType("question");
        return postService.createPost(post);
    }

    @RequestMapping(path = "/reply", method = RequestMethod.POST)
    @ResponseBody
    public Map<String, String> createAnswer(@RequestBody AnswerRequest request) {
        Post post = new Post();
        post.setDetail(request.getAnswer());
        post.setType("answer");
        post.setEmail(request.getEmail());
        post.setQid(request.getQid());
        Map<String, String> rs = new HashMap<>();
        rs.put("result", "ok");
        return rs;
    }


    @RequestMapping(path = "/allquestions", method = RequestMethod.GET)
    @ResponseBody
    public Map<String, Object> getAllQuestions(@RequestParam int topk) {
        Map<String, Object> rs = new HashMap<>();
        List<Post> questions = postService.getQuestions(topk);
        rs.put("questions", questions);
        return rs;
    }

    @RequestMapping(path = "/questiondetail", method = RequestMethod.GET)
    @ResponseBody
    public Map<String, Object> getQuestionAnswers(long qid, int topk) {
        Map<String, Object> rs = new HashMap<>();
        List<Post> answers = postService.getAnswer(qid, topk);
        Post question = postService.getPost(qid);
        rs.put("questions", question);
        rs.put("answers", answers);
        return rs;
    }
}
