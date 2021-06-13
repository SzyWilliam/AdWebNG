package adweb.userservice.controller;

import adweb.userservice.controller.requests.DeleteRequest;
import adweb.userservice.controller.requests.NewQueryRequest;
import adweb.userservice.controller.requests.UpdateRequest;
import adweb.userservice.domain.Action;
import adweb.userservice.domain.Question;
import adweb.userservice.service.ActionService;
import adweb.userservice.service.QuestionService;
import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;
import token.JWTUtils;

import java.util.Date;
import java.util.HashMap;
import java.util.Map;

@RestController
@RequestMapping("/kg")
public class KGMiddleController {


    private final ActionService actionService;
    private final QuestionService questionService;

    private static final RestTemplate restTemplate = new RestTemplate();
    private static final String basicUrl = "http://127.0.0.1:8000";

    @Autowired
    public KGMiddleController(ActionService actionService, QuestionService questionService) {
        this.actionService = actionService;
        this.questionService = questionService;
    }

    public <T> ResponseEntity<?> Exchange(String url, T body, HttpMethod method) {
        HttpHeaders headers = new HttpHeaders();
        headers.set("Content-Type", "application/json");
        HttpEntity<T> requestEntity = new HttpEntity<>(body, headers);
        return restTemplate.exchange(url, method, requestEntity, String.class);
    }


    @RequestMapping(path = "/query", method = RequestMethod.GET)
    public JSONObject query(@RequestParam String query, @RequestHeader("token") String token) {
        String url = basicUrl + "/qa/kg/query?query=" + query;
        ResponseEntity<?> response = Exchange(url, null, HttpMethod.GET);
        Action action = new Action();
        action.setEmail(JWTUtils.getEmailFromToken(token));
        action.setQuery(query);
        action.setType("GET");
        action.setTime(new Date());
        actionService.saveAction(action);

        JSONObject result = JSONObject.parseObject((String) response.getBody());
        Question question = new Question();
        question.setQtype(result.getString("type"));
        question.setParam1(result.getString("param1"));
        question.setDescription(result.getString("description"));
        questionService.putQuestion(question);
        return result;
    }

    @RequestMapping(path = "/new", method = RequestMethod.POST)
    public JSONObject newQuery(@RequestBody NewQueryRequest request, @RequestHeader("token") String token) {
        String url = basicUrl + "/qa/kg/new";
        ResponseEntity<?> response = Exchange(url, request, HttpMethod.POST);
        Action action = new Action();
        action.setEmail(JWTUtils.getEmailFromToken(token));
        action.setQuery(JSON.toJSONString(request));
        action.setType("ADD");
        action.setTime(new Date());
        actionService.saveAction(action);
        return JSONObject.parseObject((String) response.getBody());
    }

    @RequestMapping(path = "/update", method = RequestMethod.POST)
    public JSONObject updateQuery(@RequestBody UpdateRequest request, @RequestHeader("token") String token) {
        String url = basicUrl + "/qa/kg/update";
        ResponseEntity<?> response = Exchange(url, request, HttpMethod.POST);
        Action action = new Action();
        action.setEmail(JWTUtils.getEmailFromToken(token));
        action.setQuery(JSON.toJSONString(request));
        action.setType("MODIFY");
        action.setTime(new Date());
        actionService.saveAction(action);
        return JSONObject.parseObject((String) response.getBody());
    }

    @RequestMapping(path = "/delete", method = RequestMethod.POST)
    public JSONObject deleteQuery(@RequestBody DeleteRequest request, @RequestHeader("token") String token) {
        String url = "/qa/kg/delete";
        ResponseEntity<?> response = Exchange(url, request, HttpMethod.POST);
        Action action = new Action();
        action.setEmail(JWTUtils.getEmailFromToken(token));
        action.setQuery(request.getQuery());
        action.setType("DELETE");
        action.setTime(new Date());
        actionService.saveAction(action);
        return JSONObject.parseObject((String) response.getBody());
    }

    @GetMapping("/popular")
    public Map<String, Object> getPopularQuestions(@RequestParam int topk) {

        Map<String, Object> result = new HashMap<>();
        result.put("result", questionService.getPopularQuestions(topk));
        return result;
    }

}
