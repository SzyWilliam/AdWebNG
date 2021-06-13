package adweb.userservice.controller.requests;

import java.util.List;

public class NewQueryRequest {

    private String type;
    private String param1;
    private List<String> param2;

    public NewQueryRequest() {
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getParam1() {
        return param1;
    }

    public void setParam1(String param1) {
        this.param1 = param1;
    }

    public List<String> getParam2() {
        return param2;
    }

    public void setParam2(List<String> param2) {
        this.param2 = param2;
    }
}
