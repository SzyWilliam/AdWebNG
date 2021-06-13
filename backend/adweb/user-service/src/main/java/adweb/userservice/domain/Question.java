package adweb.userservice.domain;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;

@Entity
public class Question {
    @Id
    @GeneratedValue
    private Long id;

    private String description;

    private String type;

    private String param1;

    private int hot;


    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public int getHot() {
        return hot;
    }

    public void setHot(int hot) {
        this.hot = hot;
    }

    public String getDescription() { return description;}

    public void setDescription(String description) { this.description = description;}

    public String getType() { return type;}

    public void setType(String type) { this.type = type;}

    public String getParam1() { return param1;}

    public void setParam1(String param1) { this.param1 = param1;}
}
