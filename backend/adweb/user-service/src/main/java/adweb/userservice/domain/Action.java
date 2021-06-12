package adweb.userservice.domain;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import java.util.Date;

/**
 * @author yanhua
 */
@Entity
public class Action {
    @Id
    @GeneratedValue
    private Long id;

    private String email;

    private String query;

    private String type;

    private Date time;

    private String extInfo;

    public String getQuery() { return query;}

    public void setQuery(String query) { this.query = query;}

    public String getType() { return type;}

    public void setType(String type) { this.type = type;}


    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public Date getTime() {
        return time;
    }

    public void setTime(Date time) {
        this.time = time;
    }

    public String getExtInfo() { return extInfo;}

    public void setExtInfo(String extInfo) { this.extInfo = extInfo;}
}
