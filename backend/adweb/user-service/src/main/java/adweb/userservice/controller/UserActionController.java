package adweb.userservice.controller;

import adweb.userservice.controller.requests.AnswerRequest;
import adweb.userservice.controller.requests.PostRequest;
import adweb.userservice.domain.Action;
import adweb.userservice.domain.Post;
import adweb.userservice.service.ActionService;
import adweb.userservice.service.PostService;
import com.alibaba.fastjson.JSON;
import org.springframework.web.bind.annotation.*;
import token.JWTUtils;

import java.util.Date;
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
    public Map<String, Object> userActions(Integer num, String email) {
        num = new Integer(1000);

        Map<String, Object> res = new HashMap<>();
        res.put("logs", actionService.getUserActions(email, num));
        return res;
    }

    @RequestMapping(path = "/newquestion", method = RequestMethod.POST)
    @ResponseBody
    public Post createPost(@RequestBody PostRequest request, @RequestHeader("token") String token) {
        Post post = new Post();
        post.setDetail(request.getDetail());
        post.setTitle(request.getTitle());
        post.setEmail(request.getEmail());
        post.setType("question");

        Action action = new Action();
        action.setEmail(JWTUtils.getEmailFromToken(token));
        action.setQuery(request.getTitle());
        action.setType("ASK_QUESTION");
        action.setTime(new Date());
        actionService.saveAction(action);

        return postService.createPost(post);
    }

    @RequestMapping(path = "/reply", method = RequestMethod.POST)
    @ResponseBody
    public Map<String, String> createAnswer(@RequestBody AnswerRequest request,  @RequestHeader("token") String token) {
        Post post = new Post();
        post.setDetail(request.getAnswer());
        post.setType("answer");
        post.setEmail(request.getEmail());
        post.setQid(request.getQid());
        postService.createPost(post);
        Map<String, String> rs = new HashMap<>();
        rs.put("result", "ok");

        Action action = new Action();
        action.setEmail(JWTUtils.getEmailFromToken(token));
        action.setQuery(request.getAnswer());
        action.setType("REPLY_TO_QUESTION");
        action.setTime(new Date());
        actionService.saveAction(action);

        return rs;
    }


    @RequestMapping(path = "/allquestions", method = RequestMethod.GET)
    @ResponseBody
    public List<Post> getAllQuestions(@RequestParam int pageSize, @RequestParam int pageNum) {
        return postService.getQuestions(pageSize * pageNum);
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
