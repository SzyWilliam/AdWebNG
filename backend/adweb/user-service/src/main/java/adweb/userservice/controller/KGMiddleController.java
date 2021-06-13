package adweb.userservice.controller;

import adweb.userservice.controller.requests.DeleteRequest;
import adweb.userservice.controller.requests.NewQueryRequest;
import adweb.userservice.controller.requests.UpdateRequest;
import com.alibaba.fastjson.JSONObject;
import org.springframework.data.repository.query.Param;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

@RestController
@RequestMapping("/kg")
public class KGMiddleController {

    private static final RestTemplate restTemplate = new RestTemplate();
    private static final String basicUrl = "http://127.0.0.1:8000";

    public <T> ResponseEntity<?> Exchange(String url, T body, HttpMethod method) {
        HttpHeaders headers = new HttpHeaders();
        headers.set("Content-Type", "application/json");
        HttpEntity<T> requestEntity = new HttpEntity<>(body, headers);
        return restTemplate.exchange(url, method, requestEntity, String.class);
    }


    @RequestMapping(path = "/query", method = RequestMethod.GET)
    public JSONObject query(@RequestParam String query) {
        String url = basicUrl + "/qa/kg/query?query=" + query;
        ResponseEntity<?> response = Exchange(url, null, HttpMethod.GET);
        return JSONObject.parseObject((String) response.getBody());
    }

    @RequestMapping(path = "/new", method = RequestMethod.POST)
    public JSONObject newQuery(@RequestBody NewQueryRequest request) {
        String url = basicUrl + "/qa/kg/new";
        ResponseEntity<?> response = Exchange(url, request, HttpMethod.POST);
        return JSONObject.parseObject((String) response.getBody());
    }

    @RequestMapping(path = "/update", method = RequestMethod.POST)
    public JSONObject updateQuery(@RequestBody UpdateRequest request) {
        String url = basicUrl + "/qa/kg/update";
        ResponseEntity<?> response = Exchange(url, request, HttpMethod.POST);
        return JSONObject.parseObject((String) response.getBody());
    }

    @RequestMapping(path = "/delete", method = RequestMethod.POST)
    public JSONObject deleteQuery(@RequestBody DeleteRequest request) {
        String url = "/qa/kg/delete";
        ResponseEntity<?> response = Exchange(url, request, HttpMethod.POST);
        return JSONObject.parseObject((String) response.getBody());
    }



}
