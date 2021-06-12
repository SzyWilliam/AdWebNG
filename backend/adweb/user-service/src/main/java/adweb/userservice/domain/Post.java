package adweb.userservice.domain;

import com.fasterxml.jackson.annotation.JsonProperty;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import java.util.Date;

/**
 * @author yanhua
 */
@Entity
public class Post {
    @Id
    @GeneratedValue
    private Long id;

    private String email;

    private String title;

    private String detail;

    /**
     * post type：question or answer
     */
    private String type;

    /**
     * the question id for an answer
     * for the type of 'question', this is 'null'
     */
    private String qid;


    private Date time;


    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public Date getTime() {
        return time;
    }

    public void setTime(Date time) {
        this.time = time;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getQid() {
        return qid;
    }

    public void setQid(String qid) {
        this.qid = qid;
    }

    public String getEmail() { return email;}

    public void setEmail(String email) { this.email = email;}

    public String getTitle() { return title;}

    public void setTitle(String title) { this.title = title;}

    public String getDetail() { return detail;}

    public void setDetail(String detail) { this.detail = detail;}
}
