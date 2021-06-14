package adweb.userservice.controller.requests;

import java.util.List;

public class UpdateRequest {
    private String query;
    private List<String> answer;

    public UpdateRequest() {
    }

    public String getQuery() {
        return query;
    }

    public void setQuery(String query) {
        this.query = query;
    }

    public List<String> getAnswer() {
        return answer;
    }

    public void setAnswer(List<String> answer) {
        this.answer = answer;
    }
}
